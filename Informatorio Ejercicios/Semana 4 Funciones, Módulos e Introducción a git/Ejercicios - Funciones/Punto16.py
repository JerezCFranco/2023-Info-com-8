# -Crea una función llamada eliminar_duplicados que tome una lista como
# parámetro y devuelva una nueva lista sin duplicados, conservando el orden
# original.

def eliminarDuplicados(lista):
    lista=list(set(lista))
    return(lista)

lista=[1,1,1,2,3,5,8,9,1,5,7,7,4,2,3,4,5,8,7]
print(f"La lista original es {lista}.")
print(f"La lista sin duplicados es {eliminarDuplicados(lista)}.")
