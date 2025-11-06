import subprocess, requests, os, ctypes

github_raw_link = "https://raw.githubusercontent.com/muslumozturk61/akif-yasakli-siteler/main/kodlar/site_yasakla_otomatik.exe"
exe_path = r"C:\Program Files (x86)\sy.exe"


try:
    if(ctypes.windll.shell32.IsUserAnAdmin()):
        pass
except:
    print("yönetici hakları gerekli")

os.makedirs(os.path.dirname(exe_path), exist_ok=True)

try:
    with requests.get(github_raw_link, stream=True) as response:
        response.raise_for_status()
        with open(exe_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
    print(f"Dosya başarıyla indirildi: {exe_path}")
except Exception as e:
    print(f"Dosya indirme hatası: {e}")
    exit(1)


try:
    subprocess.run(f'schtasks /delete /tn "sy" /f', shell=True, capture_output=True)

    command = (
        f'schtasks /create /tn "sy" /tr "{exe_path}" '
        f'/sc onlogon /rl HIGHEST /f'
    )
    subprocess.run(command, shell=True, check=True)
    print("Görev başarıyla oluşturuldu!")
except subprocess.CalledProcessError as e:
    print(f"Görev oluşturma hatası: {e}")