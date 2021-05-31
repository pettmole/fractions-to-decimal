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
    else:
        print("wrong button(s) but don't worry! i'll help")
        math()


math()
