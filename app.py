import streamlit as st
import requests

st.title("AI Life-Load Assistant")

st.write("Enter your tasks and chores below, then click the button to get your unified plan.")

# --- NEW FIELDS ADDED FOR EXPECTED OUTCOME #1 ---
tasks = st.text_area("🧑‍💻 Enter your professional tasks (comma separated):")
chores = st.text_area("🏡 Enter your household chores (comma separated):")

if st.button("Get Today's Plan"):
    try:
        # Send tasks + chores to n8n as POST body
        payload = {
            "tasks": tasks,
            "chores": chores
        }

        result = requests.post("https://dhvanishah31.app.n8n.cloud/webhook/todayplan", json=payload).json()

        st.subheader("📌 Daily Summary")
        st.write(result.get("summary"))

        st.subheader("🧑‍💻 Prioritized Work Tasks")
        st.write(result.get("prioritized_work_tasks"))

        st.subheader("🏡 Prioritized Household Chores")
        st.write(result.get("prioritized_household_chores"))

        st.subheader("🍽 Meal Plan")
        st.write(result.get("meal_plan"))

        st.subheader("🛒 Grocery List")
        st.write(result.get("grocery_list"))

    except Exception as e:
        st.error("Webhook not connected yet or returned an error.")
        st.write(e)
