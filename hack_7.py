"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    contador = 5
    result = []
    while (contador >= 0):
        result.append(contador)
        contador = contador - 1
    return result

salida= fn_hack_7()
print(salida)