"""
ATS Engine

Compares Resume JSON with Job Description JSON
and returns an ATS analysis.
"""

from difflib import SequenceMatcher


class ATSEngine:

    def __init__(self, resume_data, job_data):
        self.resume = resume_data
        self.job = job_data

    # ---------------------------------------------
    # Normalize skills
    # ---------------------------------------------
    def _normalize(self, skills):
        if not skills:
            return []

        normalized = []

        for skill in skills:
            if skill:
                normalized.append(skill.strip().lower())

        return list(set(normalized))

    # ---------------------------------------------
    # Compare two skills
    # ---------------------------------------------
    def _is_match(self, resume_skill, job_skill):

        similarity = SequenceMatcher(
            None,
            resume_skill,
            job_skill
        ).ratio()

        return similarity >= 0.80

    # ---------------------------------------------
    # Match Skills
    # ---------------------------------------------
    def match_skills(self):

        resume_skills = self._normalize(
            self.resume.get("skills", [])
        )

        required_skills = self._normalize(
            self.job.get("required_skills", [])
        )

        matched = []
        missing = []

        for job_skill in required_skills:

            found = False

            for resume_skill in resume_skills:

                # Exact match
                if resume_skill == job_skill:
                    matched.append(job_skill)
                    found = True
                    break

                # Partial match
                if resume_skill in job_skill:
                    matched.append(job_skill)
                    found = True
                    break

                if job_skill in resume_skill:
                    matched.append(job_skill)
                    found = True
                    break

                # Similarity match
                similarity = SequenceMatcher(
                    None,
                    resume_skill,
                    job_skill
                ).ratio()

                if similarity > 0.70:
                    matched.append(job_skill)
                    found = True
                    break

            if not found:
                missing.append(job_skill)

        return matched, missing

    # ---------------------------------------------
    # ATS Score
    # ---------------------------------------------
    def calculate_score(self):

        matched, missing = self.match_skills()

        total = len(matched) + len(missing)

        if total == 0:
            return 0

        return round((len(matched) / total) * 100)

    # ---------------------------------------------
    # Recommendation
    # ---------------------------------------------
    def recommendation(self):

        score = self.calculate_score()

        if score >= 90:
            return "⭐⭐⭐⭐⭐ Highly Recommended"

        elif score >= 75:
            return "⭐⭐⭐⭐ Recommended"

        elif score >= 60:
            return "⭐⭐⭐ Consider"

        return "⭐⭐ Not Recommended"

    # ---------------------------------------------
    # Generate Final Report
    # ---------------------------------------------
    def generate_report(self):

        matched, missing = self.match_skills()

        score = self.calculate_score()

        return {

            "candidate_name":
                self.resume.get("name"),

            "job_title":
                self.job.get("job_title"),

            "ats_score":
                score,

            "matched_skills":
                matched,

            "missing_skills":
                missing,

            "recommendation":
                self.recommendation()
        }