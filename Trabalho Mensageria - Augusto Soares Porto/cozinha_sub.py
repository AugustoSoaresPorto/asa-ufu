import pika
import os
import sys

def callback(ch, method, properties, body):
    print(f" [x] Cozinha recebeu: {body.decode()}")
    print(" [x] Cozinha está preparando o prato...")
    print(" [x] Prato pronto!")

def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('localhost',
                                        5672,
                                        '/',
                                        credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='queue_pedidos')

    channel.basic_consume(queue='queue_pedidos', on_message_callback=callback, auto_ack=True)

    print(' [*] Cozinha aguardando pedidos. Para sair, pressione CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Programa interrompido')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
