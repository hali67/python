test_dict = {
    "grade1": {"name": "Sara", "grade result": 56, "subject": "math"},
        "grade2": {"name": "David", "grade result": 87, "subject": "english"},
        "grade3": {"name": "Sarah", "grade result": 92, "subject": "science"},
        "grade4": {"name": "Allan", "class": 79, "subject": "History"},
}
list=["Sara", "David", "Sara", "Allan"]
print("Sara -")
print(test_dict["grade1"].get('grade for math', 56))

print("David -")
print(test_dict["grade2"].get ('grade for english', 87))

print("Sarah -")
print(test_dict["grade3"].get ('grade for science', 92))

print("Allan -")
print(test_dict["grade4"].get ('grade for history', 79))






