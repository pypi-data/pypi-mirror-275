"""
PointCloud Pose Estimation Script

This script performs the PointCloud Pose Estimation task by downloading the model from KaggleHub,
loading the point cloud from a PLY file, running inference on images in a directory, and plotting the results.

Usage:
    python3 -m apeboiy.inav_predict --setup
    python3 -m apeboiy.inav_predict --load
    python3 -m apeboiy.inav_predict --run

Arguments:
    -mr, --model_repo   Path to the model repository on KaggleHub (required if --config is not provided).
    -mn, --model_name   Name of the model to download from KaggleHub (required if --config is not provided).
    -pf, --ply_file     Path to the PLY file containing the point cloud (required if --config is not provided).
    -id, --image_dir    Directory containing images to process (required if --config is not provided).
    -od, --output_dir   Directory to save output images (required if --config is not provided).
    -ni, --num_images   Number of images to process (default is 1).
    -c, --config        Path to the JSON configuration file.
    -r, --run           Run the script with default arguments.
    -v, --verbose       Enable verbose logging.
    -q, --quiet         Disable verbose logging.
    -f, --format        Output format (png or html).
    -s, --setup         Create tasks and pipelines.
    -l, --load          Download the model from KaggleHub.
    --help              Display this help message.

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