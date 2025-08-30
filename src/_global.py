import numpy as np
from pydantic import BaseModel


# Make variables mutable
class Global(BaseModel):
    filename: str = str("")
    output: str = "output.wav"
    verbose: bool = False

    sample_rate: int = 44100

    data: np.ndarray = np.array([], dtype=np.float32)


g = Global()
