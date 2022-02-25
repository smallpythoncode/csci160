# https://www.youtube.com/watch?v=-i5YrgqF9Gg

import random


def grade_assignment():
    grade = random.randint(70, 100)
    return grade


male_superiority = 0
female_superiority = 0
equal_skill = 0
iterations = 100000

progress_marker = 0.05
while male_superiority + female_superiority < iterations:
    if (male_superiority + female_superiority) / iterations >= progress_marker:
        print(f"{int(progress_marker * 100)}% complete")
        progress_marker += 0.05
    male_list = []
    female_list = []

    while len(male_list) < 800:
        male_list.append(grade_assignment())
    while len(female_list) < 200:
        female_list.append(grade_assignment())

    male_candidates = []
    female_candidates = []

    while len(male_candidates) < 25:
        male_candidate = male_list[random.randint(0, len(male_list) - 1)]
        male_candidates.append(male_candidate)
        male_list.remove(male_candidate)
    male_candidates.sort()

    while len(female_candidates) < 25:
        female_candidate = female_list[random.randint(0, len(female_list) - 1)]
        female_candidates.append(female_candidate)
        female_list.remove(female_candidate)
    female_candidates.sort()

    male_average = sum(male_candidates) / len(male_candidates)
    female_average = sum(female_candidates) / len(female_candidates)

    if male_average == female_average:
        equal_skill += 1
    elif male_average > female_average:
        male_superiority += 1
    else:
        female_superiority += 1

print(f"Male Superiority: {male_superiority}")
print(f"Female superiority: {female_superiority}")
print(f"Equal skill: {equal_skill}")
