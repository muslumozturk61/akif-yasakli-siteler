import libs as l

hosts_file_path = r"C:\Windows\System32\drivers\etc\hosts"

def ban(baning_url):
  
    hosts_file_lines = l.readHostFile()

    for i in hosts_file_lines:
        if (i.__contains__(f"127.0.0.1 {baning_url}")):
            return None
        
    l.writeHostFile(f"\n127.0.0.1 {baning_url}")
        
if (l.isAdmin()):
    for i in l.siteListesi():
        ban(i)
else:
    print("yönetici hakları gerekli")