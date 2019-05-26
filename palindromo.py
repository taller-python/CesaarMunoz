""" probar palindromo """
PALABRA = input('Ingrese una palabra: ')
ES_PAL = 'SI'
for i, letra in enumerate(PALABRA):
    if letra != PALABRA[len(PALABRA)-i-1]:
        ES_PAL = 'NO'
print('La palabra "' + PALABRA +'" '+ ES_PAL + ' es palindroma')
