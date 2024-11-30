class Ticket:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.mesas = []

    def añadir_mesa(self, mesa):
        self.mesas.append(mesa)
        print(f"mesa {mesa.numero} adicionada al tickete {self.nombre}.")

    def eliminar_mesa(self, mesa):
        self.mesas.remove(mesa)
        print(f"mesa {mesa.numero} eliminar del tickete {self.nombre}.")

    def buscar_mesa(self, tipo=None, precio_max=None):
        resultados = []
        for mesa in self.mesas:
            if (tipo is None or mesa.tipo == tipo) and (precio_max is None or mesa.precio <= precio_max):
                resultados.append(mesa)
        return resultados
    
    def mostrar_info(self):
        return f"Ticket {self.nombre}, Ubicado en {self.ubicacion}"
    
class Mesa:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def actualizar_disponibilidad(self, disponible):
        self.disponible = disponible
        estado = "disponible" if disponible else "no disponible"
        print(f"mesa {self.numero} ahora esta {estado}")

    def mostrar_info(self):
        return f"Mesa {self.numero}, tipo: {self.tipo}, Precio: {self.precio} por usar"
    
        
class Reserva:
    def __init__(self, id_reserva, mesa, cliente, fecha):
        self.id_reserva = id_reserva
        self.mesa = mesa
        self.cliente = cliente
        self.fecha = fecha
#        self.fecha_entrada = fecha_entrada
#        self.fecha_salida = fecha_salida
        self.estado = "pendiente"

#    def modificar_reserva(self, nueva_fecha_entrada, nueva_fecha_salida):
    def modificar_reserva(self, nueva_fecha):
        self.fecha = nueva_fecha
 #       self.fecha_entrada = nueva_fecha_entrada
 #       self.fecha_salida = nueva_fecha_salida
 #       print(f"""Reserva {self.id_reserva} modificada para el perÃ­odo {self.fecha_entrada} a
 #       {self.fecha_salida}.""")
        print(f"""Reserva {self.id_reserva} modificada para la fecha {self.fecha}.""")

    def cancelar_reserva(self):
        self.estado = "cancelada"
        print(f"Reserva {self.id_reserva} cancelada.")


class Cliente:
    def __init__(self, id_cliente, nombre, email):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.reservas = []

    def realizar_reserva(self, reserva):
        self.reservas.append(reserva)
        reserva.estado = "confirmada"
        print(f"""Reserva {reserva.id_reserva} realizada por {self.nombre} para la mesa
                {reserva.mesa.numero}.""")

    def cancelar_reserva(self, reserva):
        if reserva in self.reservas:
            reserva.cancelar_reserva()
            self.reservas.remove(reserva)


class SistemaReservas:
    def __init__ (self):
        self.tickets = []
        self.clientes = []

    def registrar_ticket(self, ticket):
        self.tickets.append(ticket)
        print(f"Ticket {ticket.nombre} registrado en el sistema.")

    def eliminar_ticket(self, ticket):
        self.tickets.remove(ticket)
        print(f"Ticket {ticket.nombre} eliminado del sistema.")

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nombre} registrado en el sistema.")

    def eliminar_cliente(self, cliente):
        self.clientes.remove(cliente)
        print(f"Cliente {cliente.nombre} eliminado del sistema.")

    def buscar_ticket(self, ubicacion=None, nombre=None):
        resultados = []
        for ticket in self.tickets:
            if (ubicacion is None or ticket.ubicacion == ubicacion)and (nombre is None or ticket.nombre == nombre):
                resultados.append(ticket)
        return resultados

def listar_reservas(self):
    for cliente in self.cliente:
        for reserva in cliente.reservas:
            print(f"""Reserva {reserva.id_reserva}, para el cliente{cliente.nombre}, para la fecha    Estado: {reserva.estado}.""" )   
    


        