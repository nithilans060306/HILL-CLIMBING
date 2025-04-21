<h1>ExpNo 5 : Implement Simple Hill Climbing Algorithm</h1> 
<h3>Name: Nithilan S</h3>
<h3>Register Number: 212223240108</h3>
<H3>Aim:</H3>
<p>Implement Simple Hill Climbing Algorithm and Generate a String by Mutating a Single Character at each iteration </p>
<h2> Theory: </h2>
<p>Hill climbing is a variant of Generate and test in which feedback from test procedure is used to help the generator decide which direction to move in search space.
Feedback is provided in terms of heuristic function
</p>


<h2>Algorithm:</h2>
<p>
<ol>
 <li> Evaluate the initial state.If it is a goal state then return it and quit. Otherwise, continue with initial state as current state.</li> 
<li>Loop until a solution is found or there are no new operators left to be applied in current state:
<ul><li>Select an operator that has not yet been applied to the current state and apply it to produce a new state</li>
<li>Evaluate the new state:
  <ul>
<li>if it is a goal state, then return it and quit</li>
<li>if it is not a goal state but better than current state then make new state as current state</li>
<li>if it is not better than current state then continue in the loop</li>
    </ul>
</li>
</ul>
</li>
</ol>

</p>
<hr>
<h3> Steps Applied:</h3>
<h3>Step-1</h3>
<p> Generate Random String of the length equal to the given String</p>
<h3>Step-2</h3>
<p>Mutate the randomized string each character at a time</p>
<h3>Step-3</h3>
<p> Evaluate the fitness function or Heuristic Function</p>
<h3>Step-4:</h3>
<p> Lopp Step -2 and Step-3  until we achieve the score to be Zero to achieve Global Minima.</p>

## Program: 
```python
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
```

<hr>
<h2>Sample Input and Output</h2>
<h2>Sample String:</h2> Artificial Intelligence
<h2>Output:</h2>
Score: 643  Solution :  8RzF:oG ]%;CPORRMe!zGvk<br>
Score: 609  Solution :  8RzF:oG ]%;CPqRRMe!zGvk<br>
Score: 604  Solution :  8RzF:oG ]%;CPqRRMe!zGqk<br>
Score: 594  Solution :  8RzF:oG ]%;CPqRRWe!zGqk<br>
Score: 551  Solution :  8RzF:oGK]%;CPqRRWe!zGqk<br>
Score: 551  Solution :  8RzF:oGK]%;CPqRRWe!zGqk<br>
Score: 551  Solution :  8RzF:oGK]%;CPqRRWe!zGqk<br>
Score: 551  Solution :  8RzF:oGK]%;CPqRRWe!zGqk<br>
Score: 551  Solution :  8RzF:oGK]%;CPqRRWe!zGqk<br>
....................................................<br>
..................................................<br>
................................................<br>
Score: 1  Solution :  Artificial Intelligencf<br>
Score: 1  Solution :  Artificial Intelligencf<br>
Score: 1  Solution :  Artificial Intelligencf<br>
Score: 1  Solution :  Artificial Intelligencf<br>
Score: 0  Solution :  Artificial Intelligence<br>
