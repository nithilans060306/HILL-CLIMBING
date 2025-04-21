#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import string

def generate_random_solution(answer):
    # Find the length of 'answer' and store in 'l'
    l = len(answer)
    # Return a random list of characters of the same length as 'answer'
    return [random.choice(string.printable) for _ in range(l)]

def evaluate(solution, answer):
    print(solution)
    target = list(answer)
    diff = 0
    for i in range(len(target)):
        s = solution[i]
        t = target[i]
        # Calculate the "difference" between two strings, character by character.
        # ord(s) - ord(t) calculates the difference between ASCII values.
        # abs() ensures the difference is non-negative.
        diff += abs(ord(s) - ord(t))
    return diff

def mutate_solution(solution):
    # Select a random index in the solution to mutate
    ind = random.randint(0, len(solution) - 1)
    # Change the character at the selected index to a random printable character
    solution[ind] = random.choice(string.printable)
    return solution

def SimpleHillClimbing():
    answer = "Artificial Intelligence"
    # Generate a random initial solution
    best = generate_random_solution(answer)
    # Evaluate the score of the initial solution
    best_score = evaluate(best, answer)
    
    while True:
        print("Score:", best_score, " Solution:", "".join(best))
        # If the best score is 0, the goal state is reached
        if best_score == 0:
            break
        # Generate a new solution by mutating the current one
        new_solution = mutate_solution(list(best))
        # Evaluate the new solution
        score = evaluate(new_solution, answer)
        # If the new solution is better, update the best solution
        if score < best_score:
            best = new_solution
            best_score = score

# answer = "Artificial Intelligence"
# Uncomment the following lines for debugging or testing purposes
# print(generate_random_solution(answer))
# solution = generate_random_solution(answer)
# print(evaluate(solution, answer))
SimpleHillClimbing()
