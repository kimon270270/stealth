## 🔴 Stealth – Red Team Persistence Simulation
Stealth is a red team simulation project designed to demonstrate how attackers achieve persistent access on a Windows system using startup folder persistence and hidden payload execution.

This project mimics real-world adversary tactics used in post-exploitation scenarios — such as those documented in the MITRE ATT&CK framework (T1547, T1059).

### ⚠️ For educational and ethical red team training only.
This project must not be deployed outside of isolated lab environments.

### 🔍 What It Does
Upon execution, the script performs the following:

- Downloads a Python script, requirements.txt, and an image from a GitHub repo
- Saves all content in a hidden directory: %APPDATA%\Roaming\Microsoft\MyApplications
- Installs Python dependencies silently (no CLI window)
- Converts the downloaded script into an .exe file using PyInstaller
- Places the .exe in the Windows startup folder to achieve persistence
- The executable runs on boot and launches the image (simulated payload)

🔁 Workflow Summary:

⬇️ Download script + image from GitHub
🛠️ Silent dependency install
🔁 .py → .exe conversion
🪪 Startup persistence via Windows startup folder
🖼️ Executable triggers image on each boot


### ⚙️ Technologies Used
Python: subprocess (with CREATE_NO_WINDOW), pyinstaller, requests, .pyw, win32com.client

Windows: Startup folder, APPDATA directory

### 🚀 How to Run
- Clone this repository
- Install required dependencies: 'pip install -r requirements.txt'
- Run the main launcher: 'python serviceupdate.py'
#### Note: This script is meant to be executed only in a safe, non-production virtual machine for red team simulation training.

### 📌 Ethical Notice
This tool is strictly for educational, research, and simulation purposes.
It was created to understand and demonstrate common persistence techniques used by attackers and should never be deployed in a real-world or unauthorized environment.

Misuse of this tool may violate laws and ethical guidelines.
