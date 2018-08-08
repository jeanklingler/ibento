import sys

from ibento.common import listen_to_event


try:
    WORKER_NAME = sys.argv[1]
except IndexError:
    WORKER_NAME = 'default_worker'


def process_message(body, message):
    print(f'>>> [{WORKER_NAME}] processing:', body)
    message.ack()


listen_to_event(queue_name=WORKER_NAME, callback=process_message)
