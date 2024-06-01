"""
LinEscalate: Linux Privilege Escalation Checker

I made LinEscalate after learning about Linux privilege escalation and realizing that automating the process
would save a lot of time. This project started as a fun way for me to apply what I learned and to create a tool
that can help others quickly identify potential security vulnerabilities and misconfigurations on Linux systems.

References:
- https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/
- https://gtfobins.github.io/

Features:
- System Information
- User and Group Information
- Sudo Permissions
- Sensitive Files
- SUID and SGID Files
- World-writable Files
- Kernel Version
- Cron Jobs
- Installed Packages
- Writable Directories in PATH
- Network Information
- Running Processes

Usage:
1. Run the script.
2. Select an option from the menu to perform a specific check or run a full scan.
3. Analyze the output for potential security issues.

Color Coding:
- Cyan: Section titles for easy navigation.
- Yellow: Potential vulnerabilities (e.g., contents of sensitive files, SUID/SGID files).
- Red: Definite vulnerabilities (e.g., world-writable files, writable PATH directories, known vulnerable kernel versions).

Disclaimer:
Use this script responsibly and ensure you have appropriate permissions before running it on any system.
This script is intended for educational purposes and initial security assessments.

Author: PixelPlatypus
"""

import os
import subprocess
from colorama import Fore, Style, init

# Initialize colorama
init()

def run_command(command):
    return subprocess.getoutput(command)

def print_section(title):
    print()
    print(Fore.CYAN + Style.BRIGHT + f"### {title} ###" + Style.RESET_ALL)

def get_system_info():
    print_section("System Information")
    print(run_command("uname -a"))
    print(run_command("cat /etc/issue"))
    print()

def get_user_info():
    print_section("User and Group Information")
    print(run_command("id"))
    print(run_command("who"))
    print(run_command("w"))
    print(run_command("last"))
    print(run_command("cat /etc/passwd | cut -d: -f1"))  # List of users
    print(run_command("grep -v -E '^#' /etc/passwd | awk -F: '$3 == 0 { print $1}'"))  # List of super users
    print(run_command("sudo -l"))
    print()

def check_sudo_permissions():
    print_section("Sudo Permissions")
    sudo_permissions = run_command("sudo -l")
    if "NOPASSWD" in sudo_permissions:
        print(f"{Fore.RED}Potential vulnerability: NOPASSWD entries found in sudo permissions.{Style.RESET_ALL}")
    print(sudo_permissions)
    print()

def find_sensitive_files():
    print_section("Sensitive Files")
    sensitive_files = [
        "/etc/passwd", "/etc/group", "/etc/shadow", 
        "/var/mail/", "/root/anaconda-ks.cfg", 
        "/root/.bash_history", "/root/.ssh/id_rsa"
    ]
    for file in sensitive_files:
        if os.path.exists(file):
            print(f"{Fore.YELLOW}Contents of {file}:{Style.RESET_ALL}")
            print(run_command(f"cat {file}"))
        else:
            print(f"{file} does not exist.")
    print()

def find_suid_sgid_files():
    print_section("SUID and SGID Files")
    suid_files = run_command("find / -perm -4000 -type f 2>/dev/null")
    sgid_files = run_command("find / -perm -2000 -type f 2>/dev/null")
    if suid_files:
        print(f"{Fore.YELLOW}SUID files found:{Style.RESET_ALL}")
        print(suid_files)
    else:
        print("No SUID files found.")
    if sgid_files:
        print(f"{Fore.YELLOW}SGID files found:{Style.RESET_ALL}")
        print(sgid_files)
    else:
        print("No SGID files found.")
    print()

def find_world_writable_files():
    print_section("World-writable Files")
    writable_files = run_command("find / -type f -perm -o+w 2>/dev/null")
    if writable_files:
        print(f"{Fore.RED}World-writable files found:{Style.RESET_ALL}")
        print(writable_files)
    else:
        print("No world-writable files found.")
    print()

def check_kernel_version():
    print_section("Kernel Version")
    kernel_version = run_command("uname -r").strip()
    print(f"Kernel version: {kernel_version}")
    known_vulnerable_versions = ['5.4.0-26', '4.15.0-45']  # Example versions
    if kernel_version in known_vulnerable_versions:
        print(f"{Fore.RED}Warning: Kernel version {kernel_version} is known to have vulnerabilities.{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}Kernel version {kernel_version} is not known to have major vulnerabilities.{Style.RESET_ALL}")
    print()

def check_cron_jobs():
    print_section("Cron Jobs")
    cron_files = ['/etc/crontab', '/etc/cron.d/', '/var/spool/cron/crontabs/']
    for cron_file in cron_files:
        if os.path.exists(cron_file):
            print(f"{Fore.YELLOW}Contents of {cron_file}:{Style.RESET_ALL}")
            print(run_command(f"cat {cron_file}"))
        else:
            print(f"{cron_file} does not exist.")
    print()

def list_installed_packages():
    print_section("Installed Packages")
    print(run_command("dpkg -l"))
    print()

def check_writable_path_dirs():
    print_section("Writable Directories in PATH")
    paths = os.environ["PATH"].split(":")
    for path in paths:
        if os.access(path, os.W_OK):
            print(f"{Fore.RED}{path} is writable.{Style.RESET_ALL}")
        else:
            print(f"{path} is not writable.")
    print()

def check_network_info():
    print_section("Network Information")
    print(run_command("ifconfig -a"))
    print(run_command("netstat -tuln"))
    print()

def list_running_processes():
    print_section("Running Processes")
    print(run_command("ps aux"))
    print()

def menu():
    while True:
        print(Fore.CYAN + Style.BRIGHT + "\n### LinEscalate Menu ###" + Style.RESET_ALL)
        print("1. System Information")
        print("2. User and Group Information")
        print("3. Sudo Permissions")
        print("4. Sensitive Files")
        print("5. SUID and SGID Files")
        print("6. World-writable Files")
        print("7. Kernel Version")
        print("8. Cron Jobs")
        print("9. Installed Packages")
        print("10. Writable Directories in PATH")
        print("11. Network Information")
        print("12. Running Processes")
        print("13. Full Scan")
        print("14. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            get_system_info()
        elif choice == '2':
            get_user_info()
        elif choice == '3':
            check_sudo_permissions()
        elif choice == '4':
            find_sensitive_files()
        elif choice == '5':
            find_suid_sgid_files()
        elif choice == '6':
            find_world_writable_files()
        elif choice == '7':
            check_kernel_version()
        elif choice == '8':
            check_cron_jobs()
        elif choice == '9':
            list_installed_packages()
        elif choice == '10':
            check_writable_path_dirs()
        elif choice == '11':
            check_network_info()
        elif choice == '12':
            list_running_processes()
        elif choice == '13':
            full_scan()
        elif choice == '14':
            break
        else:
            print("Invalid choice. Please select again.")

def full_scan():
    get_system_info()
    get_user_info()
    check_sudo_permissions()
    find_sensitive_files()
    find_suid_sgid_files()
    find_world_writable_files()
    check_kernel_version()
    check_cron_jobs()
    list_installed_packages()
    check_writable_path_dirs()
    check_network_info()
    list_running_processes()

if __name__ == "__main__":
    menu()
