from s3_kvs import ReadOnlyClient


def test_item_path():
    client = ReadOnlyClient(domain='kvs.example.com')
    assert client.get_item_path('test_item') == 'https://kvs.example.com/test_item.json'


def test_namespaced_item_path():
    client = ReadOnlyClient(domain='kvs.example.com', namespace='tests')
    assert client.get_item_path('test_item') == 'https://kvs.example.com/tests/test_item.json'


def test_json_formatter_parsing():
    client = ReadOnlyClient(domain='kvs.example.com')
    formatter = client.get_formatter()
    assert formatter('{"foo":"bar"}') == {'foo': 'bar'}
