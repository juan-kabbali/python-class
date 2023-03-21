import time

from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic
from pika.spec import BasicProperties
from server import channel


def process_msg(chan: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body):
    print(f"[{method.routing_key}] event consumed from exchange `{method.exchange}` body `{body}`")


# consume messages from queues
channel.basic_consume(queue="hello-world", on_message_callback=process_msg, auto_ack=True)

channel.basic_consume(queue="queue-a", on_message_callback=process_msg, auto_ack=True)
channel.basic_consume(queue="queue-b", on_message_callback=process_msg, auto_ack=True)
channel.basic_consume(queue="queue-c", on_message_callback=process_msg, auto_ack=True)

channel.start_consuming()
