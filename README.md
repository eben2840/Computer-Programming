
Study Plan Generator Python3 Backend & Flutter Frontend - Project Report

<!-- Project Overview --> 
<video width="560" height="315" controls>
  <source src="assets/demo.mp4" type="video/mp4">
  Your browser does not support the video tag. You can <a href="assets/demo.mp4">download the video here</a>.
</video>

Steps to fun this project:
-make sure to you have python3 > installed on your PC with 'python --version'
-Run pip install -r requirements.txt to get all the depencies 
-source into the environment file using "source venv/bin/activate"
-then lastly run python3 main.py
-The API will be available at `http://localhost:8000`
-Now get the study endpoint at `http://localhost:8000/plan`


The Study Plan Generator is a backend service built with FastAPI that leverages Google Gemini to create personalized study plans for programming languages. The system allows users to input their preferred programming languages, available study days, duration in months, and preferred study time, then generates comprehensive, structured learning plans tailored to their schedule and goals.

The project serves as the backend API for a Flutter mobile application, providing RESTful endpoints for study plan generation while ensuring cross-origin compatibility through CORS middleware.

Architecture and Implementation

Technology Stack
- Framework: FastAPI (Python web framework for building APIs)
- Integration: Google Generative (Gemini 1.5-flash model)
- Data Validation: Pydantic (for request/response models)
- Server: Uvicorn 
- Environment Management: python-dotenv (for API key handling)
- Frontend Compatibility: CORS middleware for Flutter app integration


Key Components

1. Main Application (main.py)
- FastAPI application initialization with metadata
- CORS configuration for cross-origin  for the flutter calls
- Health check endpoint (`/`)
- Study plan generation endpoint (`/plan`)
- I created an input validation and error handling

2. Data Models (schemas.py)
- UserRequest: Validates incoming study plan requests
- PlanResponse: Structures API responses with status, message, and content
- Includes JSON schema examples for API documentation

3. Service (gemini.py)
- Gemini configuration and API key management
- Dynamic prompt construction based on user inputs
- Structured prompt template for consistent, plan generation
- Error handling for service failures

Key Implementation Details

API Design
The API follows RESTful principles with a single primary endpoint:
- `POST /plan`: Accepts JSON payload with user preferences and returns generated study plan

Input Validation
- Programming languages: Non-empty list of strings
- Available days: Non-empty list of day names
- Duration: Integer between 1-24 months
- Study time: HH:MM format (24-hour) with regex validation

Prompt Engineering
The system constructs detailed prompts that include:
- User-specified parameters (languages, days, duration, time)
- Structured output requirements (monthly breakdown, weekly schedule, projects)
- Specific formatting for schedule data extraction
- Time management and learning pace considerations

Error Handling
- HTTP exceptions for invalid inputs (400 status)
- Internal server errors (500 status) with logging
- service failure handling with user-friendly messages

Challenges Faced

1. Response Consistency
- Challenge: Ensuring Gemini generates consistently formatted, actionable study plans
- Solution: Implemented detailed prompt templates with specific formatting requirements and section headers

2. Input Validation Complexity
- Challenge: Validating diverse user inputs (time formats, day names, duration ranges)
- Solution: I added conditional checks

3. API Key Security
- Challenge: Securely managing Google Gemini API keys in development and production
- Solution: Environment variable configuration with python-dotenv, avoiding hardcoded credentials

4. CORS Configuration
- Challenge: Enabling cross-origin requests from Flutter mobile app
- Solution: I had to Configured CORS middleware with permissive settings for development (to be restricted in production)


Conclusion

The Study Plan Generator backend successfully demonstrates the integration of modern capabilities with robust API design. The implementation provides an easy and nice foundation for personalized learning planner, with strong emphasis on input validation, error handling, and user experience.

Key achievements include:
- API integration with Google Gemini
- Comprehensive input validation and error handling
- Structured, study plan.
- CORS-enabled API for mobile application integration

Future enhancements could include:
- User progress tracking and plan adjustments
- Integration with learning platforms and resources
- Advanced personalization based on user skill levels
- Multi-language support for international users

The project showcases effective use of Python3 for building performant APIs.

