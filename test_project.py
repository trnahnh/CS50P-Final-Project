# CS50 Python Final Project: Fitness Helper
# Full name: Anh Tran
# GitHub & edX usernames: trnahnh
# Hue, Vietnam --> Cincinnati, OH
# CS50P - Recorded Date: 04/09/2025

import pytest
from project import fitness_advice, meal_plan_prep, contact, lifting_split


def test_fitness_advice():
    tip = fitness_advice()
    valid_tips = [
        "Every rep range should vary from 4-8 within 0-2 RIR (Reps in Reserved) left in the tank to preserve the RPE (Rate of Perceived Exertion) for the next set.",
        "Rest days are as important as training days. Having 2-3 rest days a week is the most optimal.",
        "Compound lifts regarding SBD (Squat, Bench Press, Deadlift) are the most obvious signs of whether you are progressing or not.",
        "Stay hydrated, having enough meals regarding consuming all necessary macro-nutrients, micro-nutrients, and vitamins.",
    ]
    assert tip in valid_tips


def test_meal_plan_prep_valid():
    plan = meal_plan_prep(2000, 4)
    assert len(plan) == 4
    expected_cal = 2000 / 4
    for row in plan:
        assert f"{expected_cal:.2f}" in row[1]


def test_meal_plan_prep_zero():
    plan = meal_plan_prep(2000, 0)
    assert plan[0][2] == "Meal Counting should not be zero"


def test_contact():
    info = contact()
    keys = {row[0] for row in info}
    assert "Name" in keys
    assert "Email" in keys
    assert "Github" in keys


def test_lifting_split_3():
    split = lifting_split(3)
    expected = [
        ["Day 1", "Full Body"],
        ["Day 2", "Rest or Active Cardio"],
        ["Day 3", "Full Body"],
    ]
    assert split == expected


def test_lifting_split_4():
    split = lifting_split(4)
    expected = [
        ["Day 1", "Upper Body"],
        ["Day 2", "Lower Body"],
        ["Day 3", "Rest"],
        ["Day 4", "Full Body"],
    ]
    assert split == expected


def test_lifting_split_5():
    split = lifting_split(5)
    expected = [
        ["Day 1", "Push: Chest, Shoulders, Triceps"],
        ["Day 2", "Pull: Back, Biceps"],
        ["Day 3", "Legs"],
        ["Day 4", "Core & Cardio"],
        ["Day 5", "Accessory/Full Body"],
    ]
    assert split == expected


def test_lifting_split_invalid():
    split = lifting_split(7)
    assert "No lifting schedule available" in split[0][1]
