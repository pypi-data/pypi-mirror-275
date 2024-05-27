import os
import argparse
import random
import json
import logging
from tqdm import tqdm
import kagglehub
import numpy as np
import onnxruntime as ort
from PIL import Image
from script import create_3d_scatter
from apeboiy.ply import Reader

def preprocess_image(img_path):
    img = Image.open(img_path)
    img_array = np.array(img).astype(np.float32)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


class PointCloudPoseEstimation:
    ply = None
    session = None
    input_name = None
    output_name = None

    def __init__(self, model_repo, model_name, ply_file, image_dir, output_dir, num_images, verbose=False):
        self.num_images = num_images
        self.model_repo = model_repo
        self.model_name = model_name
        self.ply_file = ply_file
        self.image_dir = image_dir
        self.output_dir = output_dir
        self.verbose = verbose

        logging.basicConfig(level=logging.DEBUG if verbose else logging.INFO)

    def download_model(self):
        logging.info("Downloading model from KaggleHub...")
        path = kagglehub.model_download(self.model_repo)
        model_file_path = os.path.join(path, self.model_name)

        total_size = os.path.getsize(model_file_path)
        chunk_size = 1024  # 1KB

        progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc="Downloading", leave=False)

        with open(model_file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(chunk_size), b''):
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
            }
        )

    def execute(self):
        self.download_model()
        self.load_point_cloud()
        image_files = os.listdir(self.image_dir)
        random_images = random.sample(image_files, self.num_images)

        with tqdm(total=self.num_images, desc="Processing Images", unit="image", leave=False) as pbar:
            for i, img_file in enumerate(random_images):
                img_path = os.path.join(self.image_dir, img_file)
                img_array = preprocess_image(img_path)
                res = self.run_inference(img_array)
                self.plot_results(res, i)
                pbar.set_postfix(file=img_file)
                pbar.update(1)

        logging.info("All images processed successfully.")
