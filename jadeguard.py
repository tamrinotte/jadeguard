# This Python file uses the following encoding: utf-8

# MODULES AND/OR LIBRARIES
from logging import basicConfig, DEBUG, debug, disable, CRITICAL
from sys import exit as sysexit, argv
from pathlib import Path
from os import system, popen
from getpass import getuser
from shutil import copy as shutilcopy


# Configuring debugging feature code
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Disabling the debugging feature. Hint: Comment out this line to enable debugging.
disable(CRITICAL)


# GLOBAL VARIABLES

command_dict = {
    'edit': 'Opens the regular firewall scripst in a file editor.',
    'show': 'Displays the firewall rules that have been set.',
    'set': 'Sets the firewall rules.',
    'delete': 'Delete all the firewall rules.',
    'restore': 'Restores the scripts.',
    'godmode': 'Open the original firewall scripts in a file editor.'
}

# List of arguments for displaying the help page
help_page_arguments = ['-h', '--help']


# Base directory path for JadeGuard
jadeguard_base_dir_path = Path("/opt/jadeguard")


# Directory paths for scripts
original_files_dir_path = Path(jadeguard_base_dir_path, "original_files")

bash_scripts_dir_path = Path(jadeguard_base_dir_path, "bash_scripts")


# File paths for original bash scripts
original_ipv4_file_path = Path(original_files_dir_path, "iptables_rules.sh")

original_ipv6_file_path = Path(original_files_dir_path, "ip6tables_rules.sh")

original_delete_rules_file_path = Path(original_files_dir_path, "delete_all_rules.sh")


# File paths for regular bash scripts
ipv4_file_path = Path(bash_scripts_dir_path, "iptables_rules.sh")

ipv6_file_path = Path(bash_scripts_dir_path, "ip6tables_rules.sh")

delete_rules_file_path = Path(bash_scripts_dir_path, "delete_all_rules.sh")


# ANSI color codes for styling text
jade_color = "\033[38;5;34m"

golden_color = "\033[38;5;220m"

light_blue_color = "\033[36m"

reset_color = "\033[0m"


# Template for formatting command and description
template = "{:<10}{}"


def main():
    """The function which runs the entire application"""

    banner = """{}
     _           _       ____                     _ 
    | | __ _  __| | ___ / ___|_   _  __ _ _ __ __| |
 _  | |/ _` |/ _` |/ _ \ |  _| | | |/ _` | '__/ _` |
| |_| | (_| | (_| |  __/ |_| | |_| | (_| | | | (_| |
 \___/ \__,_|\__,_|\___|\____|\__,_|\__,_|_|  \__,_|{}
""".format(jade_color, reset_color)

    # print(f'{jade_color}𝓙𝓐𝓓𝓔 𝓖𝓤𝓐𝓡𝓓{reset_color}\n')

    print(banner)

    user_check()

    if len(argv) == 2:

        user_command = argv[1]
        
        if user_command == list(command_dict.keys())[0]:

            open_edit_mode()

        elif user_command == list(command_dict.keys())[1]:

            show_the_rules()
        
        elif user_command == list(command_dict.keys())[2]:

            set_the_rules()

        elif user_command == list(command_dict.keys())[3]:

            delete_rules()

        elif user_command == list(command_dict.keys())[4]:

            restore_originals()

        elif user_command == list(command_dict.keys())[5]:

            godmode()

        elif user_command in help_page_arguments:

            show_the_help_page()

        else:

            print(f'Invalid command. Please refer to the help page to get more information about the usage. "jadeguard {help_page_arguments[0]}"')

    else:

        print(f'Invalid usage. Please refer to the help page to get more information about the usage. "jadeguard {help_page_arguments[0]}"')

def show_the_help_page():
    """A function which shows the help page"""

    print(f'{golden_color}𝓗𝓮𝓵𝓹{reset_color}')

    help_text = """
Usage: your_app.py [command] [options]

Description:
  A command-line application for setting firewall rules.

Commands:
{}

Options:
  -h, --help      Shows this help message and exits.

""".format("\n".join(template.format(k, v) for k, v in command_dict.items()))

    print(help_text)

def open_edit_mode():
    """A function which opens the regular bash script files in edit mode."""
    
    print(f'{golden_color}𝓔𝓭𝓲𝓽{reset_color}\n')

    while True:

        try:
        
            question = "Do you want to edit IPv4 or IPv6 rules?\n"

            print(question)

            answer = int(input("Enter your choice (4/6): "))
        
            if answer == 4:

                system(f'nano {ipv4_file_path}')

                break

            elif answer == 6:
                
                system(f'nano {ipv6_file_path}')

                break

            else:

                print("Invalid choice. Please enter 4 or 6.\n")

        except:

            print("\nExiting...\n")

            break


