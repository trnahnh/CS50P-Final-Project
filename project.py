# CS50 Python Final Project: Fitness Helper
# Full name: Anh Tran
# GitHub & edX usernames: trnahnh
# Hue, Vietnam --> Cincinnati, OH
# CS50P - Recorded Date: 04/09/2025

## INSTRUCTIONS:
# python project.py tip
# python project.py meal --calories <total calories> --meal <total meals>
# python project.py contact
# python project.py schedule --days <total days>

import random
import argparse
import pyfiglet
from tabulate import tabulate
from termcolor import colored


def fitness_advice():
    tips = [
        "Every rep range should vary from 4-8 within 0-2 RIR (Reps in Reserved) left in the tank to preserve the RPE (Rate of Perceived Exertion) for the next set.",
        "Rest days are as important as training days. Having 2-3 rest days a week is the most optimal.",
        "Compound lifts regarding SBD (Squat, Bench Press, Deadlift) are the most obvious signs of whether you are progressing or not.",
        "Stay hydrated, having enough meals regarding consuming all necessary macro-nutrients, micro-nutrients, and vitamins.",
    ]
    return random.choice(tips)


def meal_plan_prep(cals_total, meals_num):
    try:
        cals_pm = cals_total / meals_num
    except ZeroDivisionError:
        return [["Error", "Not Applicable", "Meal Counting should not be zero"]]
    plan = []
    for meal in range(1, meals_num + 1):
        advice = "Include protein, carbs, and healthy fats in every meal"
        plan.append([f"Meal {meal}", f"{cals_pm:.2f} calories", advice])
    return plan


def contact():
    return [
        ["Name", "Andrea Tran"],
        ["Email", "tran3ah@mail.uc.edu"],
        ["Github", "trnahnh"],
    ]


def lifting_split(days):
    if days == 3:
        schedule = [
            ["Day 1", "Full Body"],
            ["Day 2", "Rest or Active Cardio"],
            ["Day 3", "Full Body"],
        ]
    elif days == 4:
        schedule = [
            ["Day 1", "Upper Body"],
            ["Day 2", "Lower Body"],
            ["Day 3", "Rest"],
            ["Day 4", "Full Body"],
        ]
    elif days == 5:
        schedule = [
            ["Day 1", "Push: Chest, Shoulders, Triceps"],
            ["Day 2", "Pull: Back, Biceps"],
            ["Day 3", "Legs"],
            ["Day 4", "Core & Cardio"],
            ["Day 5", "Accessory/Full Body"],
        ]
    else:
        schedule = [["Note", f"No lifting schedule available for {days} days."]]
    return schedule


def main():
    parser = argparse.ArgumentParser(
        description="Fitness Helper: Get fitness tips, meal plans, contact info for further discussion, or lifting schedules."
    )
    subparsers = parser.add_subparsers(
        dest="command", help="Choose a command", required=True
    )
    subparsers.add_parser("tip", help="Display a random fitness tip.")
    meal_parser = subparsers.add_parser("meal", help="Generate a meal plan.")
    meal_parser.add_argument(
        "--calories", type=int, required=True, help="Total daily calorie target."
    )
    meal_parser.add_argument(
        "--meals", type=int, required=True, help="Number of meals per day."
    )
    subparsers.add_parser("contact", help="Display contact information.")
    schedule_parser = subparsers.add_parser(
        "schedule", help="Generate a lifting schedule."
    )
    schedule_parser.add_argument(
        "--days", type=int, required=True, help="Number of lifting days per week."
    )
    args = parser.parse_args()

    fancy_title = pyfiglet.figlet_format("Fitness Helper")
    print(colored(fancy_title, "green"))
    print(colored("Developed by Anh Tran", "cyan"))
    print(colored("CS50 Python Final Project", "cyan"))

    if args.command == "tip":
        tip = fitness_advice()
        table = [["Fitness Tip", tip]]
        print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))
    elif args.command == "meal":
        plan = meal_plan_prep(args.calories, args.meals)
        print(
            tabulate(
                plan, headers=["Meal", "Calories", "Suggestion"], tablefmt="fancy_grid"
            )
        )
    elif args.command == "contact":
        info = contact()
        print(tabulate(info, tablefmt="fancy_grid"))
    elif args.command == "schedule":
        schedule = lifting_split(args.days)
        print(tabulate(schedule, headers=["Day", "Workout"], tablefmt="fancy_grid"))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()