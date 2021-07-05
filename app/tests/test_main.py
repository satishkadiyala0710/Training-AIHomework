import json

#for testing api/v1/info service
def test_index(app, client):
    res = client.get('/api/v1/info')
    assert res.status_code == 200
    expected = {"Receiver": "Cisco is the best"}
    assert expected == json.loads(res.get_data(as_text=True))