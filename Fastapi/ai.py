from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def suggest_priority(title: str, description: str = ""):
    prompt = f"""
    Given this task:
    Title: {title}
    Description: {description}

    Respond ONLY in valid JSON format, no extra text, no markdown:
    {{"priority": "high or medium or low", "estimated_time": "e.g. 2 hours", "reason": "why this priority"}}
    """
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        text = response.choices[0].message.content.strip()
        text = text.replace("```json", "").replace("```", "").strip()
        return json.loads(text)
    except Exception as e:
        return {"error": str(e)}


def breakdown_goal(goal: str):
    prompt = f"""
    Break this goal into smaller actionable tasks:
    Goal: {goal}

    Respond ONLY in valid JSON format, no extra text, no markdown:
    {{"subtasks": ["subtask 1", "subtask 2", "subtask 3"]}}
    """
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        text = response.choices[0].message.content.strip()
        text = text.replace("```json", "").replace("```", "").strip()
        return json.loads(text)
    except Exception as e:
        return {"error": str(e)}


def daily_summary(tasks: list):
    task_list = "\n".join([
        f"- {t['title']} (priority: {t['priority']}, status: {t['status']})"
        for t in tasks
    ])
    prompt = f"""
    Here are my tasks:
    {task_list}

    Give me a smart daily plan.
    Respond ONLY in valid JSON format, no extra text, no markdown:
    {{"summary": "overall summary", "focus_first": "what to do first and why", "plan": ["step 1", "step 2", "step 3"]}}
    """
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        text = response.choices[0].message.content.strip()
        text = text.replace("```json", "").replace("```", "").strip()
        return json.loads(text)
    except Exception as e:
        return {"error": str(e)}