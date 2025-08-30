import numpy as np

from src._global import g


def sine(
    start: int,
    stop: int,
    freq: np.float32,
    phase: np.float32,
    amplitude: np.float32,
) -> None:
    if g.verbose:
        print(f"Generating sine wave: {freq}Hz from {start} to {stop}")
    x = np.linspace(start, stop, endpoint=False)
    sine_multiplier = amplitude * np.sin(2 * np.pi * freq * (x + phase))
    g.data = g.data[start:stop] * sine_multiplier
