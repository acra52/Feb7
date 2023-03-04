lista_estudiantes = ['David', 'Omar', 'Isaac']
lista_profesores = ['Felipe']
lista_utensilios = ['PC', 'Mouse']

def agregar(
    lista:list,
    lista2:list
) -> list: 
    estudiante= lista+lista2
    print(estudiante)
    
#agregar(lista_profesores,lista_utensilios)


def agregarvlrdefecto(
    lista:list,
    lista2:list,
    elemento = 'hola'
) -> list: 
    estudiante = lista + lista2
    estudiante.append(elemento)
    print(estudiante)
    
agregarvlrdefecto(lista_profesores,lista_utensilios)