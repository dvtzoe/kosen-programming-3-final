from pydantic import BaseModel


class ArgsModel(BaseModel):
    filename: str
    output: str = "output.wav"
    format: str | None = None
    verbose: bool = False
