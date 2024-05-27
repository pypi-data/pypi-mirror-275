import requests

class ApiMyLlama:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def generate(self, apikey, prompt, model, stream=False, images=None, raw=False):
        url = f'http://{self.ip}:{self.port}/generate'
        payload = {
            'apikey': apikey,
            'prompt': prompt,
            'model': model,
            'stream': stream,
            'images': images,
            'raw': raw
        }
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as error:
            raise error
