import io
import streamlit as st
import pandas as pd
import plotly.express as px
from pypdf import PdfReader

st.set_page_config(
    page_title="AI Student Success Agent",
    page_icon="🎓",
    layout="wide"
)

# ======================
# SIDEBAR
# ======================

st.sidebar.title("🎓 AI Student Success Agent")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Career Analysis",
        "Internship Score",
        "Roadmap",
        "Resume Analyzer",
        "Project Recommender",
        "About Project"
    ]
)

# ======================
# DASHBOARD
# ======================

if page == "Dashboard":

    st.title("🎓 AI Student Success Agent")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("Skills", "1")

    with col2:
        st.metric("Projects", "3")

    with col3:
        st.metric("Readiness", "25%")

    with col4:
        st.metric("Certificates", "2")

    with col5:
        st.metric("Internships", "0")

    st.subheader("👋 Welcome")

    st.info("""
Student Success Agent helps students:

• Discover career paths

• Find skill gaps

• Track internship readiness

• Build learning roadmaps

• Get project recommendations
""")

    st.subheader("👨‍🎓 Student Profile")

    student_name = st.text_input("Name")

    year = st.selectbox(
        "Current Year",
        ["1st Year", "2nd Year", "3rd Year", "4th Year"]
    )

    branch = st.selectbox(
        "Branch",
        ["ICT", "CSE", "IT", "ECE", "Mechanical", "Civil"]
    )

    cgpa = st.slider(
        "CGPA",
        0.0,
        10.0,
        8.0
    )

    st.success(
        f"Student: {student_name} | {year} | {branch} | CGPA: {cgpa}"
    )

    st.subheader("🎯 Personalized Recommendations")

    if year == "1st Year":
        st.info("Focus on Python, GitHub, SQL and beginner projects.")

    elif year == "2nd Year":
        st.info("Focus on DSA, GitHub and internship preparation.")

    elif year == "3rd Year":
        st.info("Focus on internships, projects and interview preparation.")

    elif year == "4th Year":
        st.info("Focus on placements, resume building and mock interviews.")

    st.subheader("📈 Career Progress")

    data = pd.DataFrame({
        "Skill": ["Python", "GitHub", "SQL", "Machine Learning"],
        "Progress": [80, 20, 10, 5]
    })

    fig = px.bar(
        data,
        x="Skill",
        y="Progress",
        title="Current Skill Progress"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🚀 Career Readiness Dashboard")

    python_score = 25
    github_score = 10
    sql_score = 5
    ml_score = 0

    total_score = (
        python_score +
        github_score +
        sql_score +
        ml_score
    )

    st.metric(
        "Career Readiness Score",
        f"{total_score}%"
    )

    st.progress(total_score / 100)
    st.markdown("---")
    st.write("Developed by Jinesh Borad")

# ======================
# CAREER ANALYSIS
# ======================
elif page == "Career Analysis":

    st.title("📊 AI Career Analysis")

    name = st.text_input("Your Name")

    year = st.selectbox(
        "Current Year",
        ["1st Year", "2nd Year", "3rd Year", "4th Year"]
    )

    interest = st.selectbox(
        "Interest",
        [
            "AI/ML",
            "Data Science",
            "Cyber Security",
            "Cloud Computing",
            "Full Stack Development",
            "DevOps"
        ]
    )

    skills = st.text_input(
        "Current Skills (comma separated)",
        placeholder="Python, Git, SQL"
    )

    if st.button("Analyze My Career"):

        st.success(f"Welcome {name}")

        skill_list = skills.lower()

        if interest == "AI/ML":

            career = "AI Engineer"

            required_skills = [
                "python",
                "sql",
                "statistics",
                "machine learning",
                "git"
            ]

            projects = [
                "AI Chatbot",
                "Resume Analyzer",
                "Student Success Agent",
                "Interview Preparation Agent"
            ]

        elif interest == "Data Science":

            career = "Data Scientist"

            required_skills = [
                "python",
                "pandas",
                "numpy",
                "statistics",
                "sql"
            ]

            projects = [
                "Sales Prediction",
                "Student Performance Analysis",
                "Data Dashboard",
                "Customer Segmentation"
            ]

        elif interest == "Cyber Security":

            career = "Cyber Security Analyst"

            required_skills = [
                "networking",
                "linux",
                "ethical hacking",
                "python"
            ]

            projects = [
                "Port Scanner",
                "Password Strength Checker",
                "Network Monitoring Tool",
                "Vulnerability Scanner"
            ]

        elif interest == "Cloud Computing":

            career = "Cloud Engineer"

            required_skills = [
                "aws",
                "azure",
                "docker",
                "kubernetes"
            ]

            projects = [
                "Cloud Storage System",
                "Docker Deployment",
                "AWS Web App",
                "Cloud Monitoring Dashboard"
            ]

        elif interest == "Full Stack Development":

            career = "Full Stack Developer"

            required_skills = [
                "html",
                "css",
                "javascript",
                "react"
            ]

            projects = [
                "E-Commerce Website",
                "Blog Platform",
                "Portfolio Website",
                "Student Management System"
            ]

        else:

            career = "DevOps Engineer"

            required_skills = [
                "linux",
                "docker",
                "kubernetes",
                "ci/cd"
            ]

            projects = [
                "CI/CD Pipeline",
                "Dockerized Web App",
                "Kubernetes Deployment",
                "Monitoring Dashboard"
            ]

        st.subheader("🎯 Career Recommendation")
        st.success(career)

        missing_skills = []

        for skill in required_skills:
            if skill not in skill_list:
                missing_skills.append(skill.title())

        st.subheader("📈 Skill Gap Analysis")

        if len(missing_skills) == 0:
            st.success("Excellent! You already have all required skills.")
        else:
            for skill in missing_skills:
                st.write("❌", skill)

        st.subheader("🗺 Learning Roadmap")

        st.write("Month 1: Learn Fundamentals")
        st.write("Month 2: Build Small Projects")
        st.write("Month 3: Learn Advanced Concepts")
        st.write("Month 4: Build Portfolio Projects")
        st.write("Month 5: Internship Preparation")
        st.write("Month 6: Apply for Opportunities")

        st.subheader("🚀 Recommended Projects")

        for project in projects:
            st.write("✅", project)

        readiness = max(0, 100 - len(missing_skills) * 20)

        st.subheader("📊 Career Readiness Score")

        st.progress(readiness / 100)

        st.metric("Readiness", f"{readiness}%")

        if readiness >= 80:
            st.success("You are internship ready!")
        elif readiness >= 50:
            st.warning("You are on the right track. Learn a few more skills.")
        else:
            st.error("Focus on learning the missing skills first.")
# ======================
# INTERNSHIP SCORE
# ======================

elif page == "Internship Score":

    st.title("🎯 Internship Readiness Score")

    python_skill = st.checkbox("Python")
    github_skill = st.checkbox("GitHub")
    sql_skill = st.checkbox("SQL")
    ml_skill = st.checkbox("Machine Learning")

    score = (
        int(python_skill)
        + int(github_skill)
        + int(sql_skill)
        + int(ml_skill)
    ) * 25

    st.metric("Readiness Score", f"{score}%")
    st.progress(score / 100)

    if score < 50:
        st.warning("You need more skills.")

    elif score < 100:
        st.info("You are getting internship ready.")

    else:
        st.success("You are internship ready! 🚀")

# ======================
# ROADMAP
# ======================

elif page == "Roadmap":

    st.title("🗺️ AI Engineer Roadmap")

    st.write("Month 1 → Python")
    st.write("Month 2 → Git & GitHub")
    st.write("Month 3 → SQL")
    st.write("Month 4 → Statistics")
    st.write("Month 5 → Machine Learning")
    st.write("Month 6 → Build AI Project")

    st.progress(25)

# ======================
# RESUME ANALYZER
# ======================
elif page == "Resume Analyzer":

    st.title("📄 Resume Analyzer")

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["txt","pdf"]
    )

    if uploaded_file is not None:

        if uploaded_file.name.endswith(".pdf"):

            pdf = PdfReader(uploaded_file)

            content = ""

            for page in pdf.pages:
                content += page.extract_text() or ""

        else:

           content = uploaded_file.read().decode("utf-8")

        st.subheader("Resume Preview")
        st.text(content[:1000])

        score = 0

        keywords = [
            "python",
            "sql",
            "machine learning",
            "project",
            "github",
            "internship"
        ]

        found = []

        for keyword in keywords:

            if keyword.lower() in content.lower():
                score += 15
                found.append(keyword)

        score = min(score, 100)

        st.subheader("Resume Score")

        st.progress(score / 100)

        st.metric("Score", f"{score}%")

        st.subheader("Detected Skills")

        for item in found:
            st.write("✅", item)

        missing = [k for k in keywords if k not in found]

        st.subheader("Suggestions")

        for item in missing:
            st.write("❌ Add:", item)

        if score >= 80:
            st.success("Strong Resume")
        elif score >= 50:
            st.warning("Good Resume, needs improvement")
        else:
            st.error("Resume needs more skills and projects")
