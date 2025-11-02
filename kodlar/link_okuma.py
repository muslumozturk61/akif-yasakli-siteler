import requests

url = "https://raw.githubusercontent.com/muslumozturk61/akif-yasakli-siteler/refs/heads/main/siteler.txt"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print(response.text)
else:
    print(response.status_code)