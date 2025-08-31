import numpy as np

from src._types.base import BaseModifier


class Amplitude(BaseModifier):
    """
    Model for a flat line modifier.

    amplitufe: Amplitude of the flat line.
    """

    amplitufe: np.float32


class Sine(BaseModifier):
    """
    Model for a sine wave modifier.

    frequency: Frequency of the sine wave in Hz.
    amplitude: Amplitude of the sine wave.
    offset: Vertical offset of the sine wave.
    """

    frequency: np.float32
    amplitude: np.float32
    phase: np.float32 = np.float32(0.0)


type AnyModifier = Amplitude | Sine