# ======================
# PROJECT RECOMMENDER
# ======================

elif page == "Project Recommender":

    st.title("🚀 Project Recommender")

    domain = st.selectbox(
        "Choose Domain",
        [
            "AI/ML",
            "Data Science",
            "Cyber Security",
            "Cloud Computing",
            "Full Stack Development",
            "DevOps"
        ]
    )

    if st.button("Recommend Projects"):

        if domain == "AI/ML":
            st.write("• AI Chatbot")
            st.write("• Resume Analyzer")
            st.write("• Student Success Agent")
            st.write("• Face Recognition System")

        elif domain == "Data Science":
            st.write("• Sales Dashboard")
            st.write("• IPL Data Analysis")
            st.write("• Customer Segmentation")
            st.write("• Placement Analytics")

        elif domain == "Cyber Security":
            st.write("• Password Checker")
            st.write("• Port Scanner")
            st.write("• Network Monitor")
            st.write("• Vulnerability Scanner")

        elif domain == "Cloud Computing":
            st.write("• Cloud Cost Tracker")
            st.write("• AWS Dashboard")
            st.write("• Docker Project")
            st.write("• Kubernetes Dashboard")

        elif domain == "Full Stack Development":
            st.write("• Portfolio Website")
            st.write("• E-Commerce Website")
            st.write("• Job Portal")
            st.write("• Food Delivery App")

        elif domain == "DevOps":
            st.write("• CI/CD Pipeline")
            st.write("• Docker Deployment")
            st.write("• Monitoring Dashboard")
            st.write("• AWS Automation")
# ======================
# ABOUT PROJECT
# ======================
elif page == "About Project":

    st.title("📖 About")

    st.write("""
    AI Student Success Agent helps students:
    - Choose careers
    - Identify skill gaps
    - Track internship readiness
    - Build learning roadmaps
    - Get project recommendations
    """)