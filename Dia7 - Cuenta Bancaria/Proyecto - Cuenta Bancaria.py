class Persona:
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido
        
class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido} \n- Cuenta: {self.numero_cuenta} - Balance: ${self.balance}"
    
    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print(f"Deposito de ${monto_deposito} exitoso!")
        
    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print(f"Retiro de ${monto_retiro} exitoso!")
        else:
            print("Fondos insuficientes!")
            
def crear_cliente():
    print("Ingrese el nombre del cliente: ")
    nombre = input()
    print("Ingrese el apellido del cliente: ")
    apellido = input()
    print("Ingrese el numero de cuenta del cliente: ")
    numero_cuenta = input()
    
    return Cliente(nombre, apellido, numero_cuenta)

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0
    
    while opcion != 'S':
        print('Elije: D - Depositar R, - Retirar, o S - Salir')
        opcion = input()
        
        if opcion == 'D':
            print("Ingrese el monto a depositar: ")
            monto_deposito = int(input())
            mi_cliente.depositar(monto_deposito)
        elif opcion == 'R':
            print("Ingrese el monto a retirar: ")
            monto_retiro = int(input())
            mi_cliente.retirar(monto_retiro)
        print(mi_cliente)
    
    print("Gracias por usar nuestros servicios!")

inicio()