from pydantic import BaseModel, Field


class ConfigsModel(BaseModel):
    n_books: int = Field(5, ge=0)
