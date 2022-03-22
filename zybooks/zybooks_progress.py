chapters = [
    {"chapter": "1", "sections_assigned": 11, "sections_complete": 11},
    {"chapter": "2", "sections_assigned": 11, "sections_complete": 11},
    {"chapter": "3", "sections_assigned": 11, "sections_complete": 11},
    {"chapter": "4", "sections_assigned": 13, "sections_complete": 13},
    {"chapter": "5", "sections_assigned": 13, "sections_complete": 13},
    {"chapter": "6", "sections_assigned": 17, "sections_complete": 17},
    {"chapter": "7", "sections_assigned": 4, "sections_complete": 4},
    {"chapter": "8", "sections_assigned": 18, "sections_complete": 9},
    {"chapter": "12", "sections_assigned": 7, "sections_complete": 0}
]

sections_assigned = [i["sections_assigned"] for i in chapters]
total_assigned = sum(sections_assigned)

sections_complete = [i["sections_complete"] for i in chapters]
total_complete = sum(sections_complete)

print(f"zyBooks Progress: {total_complete / total_assigned * 100:.1f}%")
