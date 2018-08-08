import sys
from datetime import datetime, timezone

from ibento.common import some_exchange, get_connection, EVENT_KEY

try:
    message = sys.argv[1]
except IndexError:
    message = 'default message'

with get_connection() as conn:
    producer = conn.Producer(serializer='json')
    body = {'published': datetime.now(timezone.utc), 'message': message}
    print(f'publishing message: "{message}"')
    producer.publish(
        body,
        exchange=some_exchange,
        routing_key=EVENT_KEY,
    )

