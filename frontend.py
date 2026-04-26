
import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Project 6 SaaS",
    page_icon="🚀",
    layout="wide"
)

# SESSION 
if "token" not in st.session_state:
    st.session_state.token = None

if "username" not in st.session_state:
    st.session_state.username = None

if "role" not in st.session_state:
    st.session_state.role = None


# LOGIN MODE
if st.session_state.token:

    st.sidebar.success("Logged In")
    st.sidebar.write(f"User: {st.session_state.username}")

    # role badge
    if st.session_state.role == "admin":
        st.sidebar.error("ROLE: ADMIN")
    else:
        st.sidebar.info("ROLE: USER")

    if st.sidebar.button("Logout"):
        st.session_state.token = None
        st.session_state.username = None
        st.session_state.role = None
        st.rerun()

    st.markdown("# 🚀 Project 6 Admin Dashboard")
    st.caption("Premium SaaS Management Platform")

    # load users
    r = requests.get(f"{API_URL}/users")
    users = r.json()

    st.metric("Total Users", len(users))

    st.divider()

    # ---------- CHARTS ----------
    st.subheader("📊 User Analytics")

    admin_count = len([
        u for u in users
        if u.get("role") == "admin"
    ])

    user_count = len(users) - admin_count

    chart_data = pd.DataFrame(
        {
            "count": [admin_count, user_count]
        },
        index=["Admin", "User"]
    )

    st.bar_chart(chart_data)

    st.subheader("📈 Growth Preview")

    growth_data = pd.DataFrame({
        "users": list(range(1, len(users) + 1))
    })

    st.line_chart(growth_data)

    st.divider()

    # ---------- USERS TABLE ----------
    st.subheader("All Users")

    df = pd.DataFrame(users)
    st.dataframe(df, use_container_width=True)

    # ---------- ADMIN EXPORT CSV ----------
    if st.session_state.role == "admin":

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📥 Download Users CSV",
            data=csv,
            file_name="users.csv",
            mime="text/csv"
        )

    st.divider()

    # ---------- DELETE USER ----------
    if st.session_state.role == "admin":

        st.subheader("Delete User")

        non_admin_users = [
            u for u in users
            if u["username"] != "admin"
        ]

        if len(non_admin_users) == 0:
            st.info("No deletable users")

        else:

            options = {
                f'{u["id"]} - {u["username"]}': u["id"]
                for u in non_admin_users
            }

            selected = st.selectbox(
                "Select user",
                list(options.keys())
            )

            confirm = st.checkbox(
                "I confirm delete this user"
            )

            if st.button("Delete User"):

                if not confirm:
                    st.warning("Please confirm first")

                else:

                    user_id = options[selected]

                    d = requests.delete(
                        f"{API_URL}/users/{user_id}"
                    )

                    res = d.json()

                    if "message" in res:
                        st.success(res["message"])
                        st.rerun()
                    else:
                        st.error(res["detail"])

    else:
        st.warning("Only admin can manage users.")

# GUEST MODE 
else:

    st.markdown("# 🚀 Project 6 SaaS")
    st.caption("Modern Authentication & Analytics Platform")

    menu = st.sidebar.selectbox(
        "Menu",
        ["Login", "Register"]
    )

    if menu == "Login":

        username = st.text_input("Username")
        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            r = requests.post(
                f"{API_URL}/login",
                json={
                    "username": username,
                    "password": password
                }
            )

            res = r.json()

            if "access_token" in res:

                token = res["access_token"]

                # call /me
                me = requests.get(
                    f"{API_URL}/me",
                    headers={
                        "Authorization": f"Bearer {token}"
                    }
                ).json()

                st.session_state.token = token
                st.session_state.username = me["username"]
                st.session_state.role = me["role"]

                st.rerun()

            else:
                st.error("Login failed")


    if menu == "Register":

        username = st.text_input("New Username")
        password = st.text_input(
            "New Password",
            type="password"
        )

        if st.button("Create Account"):

            requests.post(
                f"{API_URL}/register",
                json={
                    "username": username,
                    "password": password
                }
            )

            st.success("Account created")
