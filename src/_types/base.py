from pydantic import BaseModel


class BaseModifier(BaseModel):
    """
    Base model for modifier.

    start: Start position in the audio in samples.
    stop: Stop position in the audio in samples.
    """

    start: int
    stop: int


class File(BaseModel):
    """
    Base model for instruction file.

    sample_rate: Sample rate of the audio file.
    fragments: List of audio fragments.
    """

    sample_rate: int
    fragments: list[BaseModifier]
