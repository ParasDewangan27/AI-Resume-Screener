import json

from gemini_api import _generate


def generate_career_coach(resume_text, job_text):

    prompt = f"""
You are an expert Career Coach and Senior HR Recruiter.

Analyze BOTH the resume and job description.

Return ONLY valid JSON.

Schema:

{{
    "resume_suggestions":[
        "...",
        "...",
        "..."
    ],

    "recommended_certifications":[
        "...",
        "..."
    ],

    "interview_questions":[
        "...",
        "..."
    ],

    "career_roadmap":[
        "...",
        "...",
        "..."
    ]
}}

Resume

{resume_text}

Job Description

{job_text}
"""

    result = _generate(prompt)

    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    try:
        return json.loads(result)

    except json.JSONDecodeError:

        return {
            "resume_suggestions": [
                "Unable to generate suggestions."
            ],
            "recommended_certifications": [],
            "interview_questions": [],
            "career_roadmap": []
        }