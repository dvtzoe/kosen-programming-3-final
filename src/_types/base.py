from pydantic import BaseModel


class Modifier(BaseModel):
    """
    Base model for modifier.

    duration: Duration of the audio in samples.
    position: Current position in the audio in samples.
    """

    duration: int
    position: int


class File(BaseModel):
    """
    Base model for instruction file.

    sample_rate: Sample rate of the audio file.
    data: List of audio fragments.
    """

    sample_rate: int
    fragments: list[Modifier]
