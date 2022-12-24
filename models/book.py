from pydantic import BaseModel, Field


class BookModel(BaseModel):
    id: int
    title: str = Field(
        title="Title of The Book", min_length=1, max_length=100
    )
    author: str = Field(
        title="Author of The Book", min_length=1, max_length=100
    )
    description: str | None = Field(
        None, title="Description About The Book", max_length=100
    )
    rating: int | None = Field(
        None, title="Rating of The Book", ge=0, le=100)

    class Config:
        schema_extra = {
            "example": {
                "id": 1000,
                "title": "A Sample Book",
                "author": "A Sample Author",
                "description": "A Nice Description",
                "rating": 90
            }
        }


class BookModelNoID(BaseModel):
    title: str = Field(
        title="Title of The Book", min_length=1, max_length=100
    )
    author: str = Field(
        title="Author of The Book", min_length=1, max_length=100
    )
    description: str | None = Field(
        None, title="Description About The Book", max_length=100
    )

    class Config:
        schema_extra = {
            "example": {
                "title": "A Sample Book",
                "author": "A Sample Author",
                "description": "A Nice Description"
            }
        }
