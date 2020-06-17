import requests


class SimpleClient(object):

    def __init__(self, domain, namespace=None):
        self.domain = domain
        self.namespace = namespace

    def __getitem__(self, item):
        item_path = f'{self.namespace}/{item}' if self.namespace is not None else item
        response = requests.get(f'https://{self.domain}/{item_path}')
        return response.content.decode()
