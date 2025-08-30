import json

from scipy.io import wavfile

from src._global import g
from src._types.base import File


def main() -> None:
    if g.verbose:
        print("Verbose mode is enabled")
    with open(g.filename, "r", encoding="utf-8") as file:
        instruction: File = json.load(file)  # pyright: ignore[reportAny]
        g.sample_rate = instruction.sample_rate

    wavfile.write(
        g.output,
        int(instruction.sample_rate),
        g.data,
    )
