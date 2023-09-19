import random

def crear_c():
    chars = 'abcdefghijklmnopqrstuvwxyz123456789/*-+#$%&'
    clave = ''

    for x in range(16):
        clave += random.choice(chars)
    
    print(f'clave: {clave}')
    return clave

if __name__=='__main__':
    crear_c()
