import time

from ibento.common import listen_to_event


def process_message(body, message):
    print(f'>>> Sending email:', body)
    time.sleep(1)
    print(f'>>> Sent email:', body)
    message.ack()


listen_to_event(queue_name='send_email_worker', callback=process_message)
