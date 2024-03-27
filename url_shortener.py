import requests
import json

def get_url(original_url: str):
    response = requests.get('https://url.api.stdlib.com/temporary@0.3.0/create/', 
                            params={'url': original_url, 
                                    'ttl': 60})
    
    if response.status_code < 299:
        return response.json()['link_url']
    else:
        print('Something went wrong')