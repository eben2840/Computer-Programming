from pydantic import BaseModel
from typing import List


class UserRequest(BaseModel):
    # User request model for study plan generation used in main.py
    languages: List[str]
    available_days: List[str]
    duration_months: int
    study_time: str  # Format: 

    class Config:
        json_schema_extra = {
            "example": {
                "languages": ["Python", "JavaScript"],
                "available_days": ["Monday", "Wednesday", "Friday"],
                "duration_months": 6,
                "study_time": "19:00"
            }
        }


class PlanResponse(BaseModel):
    # Response model for study plan used in main.py
    status: str
    message: str
    plan_content: str

    class Config:
        json_schema_extra = {
            "example": {
                "status": "success",
                "message": "Study plan generated successfully",
                "plan_content": "Your personalized study plan..."
            }
        }