import os
import stat

# Define paths
boot_dir = os.path.expanduser("~/.termux/boot")
home_dir = "/data/data/com.termux/files/home"

# Create boot directory
os.makedirs(boot_dir, exist_ok=True)

# Create first script: 01_set_android_id.sh
script_1_content = '''#!/data/data/com.termux/files/usr/bin/sh
ANDROID_ID=b419fa14320149db # Replace with your actual Android ID
echo "Setting Android ID to $ANDROID_ID" >> /data/android_sh.log
settings put secure android_id $ANDROID_ID
if [ $? -ne 0 ]; then
    echo "Failed to set Android ID" >> /data/android_sh.log
    exit 1
fi
echo "Android ID set successfully" >> /data/android_sh.log
'''
with open(f"{home_dir}/01_set_android_id.sh", "w") as file:
    file.write(script_1_content)

# Create second script: 02_run_additional_command.sh
script_2_content = '''#!/data/data/com.termux/files/usr/bin/sh
su -c "/data/data/com.termux/files/usr/bin/sh /data/data/com.termux/files/home/01_set_android_id.sh"
'''
with open(f"{home_dir}/02_run_additional_command.sh", "w") as file:
    file.write(script_2_content)

# Create third script: 03_run_python_script.sh
script_3_content = '''#!/data/data/com.termux/files/usr/bin/sh
su -c "cd /sdcard/download && export PATH=$PATH:/data/data/com.termux/files/usr/bin && export TERM=xterm-256color && python ./rejoin.py" <<EOF
\\r
1
9999
EOF
'''
with open(f"{home_dir}/03_run_python_script.sh", "w") as file:
    file.write(script_3_content)

# Create master script: 00_run_scripts.sh
master_script_content = '''#!/data/data/com.termux/files/usr/bin/sh
/data/data/com.termux/files/home/01_set_android_id.sh
/data/data/com.termux/files/home/02_run_additional_command.sh
/data/data/com.termux/files/home/03_run_python_script.sh
'''
with open(f"{boot_dir}/00_run_scripts.sh", "w") as file:
    file.write(master_script_content)

# Make all scripts executable
scripts = [
    f"{home_dir}/01_set_android_id.sh",
    f"{home_dir}/02_run_additional_command.sh",
    f"{home_dir}/03_run_python_script.sh",
    f"{boot_dir}/00_run_scripts.sh"
]

for script in scripts:
    os.chmod(script, stat.S_IRWXU)

print("Termux boot setup complete! You can now reboot your device.")
