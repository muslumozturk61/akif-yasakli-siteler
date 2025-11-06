import requests, ctypes, time

url = "https://github.com/muslumozturk61/akif-yasakli-siteler/raw/refs/heads/main/kodlar/site_yasakla_otomatik.exe"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

hosts_file_path = r"C:\Windows\System32\drivers\etc\hosts"

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
            return linkler
        else:
            return []
    except Exception as e:
        print(e) 
        return []  
    
def readHostFile():
    try:
        with open(hosts_file_path, 'r', encoding="utf-8") as hosts_file:
            return hosts_file.readlines()
    except:
        return ""
    
def writeHostFile(text):
    try:
        with open(hosts_file_path, 'a', encoding="utf-8") as hosts_file:
            hosts_file.write(text)
            return None
    except:
        return None


def ban(baning_url):
  
    hosts_file_lines = readHostFile()

    for i in hosts_file_lines:
        if (i.__contains__(f"127.0.0.1 {baning_url}")):
            return None
        
    writeHostFile(f"\n127.0.0.1 {baning_url}")

        
if (isAdmin()):
    for d in range(1,10):
        liste=siteListesi()
        if(list.len != 0):
            for i in liste:
                ban(i)
            break

        time.sleep(5)
else:
    print("yönetici hakları gerekli")