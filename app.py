import streamlit as st
import os
from typing import TypedDict
from langgraph.graph import StateGraph
from langchain_groq import ChatGroq

# 🔐 API Key
os.environ["GROQ_API_KEY"] = "Api key"

llm = ChatGroq(model="llama-3.1-8b-instant")

# 🧠 State
class PlannerState(TypedDict):
    topic: str
    level: str
    hours: int
    breakdown: str
    schedule: str
    final_plan: str

# 🔹 Nodes
def breakdown_node(state: PlannerState):
    response = llm.invoke(
        f"Create syllabus breakdown for {state['topic']} at {state['level']} level"
    )
    return {"breakdown": response.content}

def time_node(state: PlannerState):
    response = llm.invoke(
        f"Divide {state['hours']} hours weekly based on this:\n{state['breakdown']}"
    )
    return {"schedule": response.content}

def final_node(state: PlannerState):
    response = llm.invoke(
        f"Create 4-week roadmap based on:\n{state['schedule']}"
    )
    return {"final_plan": response.content}

# 🔹 Graph
graph = StateGraph(PlannerState)
graph.add_node("breakdown", breakdown_node)
graph.add_node("time", time_node)
graph.add_node("final", final_node)
graph.set_entry_point("breakdown")
graph.add_edge("breakdown", "time")
graph.add_edge("time", "final")
app_graph = graph.compile()

# 🎨 UI
st.title("AI Study Planner")

topic = st.text_input("Enter Topic")
level = st.selectbox("Select Level", ["Beginner", "Intermediate", "Advanced"])
hours = st.number_input("Hours per week", min_value=1, max_value=40)

if st.button("Generate Plan"):
    result = app_graph.invoke({
        "topic": topic,
        "level": level,
        "hours": hours
    })
    
    st.subheader("Final Study Plan")
    st.write(result["final_plan"])
