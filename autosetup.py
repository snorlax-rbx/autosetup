import os
import zipfile
import wget
import requests
import time
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

# Check if file exists
def file_exists(file_path):
    return os.path.exists(file_path)

# Unzipping function
def unzip_file(zip_file, extract_to):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

# Download and extract helper function
def download_and_extract(file_url, file_name, extract_to):
    if not file_exists(file_name):
        print(f"Downloading {file_name}...")
        wget.download(file_url, out=file_name)
    else:
        print(f"{file_name} already exists. Proceeding to extraction...")
    unzip_file(file_name, extract_to)

# APK installation function
def install_apks(apk_base_name, tab_count):
    for i in range(1, tab_count + 1):
        apk_path = f"/sdcard/Download/{apk_base_name}{i}.apk"
        print(f"Installing {apk_base_name}{i}.apk...")
        os.system(f'su -c "pm install {apk_path}"')

# Mode setup functions
def setup_delta(tab_count):
    delta_zip = "/sdcard/Download/delta.zip"
    delta_url = "https://github.com/MinhMeow123/Autosetup/releases/download/database/delta.zip"
    download_and_extract(delta_url, delta_zip, "/sdcard/Download/")
    install_apks("delta", tab_count)

def setup_fluxus(tab_count):
    fluxus_zip = "/sdcard/Download/fluxus.zip"
    fluxus_url = "https://github.com/MinhMeow123/Autosetup/releases/download/database/fluxus.zip"
    download_and_extract(fluxus_url, fluxus_zip, "/sdcard/Download/")
    install_apks("fluxus", tab_count)

def setup_codex(tab_count):
    codex_zip = "/sdcard/Download/codex.zip"
    codex_url = "https://github.com/MinhMeow123/Autosetup/releases/download/database/codex.zip"
    download_and_extract(codex_url, codex_zip, "/sdcard/Download/")
    install_apks("codex", tab_count)

def setup_arceusx(tab_count):
    arceusx_zip = "/sdcard/Download/arceusx.zip"
    arceusx_url = "https://github.com/MinhMeow123/Autosetup/releases/download/database/arceusx.zip"
    download_and_extract(arceusx_url, arceusx_zip, "/sdcard/Download/")
    install_apks("arceusx", tab_count)

# Root status checker
def is_rooted():
    try:
        return os.system('su -c "echo"') == 0
    except Exception as e:
        print(f"Error checking root status: {e}")
        return False

# Main setup
def start_setup(mode, tab_count):
    # Download and unzip main app
    app_zip_url = "https://github.com/MinhMeow123/Autosetup/releases/download/database/App.zip"
    app_zip_file = "/sdcard/Download/App.zip"
    download_and_extract(app_zip_url, app_zip_file, "/sdcard/Download/")

    if mode == "Delta":
        setup_delta(tab_count)
    elif mode == "Fluxus":
        setup_fluxus(tab_count)
    elif mode == "Codex":
        setup_codex(tab_count)
    elif mode == "ArceusX":
        setup_arceusx(tab_count)

    # Final steps
    os.system('su -c "pm uninstall -k --user 0 com.android.vending"')
    print(f"\n{mode} setup completed!")

# Simple text-based UI
def main():
    os.system('clear')
    print("Welcome to the UG Setup Tool!")
    
    # Mode selection
    print("\nSelect Mode:")
    print("[1] Delta")
    print("[2] Fluxus")
    print("[3] Codex")
    print("[4] ArceusX")
    
    while True:
        try:
            mode_choice = int(input("\nEnter your choice (1-4): "))
            if 1 <= mode_choice <= 4:
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    mode_dict = {1: "Delta", 2: "Fluxus", 3: "Codex", 4: "ArceusX"}
    mode = mode_dict[mode_choice]
    
    # Tab selection
    while True:
        try:
            tab_count = int(input("\nEnter the number of tabs (1-10): "))
            if 1 <= tab_count <= 10:
                break
            else:
                print("Invalid number. Please choose between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Root check
    if not is_rooted():
        print("\nError: Root access is required. Please enable root access.")
        return

    print(f"\nStarting {mode} setup with {tab_count} tabs...\n")
    start_setup(mode, tab_count)

if __name__ == "__main__":
    main()
