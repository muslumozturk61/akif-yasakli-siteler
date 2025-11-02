import tkinter as tk
from tkinter import ttk
import sys
from tkinter import messagebox as mb
import libs as l

siteListesi = l.siteListesi()

hosts_file_path = r"C:\Windows\System32\drivers\etc\hosts"
ttk.Style().theme_use("xpnative")

def ban(baning_url, already_label):
    with open(hosts_file_path, 'r', encoding="utf-8") as hosts_file:
        hosts_file_lines = hosts_file.readlines()
    for i in hosts_file_lines:
            if (i == f"127.0.0.1 {baning_url}"):
                already_label.pack()
    with open(hosts_file_path, 'a', encoding="utf-8") as hosts_file:
        hosts_file.write(f"127.0.0.1 {baning_url}\n")
    already_label.pack_forget()

def deban(debaning_url, already_label):
    with open(hosts_file_path, 'r', encoding="utf-8") as hosts_file:
        hosts_file_lines = hosts_file.readlines()
    for i in hosts_file_lines:
            if (i == f"127.0.0.1 {debaning_url}"):
                already_label.pack()
    lines = ""
    with open(hosts_file_path, 'r', encoding="utf-8") as hosts_file:
        hosts_file_lines = hosts_file.readlines()
    open(hosts_file_path, 'w').close()
    with open(hosts_file_path, 'w', encoding="utf-8") as writeable_hosts_file:
        for i in hosts_file_lines:
            if (not(i == f"127.0.0.1 {debaning_url}")):
                lines = lines + i
        writeable_hosts_file.write(lines)
    already_label.pack_forget()
        
if (l.isAdmin()):
    window = tk.Tk()
    window.title("site engelleyici")
    window.geometry("500x400")
    tabs = ttk.Notebook(window)
    
    ban_tab = ttk.Frame(tabs)
    deban_tab = ttk.Frame(tabs)
    hosts_file_tab = ttk.Frame(tabs)
    tabs.add(ban_tab, text="site yasakla")
    tabs.add(deban_tab, text="site yasağı kaldır")
    tabs.add(hosts_file_tab, text="hosts dosyası")
    tabs.pack(fill=tk.BOTH, expand=True)

    # baning
    already_banned = ttk.Label(ban_tab, text="zaten yasaklanmış")
    already_banned.pack_forget()
    ttk.Label(ban_tab, text="yasaklanacak site:").pack(pady=5)
    baning_site = ttk.Entry(ban_tab)
    baning_site.pack()
    ban_button = ttk.Button(ban_tab, text="yasakla", command=lambda: ban(baning_site.get(), already_banned))
    ban_button.pack(pady=5)

    # debaning
    already_debaned = ttk.Label(deban_tab, text="zaten yasaklanmamaış")
    already_debaned.pack_forget()
    ttk.Label(deban_tab, text="yasağı kaldırılacak site:").pack(pady=5)
    debaning_site = ttk.Entry(deban_tab)
    debaning_site.pack()
    deban_button = ttk.Button(deban_tab, text="yasak kaldır", command=lambda: deban(debaning_site.get(), already_banned))
    deban_button.pack(pady=5)

    # hosts file tab
    ttk.Label(hosts_file_tab, text="Hosts dosyası nedir?\nBigisayar bir siteyi açacağında ilk önce burada hangi ip'ye yönlendirilmiş diye bakar\nburada yoksa dns sunucusundan ister ve her satır \"192.168.4.1 abc.com\" şeklindedir\nbu program ise 127.0.0.1'e (yani iç ip'ye) istek atmayı sağlar bu şekilde\n\"127.0.0.1 yasak.com\" oluşturulur ve site asla açılmaz").pack()
    ttk.Button(hosts_file_tab, text="hosts dosyasını aç", command=lambda: None).pack()
    window.mainloop()
else:
    mb.showinfo(sys.argv[0], "yönetici hakları gerekli")