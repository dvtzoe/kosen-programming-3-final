import numpy as np

from src._types.base import Modifier


class Amplitude(Modifier):
    """
    Model for a flat line audio fragment.

    amplitufe: Amplitude of the flat line.
    """

    amplitufe: np.float32


class Sine(Modifier):
    """
    Model for a sine wave audio fragment.

    frequency: Frequency of the sine wave in Hz.
    amplitude: Amplitude of the sine wave.
    offset: Vertical offset of the sine wave.
    """

    frequency: np.float32
    amplitude: np.float32
    phase: np.float32 = np.float32(0.0)
