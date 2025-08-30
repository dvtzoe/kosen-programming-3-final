import argparse

from src._global import g


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
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose output",
    )
    parsed = parser.parse_args()

    g.filename = parsed.filename  # pyright: ignore[reportAny]
    g.output = parsed.output  # pyright: ignore[reportAny]

    g.verbose = parsed.verbos  # pyright: ignore[reportAny]
