
import streamlit as st
from llm import parse_intent
from agents import finance_agent, inventory_agent, insight_agent, ai_insight_agent
from memory import add_memory, search_memory
from evaluation import update, get_metrics
import matplotlib.pyplot as plt
from database import get_all_expenses, get_category_summary

st.title("SmartOps V3.1 Research System")

user_input = st.text_input("Enter message")

if st.button("Run"):
    intent = parse_intent(user_input)
    mem = search_memory(user_input)

    if intent == "finance":
        res = finance_agent(user_input)
    elif intent == "inventory":
        res = inventory_agent(user_input)
    elif intent == "insight":
        res = insight_agent(user_input)
    else:
        res = "Unknown"

    add_memory(user_input)
    update(correct=True)

    st.write("Intent:", intent)
    st.write("Memory:", mem)
    st.write("Response:", res)

st.subheader("Evaluation Metrics")
st.json(get_metrics())
