import subprocess, requests

github_api_link = "https://github.com/muslumozturk61/akif-yasakli-siteler/blob/main/kodlar/site_yasakla_otomatik.exe"

with requests.get(github_api_link, stream=True) as response:
    response.raise_for_status()
    with open(r"C:\Program Files (x86)\sy.exe", "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)

subprocess.run(r'schtasks /create /tn sy.exe /tr "C:\Program Files (x86)\sy.exe" /sc onlogon /rl HIGHEST', shell=True, check=True)