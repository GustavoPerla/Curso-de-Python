# Manejo de tuplas

nombres=("juan","laura","Pepe") ##usa parentesis en ves de corchetes // son opcionales

#Tupla heterogenea

nombres_heterogeneos = 100,"juan",56.2

print(nombres_heterogeneos)

#Recorrer los elementos

for nom in nombres:
    print(nom,end=" ")
print()

## la palabr "pass" hace que un ciclo no tenga codigo dentro