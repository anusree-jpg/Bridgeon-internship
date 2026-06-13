import streamlit as st
import pandas as pd
from datetime import date

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Task Manager",
    page_icon="🗂️",
    layout="wide"
)

# --------------------------------------------------
# PROFESSIONAL UI
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #F5F7FB 0%, #EEF2F7 100%);
}

.main-title {
    text-align: center;
    font-size: 46px;
    font-weight: 700;
    color: #111827;
}

.subtitle {
    text-align: center;
    font-size: 16px;
    color: #6B7280;
    margin-bottom: 25px;
}

.stButton > button {
    background-color: #2563EB;
    color: white;
    border-radius: 8px;
    font-weight: 600;
    height: 42px;
    border: none;
}

.stButton > button:hover {
    background-color: #1D4ED8;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "Register"

if "users" not in st.session_state:
    st.session_state.users = {}

if "user" not in st.session_state:
    st.session_state.user = ""

if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "next_id" not in st.session_state:
    st.session_state.next_id = 1

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("<div class='main-title'>🗂️ Task Manager</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Manage tasks and track deadlines</div>", unsafe_allow_html=True)

# --------------------------------------------------
# REGISTER
# --------------------------------------------------

def register():

    st.subheader("Registration")

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):

        if not username or not email or not password:
            st.error("All fields required")
            return

        st.session_state.users[email] = {
            "username": username,
            "password": password
        }

        st.success("Account created")

        st.session_state.page = "Login"
        st.rerun()

# --------------------------------------------------
# LOGIN
# --------------------------------------------------

def login():

    st.subheader("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if email in st.session_state.users and st.session_state.users[email]["password"] == password:

            st.session_state.logged_in = True
            st.session_state.user = st.session_state.users[email]["username"]

            st.rerun()

        else:
            st.error("Invalid credentials")

# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------

def dashboard():

    st.subheader(f"Welcome {st.session_state.user}")

    # ---------------- TASK SUMMARY ----------------

    total_tasks = len(st.session_state.tasks)

    completed_tasks = sum(
        1 for task in st.session_state.tasks
        if task["completed"]
    )

    pending_tasks = total_tasks - completed_tasks

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📋 Total Tasks", total_tasks)

    with col2:
        st.metric("✅ Completed Tasks", completed_tasks)

    with col3:
        st.metric("⏳ Pending Tasks", pending_tasks)

    st.markdown("---")

    # ---------------- ADD TASK ----------------

    st.subheader("Add Task")

    task_name = st.text_input("Task Name")
    description = st.text_area("Description")
    priority = st.selectbox("Priority", ["Low", "Medium", "High"])
    due_date = st.date_input("Due Date", min_value=date.today())

    if st.button("Add Task"):

        if not task_name or not description:
            st.error("Fill all fields")
            return

        st.session_state.tasks.append({
            "id": st.session_state.next_id,
            "task_name": task_name,
            "description": description,
            "priority": priority,
            "due_date": str(due_date),
            "completed": False
        })

        st.session_state.next_id += 1

        st.success("Task added")
        st.rerun()
        st.markdown("---")

    # ---------------- TABLE ----------------
    st.subheader("Task Overview")

    if st.session_state.tasks:

        rows = []

        for t in st.session_state.tasks:

            rows.append({
                "ID": t["id"],
                "Task": t["task_name"],
                "Description": t["description"],
                "Priority": t["priority"],
                "Due Date": t["due_date"],
                "Completed": "Yes" if t["completed"] else "No"
            })

        df = pd.DataFrame(rows)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("---")

        # ---------------- ACTIONS PER TASK ----------------
        st.subheader("Task Actions")

        for t in st.session_state.tasks:

            col1, col2, col3 = st.columns([3, 2, 2])

            with col1:
                st.write(f"{t['id']} - {t['task_name']}")

            with col2:

                if not t["completed"]:

                    if st.button(f"Mark Complete {t['id']}"):

                        t["completed"] = True

                        st.success(
                            f"Task {t['id']} completed"
                        )

                        st.rerun()

                else:
                    st.write("Done")

            with col3:

                if st.button(f"Delete {t['id']}"):

                    st.session_state.tasks = [
                        task
                        for task in st.session_state.tasks
                        if task["id"] != t["id"]
                    ]

                    st.success(
                        f"Task {t['id']} deleted"
                    )

                    st.rerun()

    else:
        st.info("No tasks available")

    st.markdown("---")

    if st.button("Logout"):

        st.session_state.logged_in = False
        st.session_state.user = ""
        st.session_state.page = "Login"

        st.rerun()


# --------------------------------------------------
# APP FLOW
# --------------------------------------------------

if st.session_state.logged_in:

    dashboard()

else:

    if st.session_state.page == "Register":

        register()

        if st.button("Go to Login"):

            st.session_state.page = "Login"
            st.rerun()

    else:

        login()

        if st.button("Go to Register"):

            st.session_state.page = "Register"
            st.rerun()