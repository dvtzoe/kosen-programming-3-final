import numpy as np

from src._global import g


def amplitude(
    start: int,
    stop: int,
    amplitude: np.float32,
) -> None:
    if g.verbose:
        print(f"Applying amplitude: {amplitude} from {start} to {stop}")
    g.data = g.data[start:stop] + amplitude
