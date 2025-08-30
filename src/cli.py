import argparse

from src._types.args import ArgsModel
from src.main import main as main_function


def main():
    parser = argparse.ArgumentParser(
        prog="final_cli", description="KOSEN Programming-3's final project CLI"
    )
    _ = parser.add_argument(
        "filename",
        type=str,
        help="Input file name",
    )
    _ = parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Output file name",
        default="output.wav",
    )
    _ = parser.add_argument(
        "-f",
        "--format",
        type=str,
        help="Output file format",
        choices=["wav", "mp3", "flac"],
    )
    _ = parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose output",
    )
    args = parser.parse_args()

    args = ArgsModel(
        filename=args.filename,  # pyright: ignore[reportAny]
        output=args.output,  # pyright: ignore[reportAny]
        format=args.format,  # pyright: ignore[reportAny]
        verbose=args.verbose,  # pyright: ignore[reportAny]
    )

    main_function(args)
