import requests


class GameAPI:
    def __init__(self):
        clues_conn = open('connect.txt', 'r')
        ip = str(clues_conn.readlines(1))[2:-4]
        port = int(clues_conn.readlines(2)[0])
        self.url = f"http://{ip}:{port}/answers"
        clues_conn.close()

    def exec(self, text):
        obj = {'password': f'{text}'}
        req = requests.post(self.url, data=obj, timeout=5)
        return req.text

    def bruteforce(self):
        wordlist = ['a', 'b', 'd', 'i', 'j', 'k', 'm', 'o']
        for p1 in wordlist:
            for p2 in wordlist:
                for p3 in wordlist:
                    for p4 in wordlist:
                        self.exec(text=f"{p1}a{p2}b{p3}{p4}")
