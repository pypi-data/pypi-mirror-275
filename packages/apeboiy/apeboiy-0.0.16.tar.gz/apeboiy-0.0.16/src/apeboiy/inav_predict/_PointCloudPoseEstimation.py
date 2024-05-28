import json
import logging
import os
import random

import kagglehub
import matplotlib.pyplot as plt
import numpy as np
import onnxruntime as ort
import plotly.graph_objects as go
import plotly.io as pio
import seaborn as sns
from apeboiy.ply import Reader
from PIL import Image
from tqdm import tqdm


def preprocess_image(img_path):
    img = Image.open(img_path)
    img_array = np.array(img).astype(np.float32)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def create_3d_scatter(vertices, plot_table=False, elev=30, azim=30, save_path=None, ext=None, image=None):
    """
    Create a 3D scatter plot with optional image overlay using Seaborn styling and Matplotlib.

    Args:
    - vertices (DataFrame): DataFrame containing 'Position' and 'Color' columns for vertex positions and colors.
    - plot_table (bool): Whether to display a table of vertex coordinates.
    - elev (int): Elevation angle in the z plane for the plot view.
    - azim (int): Azimuth angle in the x,y plane for the plot view.
    - save_path (str): Path to save the plot image. If None, an exception is raised.
    - ext (dict): Additional plotting information, including predictions and plot types.
    - image (str or np.ndarray): Optional image to display alongside the plot. Can be a file path or an image array.

    Returns:
    - None
    """
    # Set Seaborn style
    sns.set(style="whitegrid")
    if ext is None:
        ext = {}

    # Extract positions and normalize colors
    positions = np.array(vertices["Position"].tolist())
    colors = np.array(vertices["Color"].tolist()) / 255.0

    # Initialize the figure
    fig = plt.figure(figsize=(12, 8))

    # Create subplot layout based on whether an image is provided
    if image is not None:
        ax_image = fig.add_subplot(121)
        ax = fig.add_subplot(122, projection='3d')
    else:
        ax = fig.add_subplot(111, projection='3d')

    # Display the image if provided
    if image is not None:
        if isinstance(image, str):
            if not os.path.exists(image):
                raise FileNotFoundError(f"Image file not found: {image}")
            image = Image.open(image)
        image = np.array(image)
        ax_image.imshow(image)
        ax_image.axis('off')

    # Create 3D scatter plot
    ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2], color=colors, s=1)

    # Process additional plotting information if provided
    if "pred" in ext:
        table_data = []
        for res in ext["pred"]:
            pred_vertices = res["vertices"]
            table_data.extend(pred_vertices)
            plot_type = res["plot_type"]
            color = res["color"]
            size = res.get("size", 1)
            alpha = res.get("alpha", 1.0)

            if plot_type == "scatter":
                for p in pred_vertices:
                    ax.scatter(p[0], p[1], p[2], color=color, s=size)
            elif plot_type == "line":
                for p in pred_vertices:
                    x, y, z = p
                    ax.plot([x, x], [y, y], [-15, 15], color=color, alpha=alpha)  # z-axis
                    ax.plot([x, x], [-15, 15], [z, z], color=color, alpha=alpha)  # y-axis
                    ax.plot([-15, 15], [y, y], [z, z], color=color, alpha=alpha)  # x-axis

        # Display table of first 10 points if required
        if plot_table and len(table_data) > 0:
            table_data = np.array(table_data[:10])
            columns = ["X", "Y", "Z"]
            rows = [f"Point {i}" for i in range(1, len(table_data) + 1)]
            cell_text = [[f"{x:.2f}", f"{y:.2f}", f"{z:.2f}"] for x, y, z in table_data]
            table = ax.table(cellText=cell_text, rowLabels=rows, colLabels=columns, loc='bottom')
            table.auto_set_font_size(False)

    # Set plot labels and title
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("3D Point Cloud")

    # Set fixed scale
    max_range = np.array([positions[:, i].max() - positions[:, i].min() for i in range(3)]).max() / 2.0
    mid_x = (positions[:, 0].max() + positions[:, 0].min()) / 2.0
    mid_y = (positions[:, 1].max() + positions[:, 1].min()) / 2.0
    mid_z = (positions[:, 2].max() + positions[:, 2].min()) / 2.0

    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    # Adjust the view angle
    ax.view_init(elev=elev, azim=azim)

    # Save or show the plot
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
    plt.close()

