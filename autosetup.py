import os
import zipfile
import wget
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import time

# Clear terminal screen
os.system('cls' if os.name == 'nt' else 'clear')

# Auto setup info
print("Auto setup UG")
print("""
Thanks for ticket rep support from ngquocthanh
and W-azure
[1]: Delta
[2]: Fluxus
[3]: Codex
[4]: ArceusX
""")

# Choose mode
def get_mode():
    while True:
        try:
            mode = int(input("Mode: "))
            if 1 <= mode <= 4:
                return mode
            else:
                print("Invalid mode. Choose between 1 and 4.")
        except ValueError:
            print("Invalid input. Enter a number.")

# Choose number of tabs
def get_tab_count():
    while True:
        try:
            tab = int(input("How many tabs: "))
            if 1 <= tab <= 10:
                return tab
            else:
                print("Choose a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Enter a number.")

# Check for root access
def is_rooted():
    try:
        return os.system('su -c "echo"') == 0
    except Exception as e:
        print(f"Error checking root status: {e}")
        return False

# Check if file exists
def file_exists(file_path):
    return os.path.exists(file_path)

# Mediafire download helper
def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_external_download_link(url):
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for a_tag in soup.find_all("a"):
        href = urljoin(url, a_tag.get("href", ""))
        if is_valid_url(href) and href.startswith("https://download"):
            return href
    return None

# Unzipping functions
def unzip_file(zip_file, extract_to):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

# Installation process
def uninstall_play_store():
    print("Uninstalling Google Play...")
    os.system('su -c "pm uninstall -k --user 0 com.android.vending"')

def download_and_extract(file_url, file_name, extract_to):
    if not file_exists(file_name):
        print(f"Downloading {file_name}...")
        wget.download(file_url, out=file_name)
    else:
        print(f"{file_name} already exists. Proceeding to extraction...")
    unzip_file(file_name, extract_to)

# APK installation process
def install_apks(apk_base_name, tab_count):
    for i in range(1, tab_count + 1):
        apk_path = f"/sdcard/Download/{apk_base_name}{i}.apk"
        print(f"Installing {apk_base_name}{i}.apk...")
        os.system(f'su -c "pm install {apk_path}"')

# Main setup
def setup(mode, tab_count):
    # Download and unzip main app
    app_zip_url = "https://github.com/MinhMeow123/Autosetup/releases/download/database/App.zip"
    app_zip_file = "/sdcard/Download/App.zip"
    download_and_extract(app_zip_url, app_zip_file, "/sdcard/Download/")

    if mode == 1:
        # Delta mode
        setup_delta(tab_count)
    elif mode == 2:
        # Fluxus mode
        setup_fluxus(tab_count)
    elif mode == 3:
        # Codex mode
        setup_codex(tab_count)
    elif mode == 4:
        # ArceusX mode
        setup_arceusx(tab_count)

    # Final steps
    os.system('su -c "pm uninstall -k --user 0 com.android.vending"')

# Setup specific modes
def setup_delta(tab_count):
    if tab_count <= 5:
        delta_zip = "/sdcard/Download/delta.zip"
        delta_url = "https://github.com/MinhMeow123/Autosetup/releases/download/database/delta.zip"
    else:
        delta_zip = "/sdcard/Download/deltasvip.zip"
        delta_url = "https://github.com/MinhMeow123/Autosetup/releases/download/database/delta2.zip"
    download_and_extract(delta_url, delta_zip, "/sdcard/Download/")
    install_apks("delta", tab_count)

def setup_fluxus(tab_count):
    if tab_count <= 5:
        fluxus_zip = "/sdcard/Download/fluxus.zip"
        fluxus_url = "https://github.com/MinhMeow123/Autosetup/releases/download/database/fluxus.zip"
    else:
        fluxus_zip = "/sdcard/Download/fluxus2.zip"
        fluxus_url = "https://github.com/MinhMeow123/Autosetup/releases/download/database/fluxus2.zip"
    download_and_extract(fluxus_url, fluxus_zip, "/sdcard/Download/")
    install_apks("fluxus", tab_count)

def setup_codex(tab_count):
    if tab_count <= 5:
        codex_zip = "/sdcard/Download/codex.zip"
        codex_url = "https://github.com/MinhMeow123/Autosetup/releases/download/database/codex.zip"
    else:
        codex_zip = "/sdcard/Download/codexvip.zip"
        codex_url = "https://github.com/MinhMeow123/Autosetup/releases/download/database/codex2.zip"
    download_and_extract(codex_url, codex_zip, "/sdcard/Download/")
    install_apks("codex", tab_count)

def setup_arceusx(tab_count):
    if tab_count <= 5:
        arceusx_zip = "/sdcard/Download/arceusx.zip"
        arceusx_url = "https://github.com/MinhMeow123/Autosetup/releases/download/database/arceusx.zip"
    else:
        arceusx_zip = "/sdcard/Download/arceusxvip.zip"
        arceusx_url = "https://github.com/MinhMeow123/Autosetup/releases/download/database/arceusx2.zip"
    download_and_extract(arceusx_url, arceusx_zip, "/sdcard/Download/")
    install_apks("arceusx", tab_count)

# Start the process
if __name__ == "__main__":
    mode = get_mode()
    tab_count = get_tab_count()

    if not is_rooted():
        print("Root access is required. Please enable root.")
        exit()

    setup(mode, tab_count)

    # Run additional tools if necessary
    os.system('su -c "cd /sdcard/download && python ./tool.py"')
