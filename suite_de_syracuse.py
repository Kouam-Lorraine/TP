
def suite_de_syracuse(nombre):
    
    l = [nombre]

    while (l.count(1) != 4) :

        if nombre % 2 == 0:
            nombre = nombre // 2
            l.append(nombre)

        else:
            nombre = (nombre * 3) + 1
            l.append(nombre)

    return l
