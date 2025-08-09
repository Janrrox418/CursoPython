class calculadora:
    
    def __init__(self, numero_a, numero_b):
        self.numero_a = numero_a
        self.numero_b = numero_b
        
    def sumar(self):
        return self.numero_a + self.numero_b
    
    def restar(self):
        return self.numero_a - self.numero_b
    
    def multiplicar(self):
        return self.numero_a * self.numero_b
    
    def dividir(self):
        if self.numero_b==0:
            print("No se puede dividir entre cero, operacion no definida")
        return self.numero_a / self.numero_b
    
    def valor_absoluto(self):
        return abs(self.numero_a), abs(self.numero_b)
    
        