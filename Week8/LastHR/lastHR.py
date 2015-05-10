import requests
import json
import sqlite3

class HR:

    def __init__(self):
        self.data = requests.get("https://hackbulgaria.com/api/students/").json()

    def save(self, content):
        with open("data4.json", "w") as f:
            json_str = json.dumps(content, indent = True, ensure_ascii = False)
            f.write(json_str)

    def read(self, filename):
        with open(filename, "r") as f:
            content = json.loads(f.read())
        return content
def main():
    hr = HR()

if __name__ == '__main__':
    main()
