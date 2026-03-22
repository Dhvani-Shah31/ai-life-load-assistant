import streamlit as st
import requests

st.title("AI Life-Load Assistant")

st.write("Click the button to fetch your plan for today!")

if st.button("Get Today's Plan"):
    try:
        result = requests.get("YOUR_N8N_WEBHOOK_URL").json()

        st.subheader("📌 Daily Summary")
        st.write(result.get("summary"))

        st.subheader("🍽 Meal Plan")
        st.write(result.get("meal_plan"))

        st.subheader("🛒 Grocery List")
        st.write(result.get("grocery_list"))
    except:
        st.error("Webhook not connected yet. We will fix this soon!")