def create_interactive_3d_scatter(vertices, verbose, plot_table,save_path=None, ext=None):
    """
    Create an interactive 3D scatter plot using Plotly.

    Args:
    - vertices: DataFrame containing vertex positions and colors
    - save_path: Path to save the HTML file. If None, the plot is displayed.
    - ext: Dictionary containing additional plotting instructions

    Returns:
    - None
    """

    if verbose:
        logging.info("Creating interactive 3D scatter plot...")
        logging.info(f"Number of vertices: {len(vertices)}")
        logging.info(f"""Configuring plot... {json.dumps(
            {   "save_path": save_path,
                "plot_table": plot_table}, indent=2)
        }"""
                     )


    def extract_positions_and_colors(vertices):
        positions = np.array(vertices["Position"].tolist())
        colors = np.array(vertices["Color"].tolist()) / 255.0  # Normalize colors
        return positions, colors

    def create_scatter_plot(positions, colors):
        return go.Scatter3d(
            x=positions[:, 0],
            y=positions[:, 1],
            z=positions[:, 2],
            mode="markers",
            marker=dict(size=3, color=colors, opacity=0.8),
        )

    def add_additional_elements(data, ext):
        if ext is None:
            return data

        for res in ext.get("pred", []):
            vertices = np.array(res["vertices"])
            plot_type = res["plot_type"]
            color = res["color"]

            if plot_type == "scatter":
                alpha = res["alpha"]
                scatter_additional = go.Scatter3d(
                    x=vertices[:, 0],
                    y=vertices[:, 1],
                    z=vertices[:, 2],
                    mode="markers",
                    marker=dict(size=3, color=color, opacity=alpha),
                )
                data.append(scatter_additional)
            elif plot_type == "line":
                add_lines(data, vertices, color)

        return data

    def add_lines(data, vertices, color):
        for vertex in vertices:
            x, y, z = vertex
            data.extend([
                create_line([x, x], [y, y], [-15, 15], color),
                create_line([x, x], [-15, 15], [z, z], color),
                create_line([-15, 15], [y, y], [z, z], color),
            ])

    def create_line(x, y, z, color):
        return go.Scatter3d(
            x=x, y=y, z=z,
            mode="lines",
            line=dict(color=color, width=1),
        )

    def create_table(result):
        column = ["X", "Y", "Z"]
        cell_text = [
            [f"{row[0]:.2f}", f"{row[1]:.2f}", f"{row[2]:.2f}"]
            for res in result[:10]
            for row in res.tolist() if isinstance(res, (np.ndarray, list))
        ]

        return go.Table(
            header=dict(values=column),
            cells=dict(values=list(zip(*cell_text)), align="center"),
            domain=dict(x=[0, 0.3], y=[0, 0.2]),  # Position the table at the bottom
        )

    def setup_layout():
        return go.Layout(
            scene=dict(
                xaxis=dict(title="X", range=[-15, 15]),
                yaxis=dict(title="Y", range=[-15, 15]),
                zaxis=dict(title="Z", range=[-15, 15]),
            ),
            title="Interactive 3D Point Cloud",
            height=800,
            width=1200,
        )

    positions, colors = extract_positions_and_colors(vertices)
    scatter = create_scatter_plot(positions, colors)
    data = add_additional_elements([scatter], ext)

    if ext:
        result = [np.array(res["vertices"]) for res in ext.get("pred", [])]
        if result and plot_table:
            table = create_table(result)
            data.append(table)

    fig = go.Figure(data=data, layout=setup_layout())

    if save_path:
        pio.write_html(fig, save_path)
    else:
        raise NotImplementedError("Displaying the plot is not supported.")

