import requests
import uuid
import threading
from eras.config.config import config
from ga4mp import GtagMP


def send_analytics_event(event_name, event_params=''):
    def send_event():
        try:
            measurement_id = config.get_google_analytics_measurement_id()
            api_secret = config.get_google_analytics_secret()
            client_id = str(uuid.uuid4())

            message = f"id: {config.get_system_identifier()}, operating_system: {config.get_user_operating_system()}, data: {event_params}"
            # print(message)

            # Initialize GtagMP client
            ga_client = GtagMP(api_secret=api_secret, measurement_id=measurement_id, client_id=client_id)

            # Prepare event data
            event_data = {
                'name': event_name,
                'params': {
                    'message': message
                }
            }

            # Send event
            ga_client.send([event_data])

            # print(f'Event sent: {event_data}')
        except Exception as e:
            pass
            # print(f'Exception sending event: {e}')

    # Run the send_event function in a separate thread
    thread = threading.Thread(target=send_event)
    thread.start()

# def send_analytics_event(event_name, event_params=''):
#     def send_event():
#         try:
#             measurement_id = config.get_google_analytics_measurement_id()
#             api_secret = config.get_google_analytics_secret()
#
#             client_id = str(uuid.uuid4())
#
#             message = f'''id: {config.get_system_identifier()}, operating_system: {config.get_user_operating_system()}, data: {event_params}'''
#             print(message)
#             payload = {
#                 'client_id': client_id,
#                 'events': [
#                     {
#                         'name': event_name,
#                         'params': message
#                     }
#                 ]
#             }
#             response = requests.post(
#                 f'https://www.google-analytics.com/mp/collect?measurement_id={measurement_id}&api_secret={api_secret}',
#                 json=payload
#             )
#             # print('analytics event sent')
#             print(response)
#         except Exception as e:
#             print('exception sending event: ')
#             print(e)
#             pass  # Swallow all exceptions
#
#     # Run the send_event function in a separate thread
#     thread = threading.Thread(target=send_event)
#     thread.start()

