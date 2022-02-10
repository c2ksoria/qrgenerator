# Importamos la biblioteca
from email import message
from email.mime import base
import qrcode
import base64

url="http://192.168.1.232:5000/"
# Creamos el código QR y entre comillas simples escribimos la cadena que se va a codificar, en este caso usamos la dirección de nuestro blog

articulo=list(range(10,20))

for item in articulo:
    codigoRaw="{"+f'"codigo":{item}'+"}"
    print(codigoRaw)
    message_bytes=codigoRaw.encode('ascii')
    base64_bytes=base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    text=f'{url}'+base64_message
    print(text)
    img = qrcode.make(text)
    img.save(f'{item}.png')


