
from database import add_expense, get_all
import numpy as np

def finance_agent(d):
    add_expense(d["amount"], d["category"])
    return f"Saved ₹{d['amount']} for {d['category']}"

def forecast():
    data=get_all()
    if len(data)<2: return "Not enough data"
    trend=np.polyfit(range(len(data)),data,1)
    next_val=trend[0]*len(data)+trend[1]
    return f"Next expense prediction: ₹{round(next_val,2)}"

def anomaly():
    data=get_all()
    if len(data)<2: return []
    mean=np.mean(data)
    std=np.std(data)
    return [x for x in data if abs(x-mean)>2*std]
