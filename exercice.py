#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        values = [input("Element : ") for i in range(10)]
        l2 = []
        for e in values:
            if(e.isnumeric()):
                l2.append(int(e))
            if(e.isdecimal()):
                l2.append(float(e))
            else:
                l2.append(e)

        return l2.sort()
    return sorted(values)


def anagrams(words: list = None) -> bool:
    if words is None:
        words = [input("Element : ") for i in range(2)]
        pass
    dict1 = {}
    for c in words[0]:
        if(c in dict1.keys()):
            dict1[c] += 1
        else :
            dict1[c] = 1
    
    dict2 = {}
    for c in words[1]:
        if(c in dict2.keys()):
            dict2[c] += 1
        else :
            dict2[c] = 1

    return dict2==dict1


def contains_doubles(items: list) -> bool:
    return len(items) != len(set(items))



def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    maxname = list(student_grades.keys())[0]
    for name, grades in student_grades.items():
        if(sum(grades)/len(grades) >= sum(student_grades[maxname])/len(student_grades[maxname])) : 
            maxname = name
    return {maxname: sum(student_grades[maxname])/len(student_grades[maxname])}


def frequence(sentence: str) -> dict:
    dict1 = {}
    for c in sentence:
        if(c in dict1.keys()):
            dict1[c] += 1
        else :
            dict1[c] = 1
    chars = dict1.keys()
    res = sorted(chars, key = lambda ele: dict1[ele])
    for i in range(5):
        print(res[i])

    return dict1


def get_recipes():
    recette = input("nom de la recette :")
    dict1 = {recette: []}
    ingredient = input("ingrédiant (\"None pour finir la saisie\"):")
    while ingredient != "None":
        dict1[recette].append(ingredient)
        ingredient = input("ingrédiant (\"None pour finir la saisie\"):")
    
    return dict1


def print_recipe(ingredients) -> None:
    [print(ingredient) for ingredient in ingredients[input("nom de la recette :")]]


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
