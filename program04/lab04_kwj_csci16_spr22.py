"""
Jahnke
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160 - Spring 2022
Lab 04 Parts A, B, C, D

Print a string specifying the start of each part (e.g., "-Part A-")

-Part A-

-Part B-
1. Prompt for a number of quiz scores.
2. Prompt for scores up to the number of quiz scores.
3. Display the number of A's, B's, C's, D's, and F's.
4. Display the class average of the quiz to 2 decimal places.

-Part C-

-Part D-

"""

# print("-Part A-")

print("\n-Part B-")
grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
total_points = 0
while True:
    try:
        num_scores = int(input("Enter the number of quiz scores: "))
        if num_scores <= 0:
            print("The number of scores must be a positive integer.")
        else:
            scores_counted = 0
            while scores_counted < num_scores:
                try:
                    score = float(input("Enter score number"
                                        f" {scores_counted + 1}: "))
                    if score < 0 or score > 100:
                        print("Scores must be between 0 and 100, inclusive.")
                    else:
                        total_points += score
                        if score >= 90:
                            grades["A"] += 1
                            scores_counted += 1
                        elif score >= 80:
                            grades["B"] += 1
                            scores_counted += 1
                        elif score >= 70:
                            grades["C"] += 1
                            scores_counted += 1
                        elif score >= 60:
                            grades["D"] += 1
                            scores_counted += 1
                        else:
                            grades["F"] += 1
                            scores_counted += 1
                except ValueError:
                    print("Scores must be entered as a number.")
            print("Number of A's:", grades["A"])
            print("Number of B's:", grades["B"])
            print("Number of C's:", grades["C"])
            print("Number of D's:", grades["D"])
            print("Number of F's:", grades["F"])
            print(f"Class average: {total_points / num_scores:.2f}")
            break
    except ValueError:
        print("Enter number of scores as an integer.")

# print("-Part C-")


# print("-Part D-")



# All work and no play makes Jack a dull boy.
