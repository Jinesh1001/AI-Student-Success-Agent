import streamlit as st
import pandas as pd
import plotly.express as px

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

    st.title("📊 Career Analysis")

    name = st.text_input("Your Name")

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

    if st.button("Analyze My Career"):

        st.success(f"Welcome {name}")

        if interest == "AI/ML":

            st.subheader("🎯 Career Recommendation")
            st.write("AI Engineer")

            st.subheader("📚 Skills To Learn")
            st.write("Python")
            st.write("SQL")
            st.write("Statistics")
            st.write("Machine Learning")
            st.write("GitHub")

            st.subheader("🛠 Recommended Projects")
            st.write("AI Chatbot")
            st.write("Resume Analyzer")
            st.write("Student Success Agent")
            st.write("Interview Preparation Agent")

            st.progress(25)

        elif interest == "Data Science":

            st.subheader("🎯 Career Recommendation")
            st.write("Data Scientist")

            st.write("Python")
            st.write("Pandas")
            st.write("NumPy")
            st.write("Statistics")
            st.write("SQL")

            st.progress(20)

        elif interest == "Cyber Security":

            st.subheader("🎯 Career Recommendation")
            st.write("Cyber Security Analyst")

            st.write("Networking")
            st.write("Linux")
            st.write("Ethical Hacking")
            st.write("Python")

            st.progress(15)

        elif interest == "Cloud Computing":

            st.subheader("🎯 Career Recommendation")
            st.write("Cloud Engineer")

            st.write("AWS")
            st.write("Azure")
            st.write("Docker")
            st.write("Kubernetes")

            st.progress(15)

        elif interest == "Full Stack Development":

            st.subheader("🎯 Career Recommendation")
            st.write("Full Stack Developer")

            st.write("HTML")
            st.write("CSS")
            st.write("JavaScript")
            st.write("React")

            st.progress(15)

        elif interest == "DevOps":

            st.subheader("🎯 Career Recommendation")
            st.write("DevOps Engineer")

            st.write("Linux")
            st.write("Docker")
            st.write("Kubernetes")
            st.write("CI/CD")

            st.progress(10)

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
        type=["pdf", "docx"]
    )

    if uploaded_file:

        st.success("Resume uploaded successfully!")

        st.subheader("📋 Resume Suggestions")

        st.write("✅ Add GitHub Profile")
        st.write("✅ Add LinkedIn Profile")
        st.write("✅ Add Projects Section")
        st.write("✅ Add Technical Skills")
        st.write("✅ Add Certifications")

        st.metric("Resume Score", "75/100")

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