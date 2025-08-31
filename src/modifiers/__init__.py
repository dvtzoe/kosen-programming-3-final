from src._types.modifiers import *
from src.modifiers import *
from src.modifiers.amplitude import amplitude
from src.modifiers.sine import sine


def process_modifier(modifier: AnyModifier) -> None:
    if isinstance(modifier, Sine):
        sine(
            modifier.start,
            modifier.stop,
            modifier.frequency,
            modifier.phase,
            modifier.amplitude,
        )
    else:  # isinstance(modifier, Amplitude)
        amplitude(
            modifier.start,
            modifier.stop,
            modifier.amplitufe,
        )
