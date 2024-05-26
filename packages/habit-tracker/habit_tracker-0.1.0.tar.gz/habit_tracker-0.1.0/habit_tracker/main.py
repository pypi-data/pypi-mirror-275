# habit_tracker/main.py

import sys
from habit_tracker.habit_tracker import add_habit, list_habits, mark_habit_done

def main():
    if len(sys.argv) < 2:
        print("Usage: habits [add|list|done] <arguments>")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: habits add <habit name>")
            return
        name = " ".join(sys.argv[2:])
        add_habit(name)
    elif command == "list":
        list_habits()
    elif command == "done":
        if len(sys.argv) < 3:
            print("Usage: habits done <habit number>")
            return
        try:
            habit_number = int(sys.argv[2])
            mark_habit_done(habit_number)
        except ValueError:
            print("Habit number must be an integer.")
    else:
        print(f"Unknown command: {command}")
