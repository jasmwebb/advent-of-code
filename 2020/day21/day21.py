# https://adventofcode.com/2020/day/21

from collections import Counter, defaultdict


def parse_ingredients(file):
    with open(file, "r") as inputf:
        """Creates the following structures from given input file:
        ingredients = [[ingredient, ...], ...]
        allergen_linked_to = {ingredient: set(possible allergen, ...)}
        foods_containing = {allergen: [index of food in ingredients]}
        """
        ingredients = []
        allergen_linked_to = defaultdict(set)
        foods_containing = defaultdict(list)

        for i, line in enumerate(inputf):
            ing_list, allergens = line.rstrip(")\n").split(" (contains ")
            ing_list = tuple(ing_list.split())
            allergens = set(allergens.split(", "))

            ingredients.append(ing_list)

            for ing in ing_list:
                allergen_linked_to[ing] |= allergens

            for allergen in allergens:
                foods_containing[allergen].append(i)

        return (tuple(ingredients), allergen_linked_to, foods_containing)


def crossref(data_tuple):
    """Cross-references all ingredients with their potential allergens and the
    ingredients lists they appear in to determine if they are hypoallergenic.
    For an ingredient to be confirmed allergenic, it must appear in all
    ingredients lists containing the allergen it is linked to.
    """
    ingredients, allergen_linked_to, foods_containing = data_tuple
    hypo = []

    for ingredient, allergens in allergen_linked_to.items():
        remove = set()

        for allergen in allergens:
            if any(ingredient not in ingredients[i]
                   for i in foods_containing[allergen]):
                remove.add(allergen)

        allergens -= remove

        if not allergens:
            hypo.append(ingredient)

    hypo = tuple(hypo)
    occurences = Counter(ing in ing_l
                         for ing_l in ingredients for ing in hypo)[True]

    return hypo, occurences


if __name__ == "__main__":
    ingredient_data = parse_ingredients("input.txt")

    print("Part 1:", crossref(ingredient_data)[1])  # 2659
