import pika

from config import CONFIG

RABBIT_MQ_SERVER = "localhost"

# establish connection with rabbit mq
credentials = pika.PlainCredentials(CONFIG['RABBIT_USER'], CONFIG['RABBIT_PASSWORD'])
parameters = pika.ConnectionParameters(RABBIT_MQ_SERVER, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
