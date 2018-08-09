from typing import Callable

from kombu import Connection, Consumer, Exchange, Queue, binding


EVENT_KEY = 'interesting_event'
REDIS_URL = 'redis://localhost:6379'

some_exchange = Exchange('some_exchange', 'topic', durable=True)


def get_connection() -> Connection:
    return Connection(REDIS_URL)


def listen_to_event(queue_name: str, callback: Callable):
    with get_connection() as conn:
        bindings = [binding(some_exchange, routing_key=EVENT_KEY)]
        queue = Queue(queue_name, exchange=some_exchange, routing_key=EVENT_KEY, bindings=bindings)
        with Consumer(conn, [queue], callbacks=[callback], auto_declare=True):
            print(f'>>> [{queue_name}] Listening to "{EVENT_KEY}" routing key')
            try:
                while True:
                    conn.drain_events()
            except (KeyboardInterrupt, SystemExit):
                print(f'>>> [{queue_name}] Stopped listening to "{EVENT_KEY}"')
