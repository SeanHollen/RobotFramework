*** Settings ***
Documentation     Test cases
...
Library           ExerciseLibrary.py

*** Test Cases ***

One Exercise Test
    Expect summary    13 0 0
    Exercise    curls: 4 sets
    Expect summary    12 1 0

Powerlifting Workout Routine (Phrak's Greyskull LP Variant)
    Exercise    overhead press: 3 sets 5 reps
    Exercise    chinups: 3 sets 5 reps
    Exercise    squats: 3 sets 5 reps
    Full rest
    Exercise    bench press: 3 sets 5 reps
    Exercise    rows: 3 sets 5 reps
    Exercise    deadlifts: 1 sets 5 reps
    Full rest

Mark Ripptoe SS Exercise Routine
    Exercise    squats: 3 sets 5 reps
    Exercise    bench press: 3 sets 5 reps
    Exercise    deadlifts: 1 sets 5 reps
    Full rest
    Exercise    squats: 3 sets 5 reps
    Exercise    overhead press: 3 sets 5 reps
    Exercise    deadlifts: 1 sets 5 reps
    Full rest
    # skipping to phase 3
    Exercise    squats: 3 sets 5 reps
    Exercise    bench press: 3 sets 5 reps
    Exercise    chin ups: 3 sets 10 reps
    Full rest

My Routine Before Pandemic
    Exercise    squats: 3 sets 5 reps
    Exercise    overhead press: 3 sets 5 reps
    Exercise    chinups: 3 sets 10 reps
    Exercise    face pulls: 3 sets 10 reps
    Exercise    dips: 2 sets 10 reps
    Exercise    hanging leg raises: 2 sets 10 reps
    Exercise    farmers carries: 2 sets 5 reps
    Full Rest
    Exercise    deadlifts: 1 sets 5 reps
    Exercise    rack pulls: 1 sets 10 reps
    Exercise    bench press: 3 sets 5 reps
    Exercise    face pulls: 2 sets 10 reps
    Exercise    curls: 2 sets 10 reps
    Exercise    situps: 2 sets 10 reps
    Exercise    calf raises: 2 sets 10 reps
    Full Rest

Lawrence Ballenger Bodybuilding Workout Split
    # legs
    Exercise    squats: 4 sets
    Exercise    leg press: 4 sets
    Exercise    squats: 4 sets
    Exercise    leg press: 4 sets
    Exercise    leg extensions: 4 sets
    Rest    0.5
    # back
    Exercise    pullups: 4 reps
    Exercise    chinups: 4 reps
    Exercise    rows: 4 reps
    Exercise    deadlifts: 4 reps
    Exercise    rows: 4 reps
    Exercise    pullups: 4 reps
    Exercise    shrugs: 4 reps
    Rest    0.5
    # chest
    Exercise    bench press: 4 reps
    Exercise    bench press: 4 reps
    Exercise    overhead press: 4 reps
    Exercise    flyes: 4 reps
    Exercise    dips: 4 reps
    Rest    0.5
    # legs (calves+hamstrings)
    Exercise    leg curls: 4 reps
    Exercise    deadlifts: 4 reps
    Exercise    squats: 4 reps
    Exercise    calf raises: 4 reps
    Exercise    calf raises: 4 reps
    Exercise    squats: 4 reps
    Rest    0.5
    # shoulders
    Exercise    lat raises: 4 reps
    Exercise    lat raises: 4 reps
    Exercise    rows: 4 reps
    Exercise    overhead press: 4 reps
    Exercise    overhead press: 4 reps
    Exercise    shrugs: 4 reps
    Rest    0.5
    # arms
    Exercise    curls: 4 reps
    Exercise    dips: 4 reps
    Exercise    curls: 4 reps
    Exercise    tricep pushdowns: 4 reps
    Exercise    curls: 4 reps
    Exercise    tricep pullovers: 4 reps
    Exercise    pull ups: 4 reps
    Exercise    tricep pushdowns: 4 reps
