from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.models.schemas import UserRequest, PlanResponse
from app.services.gemini import generate_study_plan
import re

# Language: Python 3
# Object-Oriented Design: Use classes to structure your application logically.
# File Handling: Read from and/or write to files (e.g., JSON, CSV, TXT).
# Exception Handling: Implement robust error handling for file I/O, API calls, and user input.
# API Integration: Use at least one external API to fetch or send data.
# Version Control: Use Git for version control and share your GitHub repository.



# I first of all initialize FastAPI app
# https://ai.google.dev/gemini-api/docs/api-key

app = FastAPI(
    title="Study Plan Generator",
    description="Generate personalized study plans for programming languages using AI",
    version="1.0.0"
)

# I added CORS middleware to allow Flutter app to make requests to my python,
# without it broke so i had to research into how to use this on reddit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
#    Health check endpoint
    return {"message": "Study Plan Generator API is running!"}


@app.post("/plan", response_model=PlanResponse)
def create_study_plan(request: UserRequest):
    # Generate a study plan based on user preferences from the selected options in flutter
    try:
        # Validate input fomr user on flutter frontend
        if not request.languages:
            raise HTTPException(
                status_code=400, 
                detail="At least one programming language must be selected"
            )
        
        if not request.available_days:
            raise HTTPException(
                status_code=400, 
                detail="At least one study day must be selected"
            )
        
        if request.duration_months < 1 or request.duration_months > 24:
            raise HTTPException(
                status_code=400, 
                detail="Duration must be between 1 and 24 months"
            )
        
        # Validate study_time format (HH:MM)
        if not re.match(r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$', request.study_time):
            raise HTTPException(
                status_code=400,
                detail="Study time must be in HH:MM format (24-hour)"
            )
        
        # Generate the study plan using Gemini AI, i used gemeini becuase the documentation is very easy to follow and use
        # https://ai.google.dev/gemini-api/docs/models
        plan_content = generate_study_plan(
            languages=request.languages,
            available_days=request.available_days,
            duration_months=request.duration_months,
            study_time=request.study_time
        )
        
        # Check if plan generation was successful
        if plan_content.startswith("Error generating study plan"):
            return PlanResponse(
                status="error",
                message="Failed to generate study plan. Please check your API configuration.",
                plan_content=""
            )
        
        # response from input
        return PlanResponse(
            status="success",
            message="Study plan generated successfully!",
            plan_content=plan_content
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Server error: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)