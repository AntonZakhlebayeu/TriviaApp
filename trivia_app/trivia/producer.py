import pickle

from kafka import KafkaProducer

from trivia_app.settings import KAFKA_CHANNEL, KAFKA_URI


def kfk_login(id: int):
    producer = KafkaProducer(bootstrap_servers=KAFKA_URI)
    v = {
        "msg": {"id": id, "login": True},
    }
    serialized_data = pickle.dumps(v, pickle.HIGHEST_PROTOCOL)
    producer.send(KAFKA_CHANNEL, serialized_data)


def kfk(request, answer: bool):
    producer = KafkaProducer(bootstrap_servers=KAFKA_URI)
    v = {
        "msg": {"id": request.user.pk, "answer": answer},
    }
    serialized_data = pickle.dumps(v, pickle.HIGHEST_PROTOCOL)
    producer.send(KAFKA_CHANNEL, serialized_data)
