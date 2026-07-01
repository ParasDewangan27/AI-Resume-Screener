import streamlit as st


def stats_cards(report):

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "🎯 ATS Score",
            f"{report['ats_score']}%"
        )

    with c2:
        st.metric(
            "✅ Matched",
            len(report["matched_skills"])
        )

    with c3:
        st.metric(
            "❌ Missing",
            len(report["missing_skills"])
        )

    with c4:

        total = (
            len(report["matched_skills"])
            + len(report["missing_skills"])
        )

        st.metric(
            "📋 Required",
            total
        )