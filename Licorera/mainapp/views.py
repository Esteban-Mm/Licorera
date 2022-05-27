from django.shortcuts import render, redirect, HttpResponse
from mainapp.models import Producto, Venta
from mainapp.forms import FormVenta
from django.contrib import messages
from random import random, randrange, choice

import smtplib
from email.message import EmailMessage 

# Create your views here.

def index(request):
    productos = Producto.objects.all()
    
    return render(request, 'mainapp/index.html',{
        'title': 'Inicio',
        'productos': productos
    })

def cerveza(request):

    productos = Producto.objects.filter(type="Cerveza")

    return render(request, 'mainapp/cerveza.html',{
        'title': 'Cervezas',
        'productos': productos
    })

def ron(request):

    productos = Producto.objects.filter(type="Ron")

    return render(request, 'mainapp/ron.html',{
        'title': 'Ron',
        'productos': productos
    })

def tekila(request):

    productos = Producto.objects.filter(type="Tekila")

    return render(request, 'mainapp/tekila.html',{
        'title': 'Tekila',
        'productos': productos
    })

def whiskey(request):

    productos = Producto.objects.filter(type="Whiskey")

    return render(request, 'mainapp/whiskey.html',{
        'title': 'Whiskey',
        'productos': productos
    })  

def about(request):

    return render(request, 'mainapp/about.html',{
        'title': 'Informacion'
    })

def pedido(request, id):

    if request.method == 'POST':
        
        formulario = FormVenta(request.POST)

        if formulario.is_valid():

            data_form = formulario.cleaned_data

            names = data_form.get('names')
            direction = data_form['direction']
            email = data_form['email']
            mobile = data_form['mobil']
            unit = data_form['unit']

            venta = Venta(
                names = names,
                direction = direction,
                email = email,
                mobile = mobile,
                unit = unit
            )
            
            msj = f"Pedido Realizado con exito, para {names}. Te llegara pronto a la direccion:{direction}"

            if email != "":
                email_subject = "Licorera Pascualina 24/7" 
                sender_email_address = "elmer.munoz171@pascualbravo.edu.co" 
                receiver_email_address = email, sender_email_address 
                email_smtp = "smtp.gmail.com" 
                email_password = "1152448171" 

                # Create an email message object 
                message = EmailMessage() 

                # Configure email headers 
                message['Subject'] = email_subject 
                message['From'] = sender_email_address 
                message['To'] = receiver_email_address 

                # Set email body text 
                message.set_content(msj)

                # Set smtp server and port 
                server = smtplib.SMTP(email_smtp, '587') 

                # Identify this client to the SMTP server 
                server.ehlo() 

                # Secure the SMTP connection 
                server.starttls() 

                # Login to email account 
                server.login(sender_email_address, email_password) 

                # Send email 
                server.send_message(message) 

                # Close connection to server 
                server.quit()
                venta.save()

                if request.method == 'POST':
                    vendidos = int(request.POST.get('unit'))
                    producto = Producto.objects.get(id=id)
                    cantidad = producto.stok
                    precio = producto.price
                    if vendidos <= cantidad:
                        Producto.objects.filter(id=id).update(stok=cantidad-vendidos)
                        messages.success(request, f'{venta.names} Tu pedido llegara pronto a la direccion: {venta.direction}')
                        return redirect('inicio')
                    else:
                        messages.success(request, 'Error: No existe la cantidad que quieres comprar')
                        return redirect(f'/pedido/{id}')
                else:
                    return redirect(f'/pedido/{id}')
    else:
        producto = Producto.objects.get(id=id)
        formulario = FormVenta()

    return render(request, 'mainapp/pedido.html',{
        'title': 'Formulario',
        'producto': producto,
        'form': formulario
    })


def admin():
    email_subject = "Licorera Pascualina 24/7" 
    sender_email_address = "elmer.munoz171@pascualbravo.edu.co" 
    receiver_email_address = "elmer.munoz171@pascualbravo.edu.co", sender_email_address 
    email_smtp = "smtp.gmail.com" 
    email_password = "1152448171" 

    # Create an email message object 
    message = EmailMessage() 

    # Configure email headers 
    message['Subject'] = email_subject 
    message['From'] = sender_email_address 
    message['To'] = receiver_email_address 

    # Set email body text 
    message.set_content(msj)

    # Set smtp server and port 
    server = smtplib.SMTP(email_smtp, '587') 

    # Identify this client to the SMTP server 
    server.ehlo() 

    # Secure the SMTP connection 
    server.starttls() 

    # Login to email account 
    server.login(sender_email_address, email_password) 

    # Send email 
    server.send_message(message) 

    # Close connection to server 
    server.quit()
