"""
AI Resume Screening & Skill Matching System
Main Streamlit Application
"""

import streamlit as st

from ui.profile_card import profile_card
from ui.score_card import score_card
from ui.skills_card import skills_card
from ui.summary_card import summary_card
from ui.stats_cards import stats_cards

from charts.gauge_chart import gauge_chart
from charts.skills_chart import skills_chart

from parser.resume_parser import ResumeParser
from parser.job_parser import JobParser

from reports.pdf_report import generate_pdf
from reports.json_report import generate_json

from gemini_api import (
    extract_resume_data,
    extract_job_data,
    summarize_resume
)

from services.ats_engine import ATSEngine

from services.ai_career_coach import generate_career_coach
from ui.career_coach import career_coach_card


# ---------------------------------------------------------
# Streamlit Config
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

st.title("🤖 AI Resume Screening & Skill Matching System")

st.markdown("---")


# ---------------------------------------------------------
# Upload Section
# ---------------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader(
        "Upload Resume",
        type=["pdf"]
    )

with col2:
    job_file = st.file_uploader(
        "Upload Job Description",
        type=["pdf", "docx", "txt"]
    )


st.markdown("---")


# ---------------------------------------------------------
# Analyze Button
# ---------------------------------------------------------

if st.button("🚀 Analyze Resume", use_container_width=True):

    if resume_file is None or job_file is None:
        st.error("Please upload both Resume and Job Description.")
        st.stop()

    with st.spinner("Analyzing Resume..."):

        # -------------------------------------------------
        # Parse Resume
        # -------------------------------------------------

        resume_parser = ResumeParser(resume_file)

        resume_text = resume_parser.extract_text()

        resume_json = extract_resume_data(resume_text)

        summary = summarize_resume(resume_text)

        # -------------------------------------------------
        # Parse Job Description
        # -------------------------------------------------

        job_parser = JobParser(job_file)

        job_text = job_parser.extract_text()

        job_json = extract_job_data(job_text)

        # -------------------------------------------------
        # ATS
        # -------------------------------------------------

        engine = ATSEngine(
            resume_json,
            job_json
        )

        report = engine.generate_report()

    st.success("Analysis Complete!")
    stats_cards(report)

    st.markdown("---")

    # =====================================================
    # Candidate Details
    # =====================================================

    profile_card(resume_json)

    st.markdown("---")

    # =====================================================
    # Resume Summary
    # =====================================================

    summary_card(summary)

    st.markdown("---")

    # =====================================================
    # ATS Score
    # =====================================================

    score_card(report["ats_score"])
    gauge_chart(
        report["ats_score"]
    )

    st.markdown("---")

    # =====================================================
    # Skills
    # =====================================================

    skills_card(
        report["matched_skills"],
        report["missing_skills"]
    )
    skills_chart(
        report["matched_skills"],
        report["missing_skills"]
    )

    st.markdown("---")

    # =====================================================
    # Recommendation
    # =====================================================

    st.header("💼 Recommendation")

    st.success(
        report["recommendation"]
    )

    st.markdown("---")

# =====================================================
# AI Career Coach
# =====================================================

    with st.spinner("Generating AI Career Coach..."):

        coach_data = generate_career_coach(
            resume_text,
            job_text
        )

    st.markdown("---")

    career_coach_card(coach_data)

    st.markdown("---")


    st.header("📥 Export Report")

    pdf_data = generate_pdf(
        resume_json,
        job_json,
        report,
        summary
    )

    json_data = generate_json(report)

    col1, col2 = st.columns(2)

    with col1:

        st.download_button(
            "📄 Download PDF Report",
            pdf_data,
            file_name="ATS_Report.pdf",
            mime="application/pdf",
            use_container_width=True
        )

    with col2:

        st.download_button(
            "📥 Download JSON Report",
            json_data,
            file_name="ATS_Report.json",
            mime="application/json",
            use_container_width=True
        )
    # =====================================================
    # Raw JSON (Expandable)
    # =====================================================

    with st.expander("Resume JSON"):

        st.json(resume_json)

    with st.expander("Job Description JSON"):

        st.json(job_json)

    with st.expander("ATS Report"):

        st.json(report)