import requests

def send_pushbullet(title, body, access_token):
    url = "https://api.pushbullet.com/v2/pushes"
    headers = {"Access-Token": access_token}
    data = {
        "type": "note",
        "title": title,
        "body": body
    }
    requests.post(url, json=data, headers=headers)