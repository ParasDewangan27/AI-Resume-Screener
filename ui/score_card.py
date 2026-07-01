import streamlit as st


def score_card(score):

    st.subheader("🎯 ATS Match Score")

    st.progress(score / 100)

    if score >= 90:

        st.success(f"{score}%")

    elif score >= 75:

        st.info(f"{score}%")

    elif score >= 60:

        st.warning(f"{score}%")

    else:

        st.error(f"{score}%")