import json
from app.main import app

def test_post_message_valid():
    client = app.test_client()
    payload = {
        "message": "This is a test",
        "to": "Juan Perez",
        "from": "Rita Asturia",
        "timeToLifeSec": 45
    }
    response = client.post('/DevOps', 
                            headers={"X-Parse-REST-API-Key": "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"},
                            data=json.dumps(payload),
                            content_type='application/json')

    assert response.status_code == 200
    assert response.json['message'] == "Hello Juan Perez your message will be send"

def test_post_message_invalid_api_key():
    client = app.test_client()
    payload = {
        "message": "This is a test",
        "to": "Juan Perez"
    }
    response = client.post('/DevOps',
                            headers={"X-Parse-REST-API-Key": "invalid-key"},
                            data=json.dumps(payload),
                            content_type='application/json')

    assert response.status_code == 401
