import win32com.client, requests

github_api_link = "https://github.com/muslumozturk61/akif-yasakli-siteler/blob/main/kodlar/site_yasakla_otomatik.exe"

with requests.get(github_api_link, stream=True) as response:
    response.raise_for_status()
    with open(r"C:\Program Files (x86)\sy.exe", "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)


def create_login_task(task_name, exe_path):
    scheduler = win32com.client.Dispatch("Schedule.Service")
    scheduler.Connect()
    root_folder = scheduler.GetFolder("\\")

    task_def = scheduler.NewTask(0)

    task_def.RegistrationInfo.Description = f"Run {exe_path} at user logon with highest privileges"

    trigger = task_def.Triggers.Create(9)
    trigger.UserId = "Users"
    trigger.Enabled = True

    action = task_def.Actions.Create(0)
    action.Path = exe_path

    task_def.Principal.RunLevel = 1

    # Görevi kaydet
    root_folder.RegisterTaskDefinition(
        task_name,
        task_def,
        6,  # TASK_CREATE_OR_UPDATE
        "",  # user name
        "",  # password
        3   # TASK_LOGON_INTERACTIVE_TOKEN
    )
    print("hazırlandı :)")

task_name = "sy"
exe_path = r"C:\Program Files (x86)\sy.exe"
create_login_task(task_name, exe_path)