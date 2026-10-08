scores = list(map(float, input("Enter scores separated by spaces: ").split()))

if len(scores) == 0:
    print("No scores entered.")
else:
    total = sum(scores)
    average = total / len(scores)
    maximum = max(scores)
    minimum = min(scores)

    print("Scores:", scores)
    print("Sum:", total)
    print("Average:", average)
    print("Maximum:", maximum)
    print("Minimum:", minimum)
