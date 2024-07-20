class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __del__(self):
        print(f"El producto '{self.nombre}' ha sido eliminado.")

# Ejemplo de uso
producto1 = Producto("Camiseta", 20.00, 10)
print(producto1.nombre, producto1.precio, producto1.stock)

# Eliminación del objeto
del producto1