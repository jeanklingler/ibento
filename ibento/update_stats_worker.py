import time

from ibento.common import listen_to_event


def process_message(body, message):
    print(f'>>> Updating stats:', body)
    time.sleep(.5)
    print(f'>>> Updated stats:', body)
    message.ack()


listen_to_event(queue_name='update_stats_worker', callback=process_message)
