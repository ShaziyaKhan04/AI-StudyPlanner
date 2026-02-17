## AI-StudyPlanner
### AI Study Planner – Agentic AI Project
## Overview

AI Study Planner is an Agentic AI-powered web application built using Streamlit and LangGraph.
It generates a structured 4-week study roadmap based on a user's topic, skill level, and available weekly study hours.

Instead of using a single prompt, this application uses a multi-step AI workflow to intelligently break down learning goals into actionable study plans.

## Key Features

Topic-based syllabus breakdown
Intelligent weekly time allocation
Clean 4-week structured roadmap
Multi-step agent workflow using LangGraph
Fast inference powered by Groq (Llama 3.1)
Clean and responsive UI using Streamlit

## Tech Stack

Frontend: Streamlit
Agent Framework: LangGraph
LLM: Llama 3.1 (via Groq API)
Language: Python
Architecture: Multi-node state-based agent system

## How It Works

The system follows a structured agent workflow:

Syllabus Breakdown Node
Generates a detailed syllabus based on topic and level.

Time Allocation Node
Distributes weekly study hours across the syllabus.

Final Roadmap Node
Produces a clean and organized 4-week study plan.

Each node passes its output to the next using a shared state object, making the system modular and scalable.

## Architecture Flow

User Input → Breakdown Node → Time Allocation Node → Final Plan Node → Output
This modular design improves reasoning quality compared to single-prompt AI systems.

## Why This Project?

This project demonstrates:

Agentic AI system design
State management in LLM workflows
Multi-step reasoning using LangGraph
Practical AI application development
UI integration with AI backend
