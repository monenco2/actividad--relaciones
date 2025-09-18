from django.test import TestCase

# Create your tests here.


from ventas.models import Cliente, Producto, Pedido, DetallePedido

# Crear un cliente
cliente = Cliente.objects.create(nombre="Juan Pérez", email="juan@test.com", telefono="123456")

# Crear productos
p1 = Producto.objects.create(nombre="Laptop", descripcion="Laptop gamer", precio=2500, stock=5)
p2 = Producto.objects.create(nombre="Mouse", descripcion="Mouse inalámbrico", precio=50, stock=20)

# Crear pedido
pedido = Pedido.objects.create(cliente=cliente)

# Agregar detalles al pedido
DetallePedido.objects.create(pedido=pedido, producto=p1, cantidad=1, precio_unitario=p1.precio)
DetallePedido.objects.create(pedido=pedido, producto=p2, cantidad=2, precio_unitario=p2.precio)

# Calcular total
pedido.calcular_total()

print(f"Total del pedido {pedido.id}: {pedido.total}")
