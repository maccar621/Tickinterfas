from flask import Flask, render_template, request, redirect, url_for
from reservas import Ticket, Mesa, Cliente, SistemaReservas, Reserva

app = Flask(__name__)

sistema = SistemaReservas()
#ticket1 = Ticket(nombre="ticket A", ubicacion="Ciudad A")
#sistema.registrar_ticket(ticket1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tickets')
def mostrar_tickets():
    return render_template(template_name_or_list='tickets.html', tickets=sistema.tickets)

@app.route(rule='/agregar_ticket', methods=['POST'])
def agregar_ticket():
    nombre = request.form['nombre']
    ubicacion = request.form['ubicacion']
    if nombre and ubicacion:
        nuevo_ticket = Ticket(nombre, ubicacion)
        sistema.registrar_ticket(nuevo_ticket)
    return redirect(url_for('mostrar_tickets'))

@app.route('/eliminar_ticket/<int:index>')
def eliminar_ticket(index):
    if 0 <= index < len(sistema.tickets):
        ticket = sistema.tickets[index]
        sistema.eliminar_ticket(ticket)
    return redirect(url_for('mostrar_tickets'))

@app.route('/mesas')
def mostrar_mesas():
    mesas = []
    for ticket in sistema.tickets:
        mesas.extend(ticket.mesas)
    return render_template(template_name_or_list='mesas.html', tickets=sistema.tickets, mesas=mesas)

@app.route(rule='/agregar_mesa', methods=['POST'])
def agregar_mesa():
    ticket_nombre = request.form['ticket']
    numero = int(request.form['numero'])
    tipo = request.form['tipo']
    precio = request.form['precio']
    if ticket_nombre and numero and tipo and precio:
        ticket = next((t for t in sistema.tickets if t.nombre == ticket_nombre), None)
        if ticket:
            nueva_mesa = Mesa(numero, tipo, float(precio))
            ticket.añadir_mesa(nueva_mesa)    
    return redirect(url_for('mostrar_mesas'))

@app.route('/eliminar_mesa/<int:index>')
def eliminar_mesa(index):
    mesas= []
    for ticket in sistema.tickets:
        mesas.extend(ticket.mesas) 
    if 0 <= index < len(mesas):
        mesa = mesas[index]
        for ticket in sistema.tickets:
            if mesa in ticket.mesas:
                ticket.eliminar_mesa(mesa)
                break
    return redirect(url_for('mostrar_mesas'))

@app.route('/clientes')
def mostrar_clientes():
    return render_template(template_name_or_list='clientes.html', clientes=sistema.clientes)

@app.route(rule='/agregar_cliente', methods=['POST'])
def agregar_cliente():
    nombre = request.form['nombre']
    email = request.form['email']
    if nombre and email:
        nuevo_cliente = Cliente(len(sistema.clientes) + 1, nombre, email)
        sistema.registrar_cliente(nuevo_cliente)
    return redirect(url_for('mostrar_clientes'))

@app.route('/reservas')
def mostrar_reservas():
    reservas = []
    for cliente in sistema.clientes:
        reservas.extend(cliente.reservas)
    return render_template( template_name_or_list='reservas.html', reservas=reservas, mesas=[mes for ticket in sistema.tickets for mes in ticket.mesas], clientes=sistema.clientes)

@app.route(rule='/agregar_reserva', methods=['POST'])
def agregar_reserva():
    mesa_numero = int(request.form['mesa'])
    cliente_nombre = request.form['cliente']
    fecha = request.form['fecha']
    if mesa_numero and cliente_nombre and fecha:
        mesa = None
        for ticket in sistema.tickets:
            for mes in ticket.mesas:
                if mes.numero == int(mesa_numero):
                    mesa = mes
                    break
        cliente = next((c for c in sistema.clientes if c.nombre == cliente_nombre), None)
        if mesa and cliente:
            nueva_reserva = Reserva(len(cliente.reservas) + 1, mesa, cliente, fecha)
            cliente.realizar_reserva(nueva_reserva)
    return redirect(url_for('mostrar_reservas'))

@app.route('/eliminar_reserva/<int:index>')
def eliminar_reserva(index):
    reservas = []
    for cliente in sistema.clientes:
        reservas.extend(cliente.reservas)
    if 0 <= index < len(reservas):
        reserva = reservas[index]
        cliente = reserva.cliente
        cliente.cancelar_reserva(reserva)
    return redirect(url_for('mostrar_reservas'))

if __name__ == '__main__':
    app.run(debug=True)