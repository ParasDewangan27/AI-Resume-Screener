"""
gemini_api.py

Handles all communication with Google Gemini.
"""

import json
from google import genai
from config import GEMINI_API_KEY
from prompts import (
    RESUME_PROMPT,
    JOB_DESCRIPTION_PROMPT,
    SUMMARY_PROMPT,
    RECOMMENDATION_PROMPT,
)

# ------------------------------------------
# Initialize Gemini Client
# ------------------------------------------

client = genai.Client(api_key=GEMINI_API_KEY)


# ------------------------------------------
# Internal Helper
# ------------------------------------------

import time
from google.genai import errors


def _generate(prompt: str):

    retries = 3

    for attempt in range(retries):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )

            return response.text.strip()

        except Exception as e:

            if attempt == retries - 1:
                raise e

            time.sleep(2)

# ------------------------------------------
# Safe JSON Parser
# ------------------------------------------

def _parse_json(text: str):
    """
    Removes markdown code fences if Gemini returns them.
    """

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    return json.loads(text)


# ------------------------------------------
# Resume Extraction
# ------------------------------------------

def extract_resume_data(resume_text):
    """
    Returns structured resume JSON.
    """

    prompt = f"""
{RESUME_PROMPT}

Resume:

{resume_text}
"""

    result = _generate(prompt)

    return _parse_json(result)


# ------------------------------------------
# Job Description Extraction
# ------------------------------------------

def extract_job_data(job_text):
    """
    Returns structured Job Description JSON.
    """

    prompt = f"""
{JOB_DESCRIPTION_PROMPT}

Job Description:

{job_text}
"""

    result = _generate(prompt)

    return _parse_json(result)


# ------------------------------------------
# Resume Summary
# ------------------------------------------

def summarize_resume(resume_text):

    prompt = f"""
{SUMMARY_PROMPT}

Resume:

{resume_text}
"""

    return _generate(prompt)


# ------------------------------------------
# Recommendation
# ------------------------------------------

def get_recommendation(score, missing_skills):

    prompt = f"""
{RECOMMENDATION_PROMPT}

ATS Score:

{score}

Missing Skills:

{missing_skills}
"""

    return _generate(prompt)