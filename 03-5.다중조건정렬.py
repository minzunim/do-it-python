scores = [
    (80, 100),
    (100, 50),
    (70, 100),
    (80, 90)
]

scores.sort(key=lambda x: (-x[0], -x[1]))

print(scores)