class PointCloudPoseEstimation:
    ply = None
    session = None
    input_name = None
    output_name = None

    def __init__(
            self,
            model_repo,
            model_name,
            ply_file,
            image_dir,
            output_dir,
            num_images,
            plot_table,
            out_format=None,
            verbose=False,
    ):
        self.num_images = num_images
        self.model_repo = model_repo
        self.model_name = model_name
        self.ply_file = ply_file
        self.image_dir = image_dir
        self.output_dir = output_dir
        self.out_format = out_format
        self.verbose = verbose
        self.plot_table = plot_table

        logging.basicConfig(level=logging.DEBUG if verbose else logging.INFO)

    def download_model(self):
        logging.info("Downloading model from KaggleHub...")
        path = kagglehub.model_download(self.model_repo)
        model_file_path = os.path.join(path, self.model_name)

        # save an installation path to tasks-lock.json
        config = {}
        if os.path.exists("tasks-lock.json"):
            with open("tasks-lock.json", "r") as f:
                config = json.load(f)
        config["model_install_path"] = path
        with open("tasks-lock.json", "w") as f:
            f.write(json.dumps(config, indent=2))

        total_size = os.path.getsize(model_file_path)
        chunk_size = 1024

        progress_bar = tqdm(
            total=total_size, unit="B", unit_scale=True, desc="Downloading", leave=False
        )

        with open(model_file_path, "rb") as f:
            for chunk in iter(lambda: f.read(chunk_size), b""):
                progress_bar.update(len(chunk))

        progress_bar.close()

        logging.info("Model downloaded successfully.")

    def load_point_cloud(self):
        logging.info("Loading point cloud from PLY file...")
        self.ply = Reader(self.ply_file)
        self.ply.read()
        logging.info("Point cloud loaded successfully.")

    def run_inference(self, img_array):
        return self.session.run([self.output_name], {self.input_name: img_array})

    def plot_results(self, res, index, img):
        if self.out_format == "html":
            create_interactive_3d_scatter(
                self.ply.vertices,
                verbose=self.verbose,
                save_path=os.path.join(self.output_dir, f"pointcloud_{index}.html"),
                ext={
                    "pred": [
                        {
                            "vertices": [
                                res[0][0][i : i + 3]
                                for i in range(0, len(res[0][0]) - 3)
                            ],
                            "color": "red",
                            "plot_type": "line",
                        }
                    ]
                },
                plot_table=self.plot_table,
            )

        elif self.out_format == "png":
            create_3d_scatter(
                self.ply.vertices,
                save_path=os.path.join(self.output_dir, f"pointcloud_{index}.png"),
                elev=130,
                azim=300,
                ext={
                    "pred": [
                        {
                            "vertices": [
                                res[0][0][i : i + 3]
                                for i in range(0, len(res[0][0]) - 3)
                            ],
                            "color": "red",
                            "plot_type": "line",
                        }
                    ]
                },
                plot_table=self.plot_table,
                image=img
            )

    def execute(self):

        lock_file = "tasks-lock.json"
        if not os.path.exists(lock_file):
            raise FileNotFoundError(f"Tasks lock file not found: {lock_file}")

        with open(lock_file, "r") as f:
            config = json.load(f)

            self.session = ort.InferenceSession(
                config.get("model_install_path") + "/" + self.model_name
            )
            self.input_name = self.session.get_inputs()[0].name
            self.output_name = self.session.get_outputs()[0].name

        self.load_point_cloud()
        image_files = os.listdir(self.image_dir)
        if self.num_images > len(image_files):
            if self.verbose:
                logging.warning(
                    f"Number of images to process is greater than the number of images in the directory: {len(image_files)}"
                )
                self.num_images = len(image_files)
        elif len(image_files) == 0:
            raise FileNotFoundError(
                f"No images found in the directory: {self.image_dir}"
            )

        if self.num_images > 10:
            logging.warning(
                f"Number of images to process is big: {self.num_images} the process may take a while..."
            )

        if self.verbose:
            logging.info("Starting inference...")

        random_images = random.sample(image_files, self.num_images)
        pred_results = []
        with tqdm(
                total=self.num_images, desc="Processing Images", unit="image", leave=False
        ) as pbar:
            for i, img_file in enumerate(random_images):
                img_path = os.path.join(self.image_dir, img_file)
                img_array = preprocess_image(img_path)
                res = self.run_inference(img_array)
                pred_results.append(res)
                if self.verbose:
                    logging.info(f"Image {i + 1} at {img_path} processed successfully.")

                # absoulte path to image
                self.plot_results(res, i, os.path.join(os.getcwd(), img_path))
                pbar.set_postfix(file=img_file)
                pbar.update(1)

        if self.verbose:
            logging.info("Results:")
            for i, res in enumerate(pred_results):
                logging.info(f"Image {i + 1}: {res[0][0][:3]}")
        logging.info("All images processed successfully.")
