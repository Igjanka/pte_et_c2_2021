villanyora = 25 # A
hal_f = 230 # V
telj = villanyora * hal_f
izzo = 30 # W
klima = 1500 # W
mosogep = 1200 # W
print(telj)
all = 5 * izzo + klima + mosogep
print(all)
vasalo = 2000 # W
if all + vasalo < telj:
    print("nem kapcsol le a megszakító")