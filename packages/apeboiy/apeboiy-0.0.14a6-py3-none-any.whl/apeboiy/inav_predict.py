"""
PointCloud Pose Estimation Script

This script performs the PointCloud Pose Estimation task by downloading the model from KaggleHub,
loading the point cloud from a PLY file, running inference on images in a directory, and plotting the results.

Usage:
    python3 -m apeboiy.inav_predict --model_repo <MODEL_REPO> --model_name <MODEL_NAME> --ply_file <PLY_FILE> --image_dir <IMAGE_DIR> --output_dir <OUTPUT_DIR> --num_images <NUM_IMAGES>
    python3 -m apeboiy.inav_predict --config <CONFIG_FILE>
    python3 -m apeboiy.inav_predict --run

Arguments:
    --model_repo   Path to the model repository on KaggleHub (required if --config is not provided).
    --model_name   Name of the model to download from KaggleHub (required if --config is not provided).
    --ply_file     Path to the PLY file containing the point cloud (required if --config is not provided).
    --image_dir    Directory containing images to process (required if --config is not provided).
    --output_dir   Directory to save output images (required if --config is not provided).
    --num_images   Number of images to process (default is 1).
    --config       Path to the JSON configuration file.
    --run          Run the script with default arguments.
    --verbose      Enable verbose logging.

Config File Example:
{
    "model_repo": "dummieape/poselstm_cs_cmu_indoor/onnx/csb_1f",
    "model_name": "model_100_epoch.onnx",
    "ply_file": "data/pointclouds/csb_1f_low_binary.ply",
    "image_dir": "seq01",
    "output_dir": "dist",
    "num_images": 10
}
"""

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


def parse_args():
    parser = argparse.ArgumentParser(
        description='Run PointCloud Pose Estimation',
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
Example usage:
    python3 -m apeboiy.inav_predict \\
        --model_repo "kagglehub://username/repo" \\
        --model_name "model.onnx" \\
        --ply_file "data/pointclouds/csb_1f_low_binary.ply" \\
        --image_dir "seq01" \\
        --output_dir "dist" \\
        --num_images 1

    python3 -m apeboiy.inav_predict --run
"""
    )
    parser.add_argument('--model_repo', type=str, help='Path to the model repository.')
    parser.add_argument('--model_name', type=str, help='Name of the model to download from KaggleHub.')
    parser.add_argument('--ply_file', type=str, help='Path to the PLY file containing the point cloud.')
    parser.add_argument('--image_dir', type=str, help='Directory containing images to process.')
    parser.add_argument('--output_dir', type=str, help='Directory to save output images.')
    parser.add_argument('--num_images', type=int, help='Number of images to process.')
    parser.add_argument('--config', type=str, help='Path to the JSON configuration file.')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose logging.')
    parser.add_argument('--run', action='store_true', help='Run the script with default arguments.')
    return parser.parse_args()


def load_config(config_file, override_args=None):
    with open(config_file, 'r') as f:
        config = json.load(f)
    if override_args:
        config.update({
            key: value for key, value in override_args.items() if value is not None
        })
    return config


def main():
    args = parse_args()

    override_args = vars(args)
    config = {}

    if args.run:
        config.update({
            "output_dir": "dist",
            "num_images": 1,
        })
        args.config = "config.json"

    if args.config:
        config.update(load_config(args.config, override_args))
    else:
        config.update(override_args)

    required_args = ["model_repo", "model_name", "ply_file", "image_dir", "output_dir"]
    if not all(config.get(key) for key in required_args):
        not_provided = [key for key in required_args if not config.get(key)]
        raise ValueError(f"Missing required arguments: {not_provided}")

    if args.verbose:
        logging.info(f"""
        ---
        Model Repository: {config.get('model_repo', 'N/A')}
        Model Name: {config.get('model_name', 'N/A')}
        PLY File: {config.get('ply_file', 'N/A')}
        Image Directory: {config.get('image_dir', 'N/A')}
        Output Directory: {config.get('output_dir', 'N/A')}
        Number of Images: {config.get('num_images', 'N/A')}
        
        Config File: {config.get('config', 'N/A')}
        ---
        """)

    task = PointCloudPoseEstimation(
        model_repo=config.get("model_repo"),
        model_name=config.get("model_name"),
        ply_file=config.get("ply_file"),
        image_dir=config.get("image_dir"),
        output_dir=config.get("output_dir"),
        num_images=config.get("num_images"),
        verbose=args.verbose
    )
    task.execute()


if __name__ == "__main__":
    main()
