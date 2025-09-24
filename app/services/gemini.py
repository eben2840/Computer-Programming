import os
import google.generativeai as genai
from dotenv import load_dotenv
from typing import List

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def generate_study_plan(languages: List[str], available_days: List[str], duration_months: int, study_time: str) -> str:
    try:
        # Initialize the model usieng gemini-1.5-flash https://ai.google.dev/gemini-api/docs/models#gemini-2.5-flash-lite
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Construct the prompt here
        languages_str = ", ".join(languages)
        days_str = ", ".join(available_days)


        # I created a prompt to clearly state the goals of each action plan, i had to research and find the exact way to prompt it
        prompt = f"""
        Create a detailed, personalized study plan for learning programming languages with the following specifications:

        Programming Languages to Study:{languages_str}
        Available Study Days: {days_str} ({len(available_days)} days per week)
        Study Duration: {duration_months} months
        Preferred Study Time  {study_time} daily

        Please generate a comprehensive study plan that includes:

        1. Overview & Goal : Brief introduction and learning objectives
        2. Monthly Breakdow : Detailed month-by-month curriculum for each language
        3. Weekly Schedul : Specific topics/tasks for each available day at {study_time}
        4. Daily Study Session : Structured 1-2 hour sessions starting at {study_time}
        5. Project Milestone : Practical projects to build at different stages
        6. Resource Recommendation : Books, online courses, documentation, and tools
        7. Assessment Checkpoint : Ways to measure progress and skill development
        8. Time Managemen : Tips for maintaining consistency at the scheduled time
        9. Study Session Structur : How to organize each {study_time} study session effectively

     IMPORTANT - Schedule Format Requirements 
        For scheduling and reminder purposes, include a "SCHEDULE_DATA" section at the end with this exact format:
        
        SCHEDULE_DATA:
        Week 1:
        - Monday {study_time}: [Topic/Task]
        - Wednesday {study_time}: [Topic/Task]
        - Friday {study_time}: [Topic/Task]
        Week 2:
        Continue for first 4 weeks...

     Additional Requirements 
        - Adapt the difficulty progression based on the {duration_months}-month timeline
        - Structure each study session to fit within 1-2 hours starting at {study_time}

        Make the plan detailed, actionable, and motivating. Format it clearly with headers, bullet points, and structured sections.
        """
        
        # Generate the response
        response = model.generate_content(prompt)
        
        return response.text
        
    except Exception as e:
        return f"Error generating plan: {str(e)}."