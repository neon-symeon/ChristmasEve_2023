# ------------------------------------------------------------------+
# run this file to get the shopping list with improved food amounts |
# ------------------------------------------------------------------+

from collections import defaultdict
from receipts import przepisy, create_multiplications
from enumerations import products_categories, Acquisition, dont_buy


HOW_MANY_PEOPLE = 12


def create_shopping_list() -> defaultdict:
    _lista_zakupow = list()
    for przepis in przepisy:
        # adds raw product to buy (at the grocery's)
        if przepis['jak'] == Acquisition.WE_MAKE_IT:
            for (what_to_buy, quantity) in przepis['składniki'].items():
                # slices the item
                element = what_to_buy.split('-')
                element[0] = element[0].lower().strip(" ")

                # checks if the item is really to buy
                if element[0] in dont_buy:
                    continue

                # formats and adds category info to the item
                element[1] = element[1].lower().strip(" ")
                element.insert(0, products_categories[element[0]])

                # multiplies the quantities by the dish-multiplication-factor
                quantity *= przepis['mnoznik']

                # and adds to the item to purchase
                element.append(quantity)

                # finally adds the name of the dish to the description of the item
                element.append(przepis['nazwa'])

                # extends the shopping_list by new item
                _lista_zakupow.append(element)

        # adds ready-made product to buy; additional asterisk points to ready-made product
        # and differentiates from raw products (ingredients)
        elif przepis['jak'] == Acquisition.WE_BUY_IT:
            element = ['*' + przepis['źródło'], przepis['nazwa'], przepis['jednostka'], przepis['ile']]
            _lista_zakupow.append(element)

    # sortuje wynik, najpierw po działach w sklepie, potem po produktach
    _lista_zakupow = sorted(_lista_zakupow, key=lambda x: (x[0], x[1]))

    # sums up identical items together to make a comprehensive real-life shopping list
    lista_zakupow = defaultdict(float)
    for item in _lista_zakupow:
        category, product, metric, value, *_ = item
        description = category + '| ' + product + '| ' + metric + ':'
        lista_zakupow[description] += value

    return lista_zakupow


def get_shopping_list(shopping_list_to_print: defaultdict):
    for desc, val in shopping_list_to_print.items():
        print(desc, round(val, 3))


if create_multiplications():
    shopping_list = create_shopping_list()
    get_shopping_list(shopping_list)
else:
    print('pls double check')
