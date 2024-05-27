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

    python3 -m apeboiy.inav_predict -r

Short argument usage:
    python3 -m apeboiy.inav_predict \\
        -mr "kagglehub://username/repo" \\
        -mn "model.onnx" \\
        -pf "data/pointclouds/csb_1f_low_binary.ply" \\
        -id "seq01" \\
        -od "dist" \\
        -ni 1

    python3 -m apeboiy.inav_predict -r
""",
    )
    parser.add_argument("-mr", "--model_repo", type=str, help="Path to the model repository.")
    parser.add_argument("-mn", "--model_name", type=str, help="Name of the model to download from KaggleHub.")
    parser.add_argument("-pf", "--ply_file", type=str, help="Path to the PLY file containing the point cloud.")
    parser.add_argument("-id", "--image_dir", type=str, help="Directory containing images to process.")
    parser.add_argument("-od", "--output_dir", type=str, help="Directory to save output images.")
    parser.add_argument("-ni", "--num_images", type=int, help="Number of images to process.")
    parser.add_argument("-c", "--config", type=str, help="Path to the JSON configuration file.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging.")
    parser.add_argument("-q", "--quiet", action="store_false", dest="verbose", help="Disable verbose logging.")
    parser.add_argument("-r", "--run", action="store_true", help="Run the script with default arguments.")
    parser.add_argument("-f", "--format", type=str, choices=["png", "html"], help="Output format (png or html).")

    parser.set_defaults(verbose=False)
    parser.set_defaults(run=False)
    parser.set_defaults(format="png")

    parser.add_argument("-s", "--setup", action="store_true", help="Create tasks and pipelines.")
    parser.add_argument("-l", "--load", action="store_true", help="Download the model from KaggleHub.")
    return parser.parse_args()


def load_config(config_file, override_args=None):
    with open(config_file, "r") as f:
        config = json.load(f)
    if override_args:
        config.update({key: value for key, value in override_args.items() if value is not None})
    return config


def setup_logging(verbose, debug=False):
    logging_level = logging.DEBUG if verbose and debug else logging.INFO
    logging.basicConfig(level=logging_level, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.debug("Verbose logging enabled.")


def validate_config(config):
    required_args = ["model_repo", "model_name", "ply_file", "image_dir", "output_dir"]
    missing_args = [key for key in required_args if not config.get(key)]
    if missing_args:
        if os.path.exists(config.get("config")):
            raise FileNotFoundError(f"Configuration file not found: {config.get('config')}")
        raise ValueError(f"Missing required arguments: {missing_args}")


def create_output_dir(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


def setup(args):
    """
    Load the configuration file and create tasks.lock file
    """
    validate_config(args)

    create_output_dir(args.get("output_dir"))

    # recreate the tasks-lock.json file if it exists
    if os.path.exists("tasks-lock.json"):
        os.remove("tasks-lock.json")

    with open("tasks-lock.json", "w") as f:
        f.write(json.dumps(args, indent=2))

    logging.info("Setup was successful.")


def main():
    args = parse_args()

    override_args = vars(args)
    config = {}

    setup_logging(args.verbose, not args.quiet)

    if args.setup:
        config = {
            "output_dir": "dist",
            "num_images": 1,
            "format": "png",
            "config": "config.json"
        }
        if args.config:
            config.update(load_config(args.config, override_args))
        else:
            if not os.path.exists(config.get("config")):
                raise FileNotFoundError(f"Configuration file not found: {config.get('config')}")
            config.update(load_config(config.get("config"), override_args))
        logging.info("Starting setup...")
        logging.info(f"Configuration: {json.dumps(config, indent=2)}")

        res = input("Do you want to proceed with the setup? (y/n): ")
        if res.lower() == "y":
            setup(config)
        return

    if os.path.exists("tasks-lock.json"):
        with open("tasks-lock.json", "r") as f:
            config = json.load(f)

        if override_args:
            config.update({key: value for key, value in override_args.items() if value is not None})
        if args.verbose:
            logging.info("Configuration loaded from tasks-lock.json file.")
            logging.info(f"Configuration: {json.dumps(config, indent=2)}")

    logging.info("Starting PointCloud Pose Estimation task...")
    if args.verbose:
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
    if args.load:
        task.download_model()

    if args.run:
        if args.verbose:
            logging.info("Running PointCloud Pose Estimation task...")
            logging.info(f"Configuration: {json.dumps(config, indent=2)}")
        task.execute()
        logging.info("PointCloud Pose Estimation task completed successfully.")


if __name__ == "__main__":
    main()
