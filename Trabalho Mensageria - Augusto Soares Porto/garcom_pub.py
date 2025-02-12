import pika
import json
import time

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost',
                                5672,
                                '/',
                                credentials)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue='queue_pedidos')

def anotar_pedido(pedido_id, prato, unidades_pedido):
    pedido = {"id": pedido_id, "prato": prato, "quantidade" : unidades_pedido}
    return pedido

pedido_id = 1

while True:
    prato = input("Garçom: -- Informe o nome do prato pedido: ")
    unidades_pedido = int(input("Garçom: -- Informe a quantidade de pratos pedidos: "))
    pedido = anotar_pedido(pedido_id, prato, unidades_pedido)
    
    channel.basic_publish(exchange='', routing_key='queue_pedidos', body=json.dumps(pedido).encode())
    print(f"Garçom: Pedido {pedido_id} enviado para a queue_pedidos: {pedido['prato']}")
    
    pedido_id += 1
    time.sleep(2)

connection.close()
