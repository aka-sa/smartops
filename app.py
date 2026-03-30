
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

st.subheader("📊 Analytics Dashboard")

expenses = get_all_expenses()

if expenses:

    amounts = [e[0] for e in expenses]
    categories = [e[1] for e in expenses]

    # -------- LINE CHART (SPENDING TREND) --------
    st.write("### 📈 Spending Trend")

    fig1 = plt.figure()
    plt.plot(amounts)
    plt.xlabel("Transactions")
    plt.ylabel("Amount")
    plt.title("Expense Trend")
    st.pyplot(fig1)

    # -------- BAR CHART (CATEGORY DISTRIBUTION) --------
    st.write("### 📊 Category Distribution")

    category_data = get_category_summary()
    cats = [c[0] for c in category_data]
    values = [c[1] for c in category_data]

    fig2 = plt.figure()
    plt.bar(cats, values)
    plt.xlabel("Category")
    plt.ylabel("Total Spend")
    plt.title("Category-wise Spending")
    st.pyplot(fig2)

    # -------- AI INSIGHTS --------
    st.write("### 🧠 AI Insights")

    insights = ai_insight_agent(expenses)

    for insight in insights:
        st.write(insight)

else:
    st.info("No expense data yet. Add some data to see analytics.")
