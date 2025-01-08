from services.waha import Waha

def test_waha():
    waha = Waha()
    response = waha.send_message(chat_id='12345', message='Testando integração com o Waha')
    print(response)

def test_get_history_messages():
    waha = Waha()
    history = waha.get_history_messages(chat_id='12345', limit=10)
    print(history)

def test_typing_indicators():
    waha = Waha()
    waha.start_typing(chat_id='12345')
    print("Started typing...")
    waha.stop_typing(chat_id='12345')
    print("Stopped typing...")

if __name__ == '__main__':
    test_waha()
    test_get_history_messages()
    test_typing_indicators()
