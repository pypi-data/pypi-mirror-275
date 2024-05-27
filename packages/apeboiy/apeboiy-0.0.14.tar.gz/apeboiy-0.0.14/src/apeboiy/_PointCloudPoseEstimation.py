import os
import random
import logging
from tqdm import tqdm
import kagglehub
import numpy as np
import onnxruntime as ort
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.io as pio
from PIL import Image
from apeboiy.ply import Reader


def preprocess_image(img_path):
    img = Image.open(img_path)
    img_array = np.array(img).astype(np.float32)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


def create_3d_scatter(vertices, elev=30, azim=30, save_path=None, ext=None):
    """
    Create a 3D scatter plot using Seaborn styling and Matplotlib.

    Args:
    - vertices: DataFrame containing vertex positions and colors
    - elev: Elevation angle in the z plane
    - azim: Azimuth angle in the x,y plane
    - save_path: Path to save the plot image. If None, the plot is shown.

    Returns:
    - None
    """
    # Set the Seaborn style
    if ext is None:
        ext = {}
    sns.set(style="whitegrid")

    # Extract positions and colors
    positions = np.array(vertices["Position"].tolist())
    colors = np.array(vertices["Color"].tolist()) / 255.0  # Normalize colors

    # Create a 3D plot
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection="3d")

    # Scatter plot
    ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2], color=colors, s=1)

    if "pred" in ext:
        table = []
        for res in ext["pred"]:
            vertices = res["vertices"]
            table.append(vertices[0])
            types = res["plot_type"]
            if types == "scatter":
                for p in vertices:
                    ax.scatter(
                        p[0], p[1], p[2], color=res["color"], s=res.get("size", 1)
                    )
            if types == "line":
                for p in vertices:
                    x, y, z = p
                    ax.plot(
                        [x, x],
                        [y, y],
                        [-15, 15],
                        color=res["color"],
                        alpha=res.get("alpha", 1.0),
                    )  # z-axis
                    ax.plot(
                        [x, x],
                        [-15, 15],
                        [z, z],
                        color=res["color"],
                        alpha=res.get("alpha", 1.0),
                    )  # y-axis
                    ax.plot(
                        [-15, 15],
                        [y, y],
                        [z, z],
                        color=res["color"],
                        alpha=res.get("alpha", 1.0),
                    )  # x-axis

        # show table of results(ext[pred][vertices]) (if any and not exceeding 10)
        table = np.array(table)
        table = table[:10]

        if len(table) > 0:
            columns = ["X", "Y", "Z"]
            rows = [f"Point {i}" for i in range(1, len(table) + 1)]
            cell_text = []
            for row in table:
                cell_text.append([f"{row[0]:.2f}", f"{row[1]:.2f}", f"{row[2]:.2f}"])
            table = ax.table(
                cellText=cell_text, rowLabels=rows, colLabels=columns, loc="bottom"
            )  # Changed loc to "bottom"
            table.auto_set_font_size(False)

    # Set labels
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    # Set title
    ax.set_title("3D point cloud")

    # Set fixed scale
    max_range = (
        np.array(
            [
                positions[:, 0].max() - positions[:, 0].min(),
                positions[:, 1].max() - positions[:, 1].min(),
                positions[:, 2].max() - positions[:, 2].min(),
            ]
        ).max()
        / 2.0
    )

    mid_x = (positions[:, 0].max() + positions[:, 0].min()) * 0.5
    mid_y = (positions[:, 1].max() + positions[:, 1].min()) * 0.5
    mid_z = (positions[:, 2].max() + positions[:, 2].min()) * 0.5

    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    # Rotate the plot
    ax.view_init(elev=elev, azim=azim)

    # Save the plot if save_path is provided, otherwise show the plot
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
    plt.close()


