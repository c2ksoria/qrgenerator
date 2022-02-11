# Importamos la biblioteca
from email import message
from email.mime import base
import qrcode
import base64
import random

url="http://192.168.1.232:5000/"
# Creamos el código QR y entre comillas simples escribimos la cadena que se va a codificar, en este caso usamos la dirección de nuestro blog
#url="http://ec2-177-71-171-90.sa-east-1.compute.amazonaws.com:5000/"

#articulo=list(range(10,20))
articulo=[]
for i in range(0,50):
	n=random.randint(0, 1000)
	articulo.append(n)

#print(articulo)

for item in articulo:
    codigoRaw="{"+f'"codigo":{item}'+"}"
    print(codigoRaw)
    message_bytes=codigoRaw.encode("utf-8")
    print(message_bytes)
    base64_bytes=base64.urlsafe_b64encode(codigoRaw)
    print(base64_bytes)
    base64_message = base64_bytes.decode("ascii")
    print(base64_message)
    text=f'{url}'+base64_message
    print(text)
    img = qrcode.make(text)
    img.save(f'{item}.png')


