from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def suggest_priority(title: str, description: str = ""):
    prompt = f"""
    Given this task:
    Title: {title}
    Description: {description}

    Respond ONLY in JSON format, nothing else, no extra text:
    {{
        "priority": "high or medium or low",
        "estimated_time": "e.g. 2 hours",
        "reason": "why this priority"
    }}
    """
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    text = response.text.strip().replace("```json", "").replace("```", "")
    return json.loads(text)


def breakdown_goal(goal: str):
    prompt = f"""
    Break this goal into smaller actionable tasks:
    Goal: {goal}

    Respond ONLY in JSON format, nothing else, no extra text:
    {{
        "subtasks": ["subtask 1", "subtask 2", "subtask 3"]
    }}
    """
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    text = response.text.strip().replace("```json", "").replace("```", "")
    return json.loads(text)


def daily_summary(tasks: list):
    task_list = "\n".join([
        f"- {t['title']} (priority: {t['priority']}, status: {t['status']})"
        for t in tasks
    ])
    prompt = f"""
    Here are my tasks:
    {task_list}

    Give me a smart daily plan.
    Respond ONLY in JSON format, nothing else, no extra text:
    {{
        "summary": "overall summary",
        "focus_first": "what to do first and why",
        "plan": ["step 1", "step 2", "step 3"]
    }}
    """
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    text = response.text.strip().replace("```json", "").replace("```", "")
    return json.loads(text)