def show_the_rules():
    """A function which shows the iptables rules for both IPv4 and IPv6"""

    print(f'{golden_color}𝓢𝓱𝓸𝔀{reset_color}')

    print(f'\n{light_blue_color}𝓘𝓟𝓿4 𝓢𝓾𝓶𝓶𝓪𝓻𝔂{reset_color}\n')

    system("iptables -vnL")

    print(f'\n{light_blue_color}𝓘𝓟𝓿6 𝓢𝓾𝓶𝓶𝓪𝓻𝔂{reset_color}\n')

    system("ip6tables -vnL")


def set_the_rules():
    """A function which sets the firewall rules"""

    print(f'{golden_color}𝓢𝓮𝓽{reset_color}\n')

    while True:

        try:

            question = "Do you confirm your request to set iptables rules. Making mistake on firewall rules can expose your system to vulnerabilities?\n"

            print(question)

            answer = str(input("Enter your answer (y/n): ")).strip().lower()

            if answer == "y" or answer == "yes":

                print(f'\n{light_blue_color}IPv4 Summry{reset_color}\n')

                system(f'bash {ipv4_file_path}')

                print(f'\n{light_blue_color}IPv6 Summry{reset_color}\n')

                system(f'bash {ipv6_file_path}')
                
                print()

                break 

            elif answer == "n" or answer == "no":

                break

            elif answer == "exit" or answer == "cancel":

                break

            else:

                print("Invalid answer. Please enter y or n.\n")

        except:

            print("Exiting...\n")

            break


def user_check():
    """A function which checks if user is the root user"""

    username = getuser()

    if username != "root":

        print("This application requires root permissions. Exiting...\n")

        sysexit()


def delete_rules():
    """A function which deletes all the firewall rules"""
    
    print(f'{golden_color}𝓓𝓮𝓵𝓮𝓽𝓮{reset_color}\n')

    while True:

        try:

            question = "Do you confirm your request to delete all existing rules. This can expose your system to vulnerabilities?\n"

            print(question)

            answer = str(input("Enter your answer (y/n): ")).strip().lower()

            if answer == "y" or answer == "yes":

                system(f'bash {delete_rules_file_path}')

                print(f'\n{light_blue_color}𝓘𝓟𝓿4 𝓢𝓾𝓶𝓶𝓪𝓻𝔂{reset_color}\n')

                system("iptables -vnL")

                print(f'\n{light_blue_color}𝓘𝓟𝓿6 𝓢𝓾𝓶𝓶𝓪𝓻𝔂{reset_color}\n')

                system("ip6tables -vnL")

                print()

                break 

            elif answer == "n" or answer == "no":

                break

            elif answer == "exit" or answer == "cancel":

                break

            else:

                print("Invalid answer. Please enter y or n.\n")

        except:

            print("Exiting...\n")

            break


def restore_originals():
    """A function which restores bash script files from its' originals"""

    print(f'{golden_color}𝓡𝓮𝓼𝓽𝓸𝓻𝓮{reset_color}\n')

    while True:

        try:

            question = "Do you confirm your request to restore scripts?\n"

            print(question)

            answer = str(input("Enter your answer (y/n): ")).strip().lower()

            if answer == "y" or answer == "yes":

                shutilcopy(original_delete_rules_file_path, delete_rules_file_path)
                
                shutilcopy(original_ipv4_file_path, ipv4_file_path)
                
                shutilcopy(original_ipv6_file_path, ipv6_file_path)

                break

            elif answer == "n" or answer == "no":

                break

            elif answer == "exit" or answer == "cancel":

                break

            else:

                print("Invalid answer. Please enter y or n.\n")

        except:

            print("Exiting...\n")

            break


def godmode():
    """A function which opens the original bash scripts in edit mode."""

    print(f'{golden_color}𝓖𝓸𝓭 𝓜𝓸𝓭𝓮{reset_color}\n')

    while True:

        try:
        
            question = "Do you want to edit IPv4 or IPv6 rules?\n"

            print(question)

            answer = str(input("Enter your choice (4/6): "))
        
            if answer == "4":

                system(f'nano {original_ipv4_file_path}')

                break

            elif answer == "6":
                
                system(f'nano {original_ipv6_file_path}')

                break

            elif answer == "n" or answer == "no":

                break

            elif answer == "exit" or answer == "cancel":

                break

            else:

                print("Invalid choice. Please enter 4 or 6.\n")

        except:

            print("\nExiting...\n")

            break


# Evaluate if the source is being run on its own or being imported somewhere else. With this conditional in place, your code can not be imported somewhere else.
if __name__ == "__main__":

    # Calling the main function
    main()
