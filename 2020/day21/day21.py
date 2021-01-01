# https://adventofcode.com/2020/day/21

from collections import Counter, defaultdict


def parse_ingredients(file):
    with open(file, "r") as inputf:
        """Creates the following structures from given input file:
        ingredients = [[ingredient, ...], ...]
        allergens_in = {ingredient: set(possible allergen, ...)}
        foods_containing = {allergen: [index of food in ingredients]}
        """
        ingredients = []
        allergens_in = defaultdict(set)
        foods_containing = defaultdict(list)

        for i, line in enumerate(inputf):
            ing_list, allergens = line.rstrip(")\n").split(" (contains ")
            ing_list = tuple(ing_list.split())
            allergens = set(allergens.split(", "))

            ingredients.append(ing_list)

            for ing in ing_list:
                allergens_in[ing] |= allergens

            for allergen in allergens:
                foods_containing[allergen].append(i)

        return (tuple(ingredients), allergens_in, foods_containing)


def determine_safe(data_tuple):
    """Cross-references all ingredients with their potential allergens and the
    ingredients lists they appear in to determine if they are hypoallergenic.
    For an ingredient to be confirmed allergenic, it must appear in all
    ingredients lists containing the allergen it is linked to.
    """
    ingredients, allergens_in, foods_containing = data_tuple
    hypo = []

    for ingredient, allergens in allergens_in.items():
        remove = set()

        for allergen in allergens:
            if any(ingredient not in ingredients[i]
                   for i in foods_containing[allergen]):
                remove.add(allergen)

        allergens -= remove

        if not allergens:
            hypo.append(ingredient)

    hypo = set(hypo)
    occurences = Counter(ing in ing_l
                         for ing_l in ingredients for ing in hypo)[True]

    return occurences, allergens_in


def determine_allergens(updated_data):
    """Cross-reference all unsafe ingredients and determine their allergens.
    """
    unsafe = {ing: alls for ing, alls in updated_data.items() if len(alls)}
    len_unsafe = len(unsafe)
    canon = {}

    while len(canon) != len_unsafe:
        for ingredient, allergens in tuple(unsafe.items()):
            if len(allergens) == 1:
                canon[ingredient] = str(*allergens)

                del unsafe[ingredient]

                for ing in unsafe:
                    unsafe[ing] -= allergens

    return ",".join(sorted(canon, key=canon.get))


if __name__ == "__main__":
    ingredient_data = parse_ingredients("input.txt")
    occurences, updated_ings = determine_safe(ingredient_data)
    unsafe = determine_allergens(updated_ings)

    print("Part 1:", occurences)  # 2659
    print("Part 2:", unsafe)  # rcqb,cltx,nrl,qjvvcvz,tsqpn,xhnk,tfqsb,zqzmzl
