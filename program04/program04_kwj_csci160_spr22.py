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
Prompt for integers until the user enters 0, at which time display the
average of the positive values and the average of the negative values.
Make no assumption about the type of data entered. If a positive or
negative value cannot be calculated, state that no values of that type
(+/-) were entered. Round the averages to 2 decimal places.

-Part D-
Create a table that lists degrees Celsius from 0 to 100 in one column
and their respective conversion to degrees Fahrenheit in the next
column. List temperatures as integers and justify them to the right.
"""

# print("-Part A-")

print("\n-Part B-")
grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
total_points = 0
while True:
    try:
        num_scores = int(input("Enter the number of quiz scores: "))
        if num_scores < 0:
            print("The number of scores must be a positive integer.")
        elif num_scores == 0:
            print("Refer to the definition of futility.")
            break
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
        print("Enter the number of scores as an integer.")

print("\n-Part C-")
print("Enter either positive or negative integers.")
print("To stop, enter \"0\".")

pos_values = []
neg_values = []
while True:
    value = int(input("Enter a value: "))
    if value == 0:
        if len(pos_values) == 0:
            print("No positive values were entered.")
        else:
            print("Average of positive values: "
                  f"{sum(pos_values) / len(pos_values):.2f}")
        if len(neg_values) == 0:
            print("No negative values were entered.")
        else:
            print("Average of negative values: "
                  f"{sum(neg_values) / len(neg_values):.2f}")
        break
    elif value > 0:
        pos_values.append(value)
    else:
        neg_values.append(value)

print("\n-Part D-")
# len_str_c == 7, len_str_f == 10
print("Celsius | Fahrenheit")
print("¯" * 8, "|", "¯" * 11, sep="")
for temp_c in range(0, 101, 5):
    temp_f = round(temp_c * 1.8 + 32)
    print(f"{temp_c:>7d}", "|", f"{temp_f:>10d}")

# All work and no play makes Jack a dull boy.
