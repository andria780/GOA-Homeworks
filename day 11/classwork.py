score = int(input("what did you get in the test:    "))

if score > 90 and score < 100:
    print("თქვენ დაგიფინანსდათ სწავლა სრულიად")

if score > 80 and score < 100:
    print("თქვენ დაგიფინანსდათ სწავლა 1500 ლარით")

if score > 40 and score < 70:
    print("თქვენ დაგიფინანსდათ სწავლა 500 ლარით")

if score < 40:
    print("თქვენ არ დაგიფინანსდათ სწავლის პროცესი")