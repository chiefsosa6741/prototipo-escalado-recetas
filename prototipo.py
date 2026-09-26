a=int(input("inserte la cantidad del ingrediente que viene en la receta:  "))
b=int(input("inserte la cantidad de personas para la que es la receta:  "))
c=int(input("inserte la cantidad de personas para la que quiere adaptar la receta:  "))

d=(a*c)/b

res=f"la cantidad de ese ingrediente para la receta es: {d}"

print(res)