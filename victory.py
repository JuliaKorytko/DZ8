"""МОДУЛЬ 6"""

# Викторина по датам рождения знаменитых людей

while True:
    score_a = 0
    score_b = 0
    daVinchibornyear = int(input("В каком году родился Леонардо да Винчи? ")) # 1452
    if daVinchibornyear == 1452:
        score_a += 1
    if daVinchibornyear != 1452:
        score_b += 1
    Einsteinbornyear = int(input("В каком году родился Альберт Эйнштейн? ")) # 1879
    if Einsteinbornyear == 1879:
        score_a += 1
    if Einsteinbornyear != 1879:
        score_b += 1
    Teslabornyear = int(input("В каком году родился Никола Тесла? ")) # 1856
    if Teslabornyear == 1856:
        score_a += 1
    if Teslabornyear != 1856:
        score_b += 1
    Zellebornyear = int(input("В каком году родилась Маргарета Гертруда Зелле? ")) # 1876
    if Zellebornyear == 1876:
        score_a += 1
    if Zellebornyear != 1876:
        score_b += 1
    Theronbornyear = int(input("В каком году родилась Шарлиз Терон? ")) # 1975
    if Theronbornyear == 1975:
        score_a += 1
    if Theronbornyear != 1975:
        score_b += 1

    print("Вы ответили правильно на %s вопроса(-ов)" %score_a)
    print("Вы ответили неправильно на %s вопроса(-ов)" %score_b)
    print ("Процент правильных ответов:", score_a*100/5,"%")
    print ("Процент неправильных ответов:", score_b*100/5,"%" )

    question_about_quiz = str(input("Хотите ли вы начать игру сначала? "))
    if question_about_quiz == "нет":
        break
    if question_about_quiz == "да":
        continue
print("end")





