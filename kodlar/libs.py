import requests, ctypes

url = "https://raw.githubusercontent.com/muslumozturk61/akif-yasakli-siteler/refs/heads/main/siteler.txt"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


def isAdmin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def siteListesi(url=url, headers=headers):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            linkler = []
            for i in response.text.split("\n"):
                if (i != ""):
                    linkler.append(i)
            print(response.text)
            return linkler
        else:
            return []
    except Exception as e:
        print(e) 
        return []  