import toml
import base64
from HTTP_client import HttpClient

def send_msg(sender, recipient, msg):
    config = toml.load('config.toml')
    url = config['server']['url']
    username = config['user']['username']
    password = config['user']['password']

    user_header = base64.b64encode(f'{username}:{password}'.encode()).decode()

    request_body = {
        'sender': sender,
        'recipient': recipient,
        'message': msg
    }

    headers = {
        'Host': 'localhost',
        'Authorization': f'Basic {user_header}',
        #'Content-Type': 'application/json'
    }

    client = HttpClient(url)
    response = client.post('/send_sms', request_body, headers)

    return response