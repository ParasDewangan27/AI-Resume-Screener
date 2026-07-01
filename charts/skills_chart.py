import streamlit as st
import plotly.graph_objects as go


def skills_chart(matched, missing):

    # ----------------------------
    # Matched Skills
    # ----------------------------

    if matched:

        matched_fig = go.Figure()

        matched_fig.add_trace(
            go.Bar(
                x=[1] * len(matched),
                y=[skill.title() for skill in matched],
                orientation="h",
                marker=dict(
                    color="#2ECC71"
                ),
                text=["✓"] * len(matched),
                textposition="inside",
                hovertemplate="<b>%{y}</b><extra></extra>"
            )
        )

        matched_fig.update_layout(
            title="✅ Matched Skills",
            height=max(300, len(matched) * 45),
            xaxis=dict(
                visible=False,
                range=[0, 1.2]
            ),
            yaxis=dict(
                autorange="reversed"
            ),
            margin=dict(l=20, r=20, t=50, b=20),
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)"
        )

    # ----------------------------
    # Missing Skills
    # ----------------------------

    if missing:

        missing_fig = go.Figure()

        missing_fig.add_trace(
            go.Bar(
                x=[1] * len(missing),
                y=[skill.title() for skill in missing],
                orientation="h",
                marker=dict(
                    color="#E74C3C"
                ),
                text=["✗"] * len(missing),
                textposition="inside",
                hovertemplate="<b>%{y}</b><extra></extra>"
            )
        )

        missing_fig.update_layout(
            title="❌ Missing Skills",
            height=max(300, len(missing) * 45),
            xaxis=dict(
                visible=False,
                range=[0, 1.2]
            ),
            yaxis=dict(
                autorange="reversed"
            ),
            margin=dict(l=20, r=20, t=50, b=20),
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)"
        )

    # ----------------------------
    # Display
    # ----------------------------

    col1, col2 = st.columns(2)

    with col1:
        if matched:
            st.plotly_chart(
                matched_fig,
                use_container_width=True
            )
        else:
            st.info("No matched skills found.")

    with col2:
        if missing:
            st.plotly_chart(
                missing_fig,
                use_container_width=True
            )
        else:
            st.success("No missing skills 🎉")