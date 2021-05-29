def math():
    print("input numerator")
    numerator = int(input())
    print("input denominator")
    denominator = int(input())
    answer = numerator / denominator
    print(answer)
    print("press 'y' for another question")
    another_question = input()
    if another_question == "y":
        math()


math()
