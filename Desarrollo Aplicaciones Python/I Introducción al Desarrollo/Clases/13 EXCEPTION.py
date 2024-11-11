def main():
    # try:
    #     input('digite una palabra')
    # except:
    #     print('terminando programa...')
    #     exit()
    # print('continua el programa')
    
    # try:
    #     4/0
    # except Exception as e:
    #     print('ocurrio un error', e)
    input('digite una palabra')
    
if __name__=='__main__':
    try:
        4/0
        #'hola' + 5
        main()
    except KeyboardInterrupt as e:
        print('saliendo...')
        exit()
    except ZeroDivisionError as e:
        print('Error: division entre cero', e)
    except TypeError as e:
        print('error de tipos', e)
    else:
        print('no hubo errores')
    finally:
        print('se ejecuta siempre, hayan o no errores')

    suma = 6+4
    print('la suma es:', suma)