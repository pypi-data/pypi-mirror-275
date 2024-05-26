# habit_tracker/habit_tracker.py

import json
import os
from datetime import date

HABITS_FILE = "habits.json"

def load_habits():
    if os.path.exists(HABITS_FILE):
        with open(HABITS_FILE, "r") as f:
            return json.load(f)
    return []

def save_habits(habits):
    with open(HABITS_FILE, "w") as f:
        json.dump(habits, f)

def add_habit(name):
    habits = load_habits()
    habits.append({"name": name, "dates": []})
    save_habits(habits)
    print(f"Added habit: {name}")

def list_habits():
    habits = load_habits()
    if not habits:
        print("No habits found.")
        return
    for i, habit in enumerate(habits, start=1):
        print(f"{i}. {habit['name']} - Progress: {len(habit['dates'])} days")

def mark_habit_done(habit_number):
    habits = load_habits()
    if 0 < habit_number <= len(habits):
        habit = habits[habit_number - 1]
        today = str(date.today())
        if today not in habit["dates"]:
            habit["dates"].append(today)
            save_habits(habits)
            print(f"Marked habit '{habit['name']}' as done for today.")
        else:
            print(f"Habit '{habit['name']}' is already marked as done for today.")
    else:
        print("Invalid habit number.")
