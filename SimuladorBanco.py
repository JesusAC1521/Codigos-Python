from os import  system


fuera_codigo = False
opcion_cliete = 'a'
dinero_operacion = 0



class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apelido = apellido

class Cliente(Persona):
    def __init__(self,nombre, apellido, numero_cuenta, balance):
        super().__init__( nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"El cliente {self.nombre} {self.apelido} con numero de cuenta: {self.numero_cuenta} tiene {self.balance} pesos en su cuenta de banco"

    def depositar(self, cantidad):
        self.balance += cantidad
        print(f"Se ha ingresado {cantidad} pesos a tu cuenta, tu saldo nuevo es de {self.balance}")

    def retirar(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Se ha retirado {cantidad} quedan {self.balance} pesos en tu cuenta")
        else:
            print("No cuentas con el dinero suficiente para retirar tal cantidad")

def crea_objeto():
    nombre_cliente = input("Como te llamas?: ")
    apellido_cliente = input("Cual es tu apellido?: ")
    numero_cu = int(input("Cual es tu numero de cuenta?: "))
    dinero = int(input("Cuanto dinero tienes en tu cuenta?: "))
    system('cls')
    return Cliente(nombre_cliente, apellido_cliente, numero_cu, dinero)

def espera():
    esperar = 'x'
    while esperar not in 'c':
        esperar = input('\nPresiona [C] para continuar').lower()
    system('cls')

mi_cliente = crea_objeto()

while not fuera_codigo:
    print('*'*50 + '\n')
    print(mi_cliente)
    print('\n' + '*' * 50 + '\n')
    opcion_cliete = 'x'
    while opcion_cliete not in 'rds':
        opcion_cliete = input("Introduce la operacion que deseas realizar:\n[R] Retirar\n[D] Depositar\n[S] Salir \n").lower()
    match opcion_cliete:
        case 'r':
            dinero_operacion = int(input("Ingresa la cantidad que vas a retirar: "))
            mi_cliente.retirar(dinero_operacion)
            espera()
        case 'd':
            dinero_operacion = int(input("Ingresa la cantidad que vas a depositar: "))
            mi_cliente.depositar(dinero_operacion)
            espera()
        case 's':
            fuera_codigo = True
