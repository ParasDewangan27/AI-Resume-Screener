"""
prompts.py

Contains all prompts used by the AI Resume Screening System.
"""

# ----------------------------------------------------------
# Resume Parsing Prompt
# ----------------------------------------------------------

RESUME_PROMPT = """
You are an expert ATS Resume Parser.

Your task is to extract structured information from the resume.

Return ONLY valid JSON.

Do NOT use markdown.
Do NOT explain anything.
Do NOT add extra text.

If a field is missing, return null.

Return exactly this schema:

{
    "name": "",
    "email": "",
    "phone": "",
    "linkedin": "",
    "github": "",

    "skills": [],

    "education": [
        {
            "degree": "",
            "college": "",
            "year": ""
        }
    ],

    "experience": [
        {
            "company": "",
            "role": "",
            "duration": ""
        }
    ],

    "projects": [],

    "certifications": [],

    "languages": []
}
"""

# ----------------------------------------------------------
# Job Description Parsing Prompt
# ----------------------------------------------------------

JOB_DESCRIPTION_PROMPT = """
You are an expert HR Recruiter.

Extract structured information from the Job Description.

Return ONLY valid JSON.

Never use markdown.

Never explain anything.

If data is missing, return null.

Schema:

{
    "job_title": "",

    "required_skills": [],

    "preferred_skills": [],

    "education": "",

    "experience": "",

    "responsibilities": []
}
"""

# ----------------------------------------------------------
# Resume Summary Prompt
# ----------------------------------------------------------

SUMMARY_PROMPT = """
Summarize this resume in less than 120 words.

Focus on:

• Skills

• Experience

• Projects

• Education

Return plain text only.
"""

# ----------------------------------------------------------
# Recommendation Prompt
# ----------------------------------------------------------

RECOMMENDATION_PROMPT = """
You are a senior HR recruiter.

Based on the ATS score and missing skills,

recommend ONE of these:

Highly Recommended

Recommended

Consider

Not Recommended

Give a short reason in less than 40 words.

Return plain text only.
"""