# Tarea: Calculadora de Renta y Préstaciones

# Parámetros
isss_techo_monto = 1000.00
isss_techo_valor = 30.00
isss_porcentaje = 0.03
afp_porcentaje = 0.0725
isr_tramo01_monto_min = 0.01
isr_tramo01_monto_max = 472.00
isr_tramo02_monto_min = 472.01
isr_tramo02_monto_max = 895.24
isr_tramo02_porcentaje = 0.1
isr_tramo02_cuota = 17.67
isr_tramo03_monto_min = 895.25
isr_tramo03_monto_max = 2038.10
isr_tramo03_porcentaje = 0.2
isr_tramo03_cuota = 60.00
isr_tramo04_monto_min = 2038.11
isr_tramo04_porcentaje = 0.3
isr_tramo04_cuota = 288.57


mensaje_introductorio = '\n***********************************\n'
mensaje_introductorio += '*   CALCULO DE ISR Y PRESTACIONES  \n'
mensaje_introductorio += '*          by Carlos Dubón         \n'
mensaje_introductorio += '***********************************\n'
print(mensaje_introductorio)

salario = float(input('Ingresa tu salario: $'))

# Calculo AFP
valor_afp = salario * afp_porcentaje

# Calculo de ISSS
if salario <= isss_techo_monto:
    valor_isss =  salario * isss_porcentaje
else:
    valor_isss = isss_techo_valor

# Salario gravable
salario_gravable = salario - (valor_afp + valor_isss) 

# Calculo Impuesto
if salario_gravable <= isr_tramo01_monto_max:
    valor_isr = 0
elif salario_gravable <= isr_tramo02_monto_max:
    valor_isr = isr_tramo02_cuota + ((salario_gravable - isr_tramo01_monto_max) * isr_tramo02_porcentaje)
elif salario_gravable < isr_tramo03_monto_max:
    valor_isr = isr_tramo03_cuota + ((salario_gravable - isr_tramo02_monto_max) * isr_tramo03_porcentaje)
else:
    valor_isr = isr_tramo04_cuota + ((salario_gravable - isr_tramo03_monto_max) * isr_tramo03_porcentaje)

print('\n\nCALCULO:')
print(f'Ingresos:')
print('El salario ingresado es : ${:.2f}'.format(salario))
print('El salario gravable es  : ${:.2f}'.format(salario_gravable))

print(f'\nDeducciones:')
print('- Seguro Social         : ${:.2f}'.format(valor_isss))
print('- AFP                   : ${:.2f}'.format(valor_afp))
print('- ISR                   : ${:.2f}'.format(valor_isr))
print('---------------------------------')
print('Monto Pagado            : ${:.2f}'.format(salario - valor_isss - valor_afp - valor_isr))

print('\n')