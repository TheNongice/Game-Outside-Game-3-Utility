import requests
class GameAPI:
    def __init__(self):
        clues_conn = open('connect.txt','r')
        ip = str(clues_conn.readlines(1))[2:-4]
        self.port = int(clues_conn.readlines(2)[0])
        self.url = f"http://{ip}:{self.port}/answers"
    def exec(self,text):
        obj = {'password': f'{text}'}
        req = requests.post(self.url, data = obj)
        return req.text