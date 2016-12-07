#!/usr/bin/python3

# Random walk generator programmed for my Introduction to Python class at UC Santa Cruz in Fall 2016
# Programmed very early in the quarter, and before we had knowledge of any of Python's more complicated data structures

# necessary modules
import math
import random


# Function that asks for parameters
def prompt(input_value, min_value, max_value, question):
    # Asks for a value to assign to input_value with a unique question
    while input_value < min_value or input_value > max_value:
        input_value = int(input(question))
    return input_value


# Function to repeat the walk the number of times specified by user
# The method I use here for mean and SD was found at http://stackoverflow.com/questions/1174984/how-to-efficiently-calculate-a-running-standard-deviation
def walk_repeater(walks_so_far, steps_taken, num_min, num_max, num_5000, running_steps_sum_min, running_steps_sum_min2,
                  running_steps_sum_max, running_steps_sum_max2, mean_max, SD_max, mean_min, SD_min):
    # lists to be filled with step data as the simulation runs
    # function runs as long as fewer walks have been run than the user wanted to run
    for walks_so_far in range(0, number_walks):
        # noinspection PyUnusedLocal
        walks_so_far = walks_so_far + 1
        # this function triggers the random walk function a certain number of times
        steps_taken = random_walk(start_location, 0, 0)
        # What happens if a walk terminates at the minimum constraint:
        if steps_taken < 0:
            # Counts the number of walks that terminate at minimum
            num_min = num_min + 1
            # Keeps track of the sum of the number of steps taken (for mean calculation)
            running_steps_sum_min = running_steps_sum_min + abs(steps_taken)
            # Keeps track of the sum of the number of steps taken squared (for SD calculation)
            running_steps_sum_min2 = running_steps_sum_min2 + ((abs(steps_taken)) ** 2)
        # Keeps track of how many walks hit the step limit (5000)
        elif steps_taken == 5000:
            num_5000 = num_5000 + 1
        # What happens if a walk terminates at the maximum constraint:
        else:
            # Counts the number of walks that terminate at maximum
            num_max = num_max + 1
            # Keeps track of the sum of the number of steps taken (for mean calculation)
            running_steps_sum_max = running_steps_sum_max + steps_taken
            # Keeps track of the sum of the number of steps taken squared (for SD calculation)
            running_steps_sum_max2 = running_steps_sum_max2 + (steps_taken ** 2)
        # Mean and SD are only calculated if more than 0 walks terminate at a wall
        if num_max > 0:
            mean_max = running_steps_sum_max / num_max
            SD_max = math.sqrt((running_steps_sum_max2 / num_max) - (mean_max ** 2))
        if num_min > 0:
            mean_min = running_steps_sum_min / num_min
            SD_min = math.sqrt((running_steps_sum_min2 / num_min) - (mean_min ** 2))
    print("Number of walks terminated at 5000 steps:", num_5000)
    if num_5000 > 0:
        print(
            "The mean number of steps taken for the above was 5000. The standard deviation was 0.")  # No point in calculating these when all the numbers are 5000
    else:
        print("No walks ended at 5000 steps. Therefore, no mean nor standard deviation can be calculated")
    print("Number of walks terminated at the minimum constraint:", num_min)
    if num_min > 0:
        print("The mean number of steps taken for the above was ", mean_min, ". The standard deviation was ", SD_min,
              ".")
    else:
        print(
            "No walks ended at the minimum constraint. Therefore, neither mean nor standard deviation can be calculated")
    print("Number of walks terminated at the maximum constraint:", num_max)
    if num_max > 0:
        print("The mean number of steps taken for the above was ", mean_max, ". The standard deviation was ", SD_max,
              ".")
    else:
        print(
            "No walks ended at the maximum constraint. Therefore, neither mean nor standard deviation can be calculated")


# Function to do one random walk
def random_walk(current_pos, step_chance, step_count):
    # function repeats until 5000 steps have been taken
    for step_count in range(0, 5001):
        # rolls a new d100 for each step
        step_chance = random.randint(1, 100)
        # rolls less than or equal to thr chance of going right trigger a right step
        if step_chance <= right_chance:
            # adds one to current position (right step)
            current_pos = current_pos + 1
            # adds one to step count
            step_count = step_count + 1
            # If the point hits the max wall, the function ends and step count is returned
            if current_pos == max_wall:
                return step_count
        # rolls greater than the right chance trigger a left step
        elif step_chance > right_chance:
            current_pos = current_pos - 1
            step_count = step_count + 1
            # If the point hits the min wall, the function ends and the negative step count is returned
            if current_pos == min_wall:
                return -step_count
    # if no walls are hit and the step count reaches 5000, the program returns 5000
    return 5000


start_location = prompt(-100, 1, 499, "Where should this random walk begin (1-499)?")

# This if/else ensures that the user does not input a minimum constraint larger than the starting position
if start_location > 199:
    min_wall = prompt(-100, 0, 199,
                      "What is the minimum value for this walk (0-199 and smaller than starting position)?")
else:
    min_wall = prompt(-100, 0, start_location,
                      "What is the minimum value for this walk (0-199 and smaller than starting position)?")

# This if/else ensures that the user does not input a maximum constraint smaller than the starting position
if start_location < 201:
    max_wall = prompt(-100, 201, 500,
                      "What is the maximum value for this walk (201-500 and larger than starting position)?")
else:
    max_wall = prompt(-100, start_location, 500,
                      "What is the maximum value for this walk (201-500 and larger than starting position)?")

right_chance = prompt(-100, 1, 99, "What is the chance of stepping right (1-99)?")

number_walks = prompt(-100, 1, 10000, "How many walks will be simulated (1-10000)?")

# All values assigned to zero assigned in function
walk_repeater(number_walks, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
