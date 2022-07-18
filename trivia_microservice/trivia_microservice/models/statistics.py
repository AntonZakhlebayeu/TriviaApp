from typing import Optional

from pydantic import BaseModel


class StatisticsModel(BaseModel):
    amount_of_answers: int = 0
    amount_of_correct_answers: int = 0

    class Config:
        schema_extra = {
            "example": {
                "amount_of_answers": 15,
                "amount_of_correct_answers": 5,
            }
        }


class UpdateStatisticsModel(BaseModel):
    id: int
    amount_of_answers: Optional[int]
    amount_of_corrected_answers: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "id": 25,
                "amount_of_answers": 15,
                "amount_of_corrected_answers": 5,
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
