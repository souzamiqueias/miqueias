import requests
from decouple import config

class Waha:

    def __init__(self):
        self.__api_url = config('WAHA_API_URL', default='http://localhost:3000')

    def send_message(self, chat_id, message):
        url = f'{self.__api_url}/api/sendText'
        headers = {
            'Content-Type': 'application/json',
        }
        payload = {
            'session': 'default',
            'chatId': chat_id,
            'text': message,
        }
        response = requests.post(
            url=url,
            json=payload,
            headers=headers,
        )
        return response.json()  # Adicionado para retornar a resposta

    def get_history_messages(self, chat_id, limit):
        url = f'{self.__api_url}/api/default/chats/{chat_id}/messages?limit={limit}&downloadMedia=false'
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.get(
            url=url,
            headers=headers,
        )
        return response.json()

    def start_typing(self, chat_id):
        url = f'{self.__api_url}/api/startTyping'
        headers = {
            'Content-Type': 'application/json',
        }
        payload = {
            'session': 'default',
            'chatId': chat_id,
        }
        response = requests.post(
            url=url,
            json=payload,
            headers=headers,
        )
        return response.json()  # Adicionado para retornar a resposta

    def stop_typing(self, chat_id):
        url = f'{self.__api_url}/api/stopTyping'
        headers = {
            'Content-Type': 'application/json',
        }
        payload = {
            'session': 'default',
            'chatId': chat_id,
        }
        response = requests.post(
            url=url,
            json=payload,
            headers=headers,
        )
        return response.json()  # Adicionado para retornar a resposta
