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
    --format       Output format (png or html).
    --help         Display this help message.

Config File Example:
{
    "model_repo": "dummieape/poselstm_cs_cmu_indoor/onnx/csb_1f",
    "model_name": "model_100_epoch.onnx",
    "ply_file": "data/pointclouds/csb_1f_low_binary.ply",
    "image_dir": "seq01",
    "output_dir": "dist",
    "num_images": 10,
    "format": "html"
}
"""

import os
import argparse
import json
import logging

from ._PointCloudPoseEstimation import PointCloudPoseEstimation


def parse_args():
    parser = argparse.ArgumentParser(
        description="Run PointCloud Pose Estimation",
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
""",
    )
    parser.add_argument("--model_repo", type=str, help="Path to the model repository.")
    parser.add_argument("--model_name", type=str, help="Name of the model to download from KaggleHub.")
    parser.add_argument("--ply_file", type=str, help="Path to the PLY file containing the point cloud.")
    parser.add_argument("--image_dir", type=str, help="Directory containing images to process.")
    parser.add_argument("--output_dir", type=str, help="Directory to save output images.")
    parser.add_argument("--num_images", type=int, help="Number of images to process.")
    parser.add_argument("--config", type=str, help="Path to the JSON configuration file.")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging.")
    parser.add_argument("--run", action="store_true", help="Run the script with default arguments.")
    parser.add_argument("--format", type=str, choices=["png", "html"], help="Output format (png or html).")
    return parser.parse_args()


def load_config(config_file, override_args=None):
    with open(config_file, "r") as f:
        config = json.load(f)
    if override_args:
        config.update({key: value for key, value in override_args.items() if value is not None})
    return config


def setup_logging(verbose):
    logging_level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=logging_level, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.debug("Verbose logging enabled.")


def validate_config(config):
    required_args = ["model_repo", "model_name", "ply_file", "image_dir", "output_dir"]
    missing_args = [key for key in required_args if not config.get(key)]
    if missing_args:
        raise ValueError(f"Missing required arguments: {missing_args}")


def create_output_dir(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


def main():
    args = parse_args()

    override_args = vars(args)
    config = {}

    if args.run:
        config.update({"output_dir": "dist", "num_images": 1})
        args.config = "config.json"

    if args.config:
        config.update(load_config(args.config, override_args))
    else:
        config.update(override_args)

    setup_logging(args.verbose)
    validate_config(config)
    create_output_dir(config.get("output_dir"))

    logging.info("Starting PointCloud Pose Estimation task...")
    logging.info(f"Configuration: {json.dumps(config, indent=2)}")

    task = PointCloudPoseEstimation(
        model_repo=config["model_repo"],
        model_name=config["model_name"],
        ply_file=config["ply_file"],
        image_dir=config["image_dir"],
        output_dir=config["output_dir"],
        num_images=config["num_images"],
        out_format=config.get("format"),
        verbose=args.verbose,
    )
    task.execute()

    logging.info("PointCloud Pose Estimation task completed successfully.")


if __name__ == "__main__":
    main()
