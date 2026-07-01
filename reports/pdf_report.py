from io import BytesIO
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    ListFlowable,
    ListItem
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import HexColor

styles = getSampleStyleSheet()

title_style = styles["Heading1"]
title_style.alignment = TA_CENTER
title_style.textColor = HexColor("#0066CC")

heading_style = styles["Heading2"]
normal_style = styles["BodyText"]


def generate_pdf(resume_json, job_json, report, summary):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    story = []

    story.append(
        Paragraph(
            "AI Resume Screening Report",
            title_style
        )
    )

    story.append(Spacer(1, 20))

    # Candidate

    story.append(
        Paragraph("Candidate Information", heading_style)
    )

    story.append(
        Paragraph(
            f"<b>Name:</b> {resume_json.get('name')}",
            normal_style
        )
    )

    story.append(
        Paragraph(
            f"<b>Email:</b> {resume_json.get('email')}",
            normal_style
        )
    )

    story.append(
        Paragraph(
            f"<b>Phone:</b> {resume_json.get('phone')}",
            normal_style
        )
    )

    story.append(Spacer(1, 15))

    # Job

    story.append(
        Paragraph("Job", heading_style)
    )

    story.append(
        Paragraph(
            f"<b>Title:</b> {job_json.get('job_title')}",
            normal_style
        )
    )

    story.append(Spacer(1, 15))

    # Score

    story.append(
        Paragraph("ATS Score", heading_style)
    )

    story.append(
        Paragraph(
            f"{report['ats_score']}%",
            normal_style
        )
    )

    story.append(Spacer(1, 15))

    # Summary

    story.append(
        Paragraph("Resume Summary", heading_style)
    )

    story.append(
        Paragraph(summary, normal_style)
    )

    story.append(Spacer(1, 15))

    # Matched

    story.append(
        Paragraph("Matched Skills", heading_style)
    )

    story.append(

        ListFlowable(

            [
                ListItem(
                    Paragraph(skill, normal_style)
                )
                for skill in report["matched_skills"]
            ]

        )

    )

    story.append(Spacer(1, 15))

    # Missing

    story.append(
        Paragraph("Missing Skills", heading_style)
    )

    story.append(

        ListFlowable(

            [
                ListItem(
                    Paragraph(skill, normal_style)
                )
                for skill in report["missing_skills"]
            ]

        )

    )

    story.append(Spacer(1, 15))

    # Recommendation

    story.append(
        Paragraph("Recommendation", heading_style)
    )

    story.append(
        Paragraph(
            report["recommendation"],
            normal_style
        )
    )

    doc.build(story)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf