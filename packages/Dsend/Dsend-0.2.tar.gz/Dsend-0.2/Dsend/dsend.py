# my_library/dsend.py

import requests

def get(url_for_send, print_response=False, print_text=False, timeout=5):
    url = 'https://send.marop18689.workers.dev'
    try:
        data_to_send = {
            "method": "GET",
            "url": url_for_send,
            "data": None
        }

        response_post = requests.post(url, json=data_to_send, timeout=timeout)
        
        if print_response:
            print(response_post)
        if print_text:
            print(response_post.text)

    except Exception as e:
        print(f"An error occurred: {e}")
