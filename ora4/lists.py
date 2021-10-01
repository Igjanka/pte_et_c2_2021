my_list=[1,2.5,"alma",False]
print("A lista hossza:",len(my_list))
print("A len() függvény visszatérési értékének típusa:", type(len(my_list)))

print("A lista tartalmazza a 2.5 értéket:", 2.5 in my_list)
print(" Az in operátor eredményének típusa:", type(2.5 in my_list))

print("A lista tartalmazza a 2.5 értéket:", 2 in my_list)
print(" Az in operátor eredményének típusa:", type(2 in my_list))

print("A 2.5 érték pozíciója a listában:", my_list.index(2.5))
print("Az index() metódus visszatérési értékének típusa:", type(my_list.index(2.5)))

