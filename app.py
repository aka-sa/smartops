
import streamlit as st
from llm import parse_and_extract
from agents import finance_agent, forecast, anomaly
from memory import add_memory, search_memory
import matplotlib.pyplot as plt
from database import get_all

st.title("SmartOps V3.2")

inp=st.text_input("Enter message")

if st.button("Run"):
    d=parse_and_extract(inp)
    if d["intent"]=="finance":
        res=finance_agent(d)
    else:
        res="Unknown"

    add_memory(inp)
    st.write(res)

data=get_all()
if data:
    st.line_chart(data)

st.subheader("Forecast")
st.write(forecast())

st.subheader("Anomalies")
st.write(anomaly())
