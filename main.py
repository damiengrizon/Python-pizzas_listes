# def tri_personnalise(e):
# return len(e)


# def afficher(collection, pizza_list=99):
#     # collection.sort(reverser=True, key=tri_personnalise)
#     nb_pizza = len(collection)
#     if nb_pizza == 0:
#         print("AUCUNE PIZZA")
#     else:
#         derniere_pizza = collection[-1]
#         premiere_pizza = collection[0]
#         print(f"----- LISTE DES PIZZAS ({nb_pizza}) -----")
#         if pizza_list == 99:
#             for i in collection:
#                 print(i)
#         else:
#             for i in range(0, pizza_list):
#                 print(collection[i])
#         print()
#         print(f"Première pizza : {premiere_pizza}")
#         print(f"Dernière pizza : {derniere_pizza}")

def afficher(collection, pizza_list=-1):
    c = collection
    if not pizza_list == -1:
        c = collection[:pizza_list]

    nb_pizza = len(c)
    if nb_pizza == 0:
        print("AUCUNE PIZZA")
    else:
        derniere_pizza = c[-1]
        premiere_pizza = c[0]
        print(f"----- LISTE DES PIZZAS ({nb_pizza}) -----")
        for i in c:
            print(i)
        print()
        print(f"Première pizza : {premiere_pizza}")
        print(f"Dernière pizza : {derniere_pizza}")


def ajouter_pizza_utilisateur(collection):
    item = input("Pizza que vous souhaitez ajouter : ")
    if item.lower() in collection:
        print("ERREUR : la pizza existe déjà!!")
    else:
        collection.append(item)

#
# def pizza_existe(item, collection):
#     for i in collection:
#         if i == item:
#             return True


pizzas = ["4 fromages", "végétarienne", "hawai", "calzone"]


# vide = ()
ajouter_pizza_utilisateur(pizzas)
afficher(pizzas)
# afficher(vide)