def create_interactive_3d_scatter(vertices, save_path=None, ext=None):
    """
    Create an interactive 3D scatter plot using Plotly.

    Args:
    - vertices: DataFrame containing vertex positions and colors
    - save_path: Path to save the HTML file. If None, the plot is displayed.
    - ext: Dictionary containing additional plotting instructions

    Returns:
    - None
    """
    # Extract positions and colors
    positions = np.array(vertices["Position"].tolist())
    colors = np.array(vertices["Color"].tolist()) / 255.0  # Normalize colors

    # Create a scatter plot
    scatter = go.Scatter3d(
        x=positions[:, 0],
        y=positions[:, 1],
        z=positions[:, 2],
        mode="markers",
        marker=dict(size=3, color=colors, opacity=0.8),
    )

    data = [scatter]

    # Add additional elements from ext parameter
    if ext is not None:
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
                # Draw lines parallel to axes
                for vertex in vertices:
                    x, y, z = vertex
                    # Draw lines parallel to z-axis
                    line_z = go.Scatter3d(
                        x=[x, x],
                        y=[y, y],
                        z=[-15, 15],
                        mode="lines",
                        line=dict(color=color, width=1),
                    )
                    data.append(line_z)

                    # Draw lines parallel to y-axis
                    line_y = go.Scatter3d(
                        x=[x, x],
                        y=[-15, 15],
                        z=[z, z],
                        mode="lines",
                        line=dict(color=color, width=1),
                    )
                    data.append(line_y)

                    # Draw lines parallel to x-axis
                    line_x = go.Scatter3d(
                        x=[-15, 15],
                        y=[y, y],
                        z=[z, z],
                        mode="lines",
                        line=dict(color=color, width=1),
                    )
                    data.append(line_x)

    # Set up the layout
    layout = go.Layout(
        scene=dict(
            xaxis=dict(title="X", range=[-15, 15]),
            yaxis=dict(title="Y", range=[-15, 15]),
            zaxis=dict(title="Z", range=[-15, 15]),
        ),
        title="Interactive 3D Point Cloud",
    )

    # Create the figure
    fig = go.Figure(data=data, layout=layout)

    # Save the plot if save_path is provided, otherwise show the plot
    if save_path:
        pio.write_html(fig, save_path)
    else:
        pio.show(fig)


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

        logging.basicConfig(level=logging.DEBUG if verbose else logging.INFO)

    def download_model(self):
        logging.info("Downloading model from KaggleHub...")
        path = kagglehub.model_download(self.model_repo)
        model_file_path = os.path.join(path, self.model_name)

        total_size = os.path.getsize(model_file_path)
        chunk_size = 1024  # 1KB

        progress_bar = tqdm(
            total=total_size, unit="B", unit_scale=True, desc="Downloading", leave=False
        )

        with open(model_file_path, "rb") as f:
            for chunk in iter(lambda: f.read(chunk_size), b""):
                progress_bar.update(len(chunk))

        progress_bar.close()

        self.session = ort.InferenceSession(model_file_path)
        self.input_name = self.session.get_inputs()[0].name
        self.output_name = self.session.get_outputs()[0].name
        logging.info("Model downloaded successfully.")

    def load_point_cloud(self):
        logging.info("Loading point cloud from PLY file...")
        self.ply = Reader(self.ply_file)
        self.ply.read()
        logging.info("Point cloud loaded successfully.")

    def run_inference(self, img_array):
        return self.session.run([self.output_name], {self.input_name: img_array})

    def plot_results(self, res, index):
        if self.out_format is not None:
            if self.out_format == "html":
                create_interactive_3d_scatter(
                    self.ply.vertices,
                    save_path=os.path.join(self.output_dir, f"pointcloud_{index}.html"),
                    ext={
                        "pred": [
                            {
                                "vertices": [res[0][0][:3]],
                                "color": "red",
                                "plot_type": "line",
                            }
                        ]
                    },
                )

        else:
            create_3d_scatter(
                self.ply.vertices,
                save_path=os.path.join(self.output_dir, f"pointcloud_{index}.png"),
                elev=130,
                azim=300,
                ext={
                    "pred": [
                        {
                            "vertices": [res[0][0][:3]],
                            "color": "red",
                            "plot_type": "line",
                        }
                    ]
                },
            )

    def execute(self):
        self.download_model()
        self.load_point_cloud()
        image_files = os.listdir(self.image_dir)
        random_images = random.sample(image_files, self.num_images)

        with tqdm(
            total=self.num_images, desc="Processing Images", unit="image", leave=False
        ) as pbar:
            for i, img_file in enumerate(random_images):
                img_path = os.path.join(self.image_dir, img_file)
                img_array = preprocess_image(img_path)
                res = self.run_inference(img_array)
                self.plot_results(res, i)
                pbar.set_postfix(file=img_file)
                pbar.update(1)

        logging.info("All images processed successfully.")
