# Programa para valores por default
# Valores opcionales, puenes o no ir

def calculo_isss_afp(sueldo:float, isss:float = 0.03, afp:float = 0.075) -> float:
    '''
    La funcion calculo_isss_afp realiza el calculo del ISSS y AFP a partir del sueldo\n
    El parametro isss es opcional y su valor por default es 3%\n
    El parámetro afp es opcioneal y su valor por default es 7.5%\n
    El valor de retorno es el valor del afp, isss y la suma de Isss y AFP\n
    '''
    desc_afp = sueldo * afp
    if sueldo >= 1000:
        desc_isss = 1000*isss
    else:
        desc_isss = sueldo*isss
    return desc_afp, desc_isss, desc_afp + desc_isss

descuento = calculo_isss_afp(1200)
print(f'Los descuentos son ISSS: {descuento[0]:.2f}, AFP: {descuento[1]:.2f} Total: {descuento[2]:.2f}')

descuento2 = calculo_isss_afp(1200, 0.04)
descuento3 = calculo_isss_afp(1200, 0.04, 0.08)
descuento4 = calculo_isss_afp(1200, afp=0.08)
descuento5 = calculo_isss_afp(1200, isss=0.04)
descuento6 = calculo_isss_afp(sueldo=1200, isss=0.04, afp=0.08)

print(descuento)
print(descuento2)
print(descuento3)
print(descuento4)
print(descuento5)
print(descuento6)