ISSS = 0.03
AFP = 0.0725

def isss(sueldo):
    if sueldo>=1000:
        return 1000 * ISSS
    else:
        return sueldo * ISSS

def afp(sueldo):
    return sueldo * AFP

def sueldo_gravable(sueldo):
    return sueldo - isss(sueldo) - afp(sueldo)

def isr(sueldo):
    sg = sueldo_gravable(sueldo)
    if sg >0.01 and sg <= 472.00:
        return 0
    elif sg >= 472.01 and sg <= 895.24:
        return (sg - 472.00)*0.1 + 17.67
    elif sg >= 895.25 and sg <= 2038.10:
        return (sg - 895.24)*0.2 + 60
    elif sg >= 2038.11:
        return (sg - 2038.10)*0.3 + 288.57

def descuentos(sueldo):
    return isss(sueldo) + afp(sueldo) + isr(sueldo)

def sueldo_a_pagar(sueldo):
    return sueldo - descuentos(sueldo) 