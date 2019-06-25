class compuerta():
    # Initializer / Instance Attributes
    def __init__(self, valor_a, valor_b):
        self.valor_a = valor_a
        self.valor_b = valor_b

class compuerta_AND(compuerta):
    # metodo de la compuerta and
    def salida(self):
        return "{} AND {} = {}".format(self.valor_a, self.valor_b, self.valor_a and self.valor_b)

class compuerta_OR(compuerta):
    # metodo de la compuerta or
    def salida(self):
        return "{} OR  {} = {}".format(self.valor_a, self.valor_b, self.valor_a or self.valor_b)

# instancia
micompuertaand = compuerta_AND(0,0)
micompuertaor = compuerta_OR(0,0)
# visualizar ejemplo
print('Simple sample')
print(micompuertaand.salida())
print(micompuertaor.salida())
# loop para visualizar toda la tabla
booleans = [0,1]
print('*************')
print("* AND Table *")
for x in booleans:
    for y in booleans:
        micompuertaand.valor_a = x
        micompuertaand.valor_b = y
        print(micompuertaand.salida())
print('**************')
print("** OR Table **")
for x in booleans:
    for y in booleans:
        micompuertaor.valor_a = x
        micompuertaor.valor_b = y
        print(micompuertaor.salida())
print('**************')
