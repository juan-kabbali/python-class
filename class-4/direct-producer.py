import time

from server import channel

QUEUE_HELLO_WORLD = "hello-world"
EXCHANGE_NAME = "direct-exchange-hello-world"

# create exchange
channel.exchange_declare(EXCHANGE_NAME, durable=True, exchange_type='direct')

# create a queue
channel.queue_declare(queue=QUEUE_HELLO_WORLD)
channel.queue_bind(exchange=EXCHANGE_NAME, queue=QUEUE_HELLO_WORLD)

# publish event
events = ["event 1", "event 2", "event 3", "event 4", "event 5"]

for event in events:
    channel.basic_publish(exchange=EXCHANGE_NAME, routing_key=QUEUE_HELLO_WORLD, body=event)
    time.sleep(2)
    print(f"[x] published {event}")
