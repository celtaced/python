# programa para paso por valor/referencias

# paso de copia (valor) inmutables
y = 2
def modificar_variable(x):
    x+=20
    return x

print(modificar_variable(y))
print(y)

# paso por referencia (direccion) mutables
v = [1,3,7]
def modificar_vector(z):
    z.append(9)
    return z

print(modificar_vector(v))
print(v)