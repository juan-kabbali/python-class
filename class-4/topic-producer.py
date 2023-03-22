import time

from server import channel

QUEUES = [
    {
        "name": "queue-a",
        "topic": "a"
    },
    {
        "name": "queue-b",
        "topic": "b"
    },
    {
        "name": "queue-c",
        "topic": "c"
    }
]

EVENTS = [
    {
        "topic": "a",
        "body": "event 1"
    },
    {
        "topic": "b",
        "body": "event 1"
    },
    {
        "topic": "c",
        "body": "event 1"
    },
    {
        "topic": "a",
        "body": "event 2"
    },
    {
        "topic": "b",
        "body": "event 2"
    }
]

EXCHANGE_NAME = "topic-exchange-hello-world"

# create exchange
channel.exchange_declare(EXCHANGE_NAME, durable=True, exchange_type='topic')

# create queues
for queue in QUEUES:
    channel.queue_declare(queue=queue['name'])
    channel.queue_bind(exchange=EXCHANGE_NAME, queue=queue['name'], routing_key=queue['topic'])


# publish event
for event in EVENTS:
    channel.basic_publish(exchange=EXCHANGE_NAME, routing_key=event['topic'], body=event['body'])
    time.sleep(2)
    print(f"[x] published event `{event['body']}` in topic `{event['topic']}`")
