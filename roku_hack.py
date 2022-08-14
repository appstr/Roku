import os

# PORT TO CONNECT TO ROKU:
PORT = 8060

# MAC ADRESS(ES):
#Example: BEDROOM_MAC = "d3:0a:5e:00:53:af"
BEDROOM_MAC = "REPLACE THIS TEXT WITH THE ROKU MAC ADDRESS FOR YOUR BEDROOM"
# Comment out the code below this comment if running just 1 device. Continue commenting out lines as directed within get_ip().
# Add another MAC address variable if using more than 2 devices. For more than 2 devices, additional code must be added within get_ip().
LIVINGROOM_MAC = "REPLACE THIS TEXT WITH THE ROKU MAC ADDRESS FOR YOUR LIVINGROOM"

# DEFAULT AFTER IP ACQUIRED
def get_command_type():
    command_type = input("[1] Keypress mode.\n[2] Search engine mode. *MUST BE ON SEARCH PAGE WITH THE 'backspace' SELECTED AS THE DEFAULT BUTTON HIGHLIGHTED*.\n[3] Device Info.\n[Q] Quit/exit.\nENTER: ")
    return command_type

# Scanning network 192.168.0.1-10 using nmap to acquire IP's associated with the hard-coded MAC addresses.
def get_ip():
    # Creating IP-Address storage files.
    os.system('touch bed_room_ip.txt')
    # Comment out the code below this line if running just 1 device. For more than 2 devices, duplicate the code below and change the file name to something unique.
    os.system('touch living_room_ip.txt')

    print('\nScanning your Roku devices...\n')

    # Change IP-Address and IP range if your network is different.
    # Scanning IP's 192.168.0.1 - 192.168.9.10
    os.system('sudo nmap 192.168.0.1-10 --min-rate=1000 -T4 -o tmp.txt')
    # Disecting the response into files and detecting the text containing the IP-Addresses which correspond to the MAC addresses hardcoded above.
    os.system(f'awk -v RS= "/{BEDROOM_MAC}/" tmp.txt |grep 192.168 | cut -d " " -f 5 >> bed_room_ip.txt')
    # Comment out code below this line if running just 1 device. Duplicate the code below and replace the file name with the unique file name created if using more than 2 devices.
    os.system(f'awk -v RS= "/{LIVINGROOM_MAC}/" tmp.txt |grep 192.168 | cut -d " " -f 5 >> living_room_ip.txt')

    os.system('clear')
    # Assigning IP-Addresses to variables, then deleting the files created.
    with open('bed_room_ip.txt', 'r') as file:
        bed_room_ip = file.read().rstrip()
    # Comment out code below this line if running just 1 device. Duplicate the code and replace with unique file and variable name if running more than 2 devices.
    with open('living_room_ip.txt', 'r') as file:
        living_room_ip = file.read().rstrip()

    # Add or remove file names as needed.
    os.system("rm -rf tmp.txt bed_room_ip.txt living_room_ip.txt")
    # User is given option of either the Bed Room or Living Room device. Add or remove options as needed.
    chosen_ip = input(f'[1] Bed Room\n[2] Living Room\nEnter: ')
    # If using just 1 device, comment out the elif portion. If using more than 2 devices, add another elif that corresponds to the chosen_ip input.
    if (chosen_ip == "1"):
        chosen_ip = bed_room_ip
    elif (chosen_ip == "2"):
        chosen_ip = living_room_ip
    return chosen_ip

# Commands that can be ran in 'keypress mode'.
def keypress_help():
    print('''
      Home
      Rev
      Fwd
      Play
      Select
      Left
      Right
      Down
      Up
      Back
      InstantReplay
      Info
      Backspace
      Search
      Enter
      VolumeDown
      VolumeMute
      VolumeUp
      PowerOff
      PowerOn (Only works if the Roku has just recently been turned off.)
    ''')

# Get remote keypress command.
def get_keypress_command():
    command = input("Enter the Roku keypress command. To repeat it again later, just enter '.' and the previous command will be executed. To exit to the previous menu, type 'Q'.\nEnter: ")
    return command

# Running Roku remote keypress commands.
def keypress_commands():
    keypress_help()
    command = get_keypress_command().lower()
    while(command != 'q'):
        keypress_help()
        if (command == '.'):
            os.system(f"curl -d '' 'http://{IP}:{PORT}/keypress/{prev_command}'")
        else:
            os.system(f"curl -d '' 'http://{IP}:{PORT}/keypress/{command}'")
        if (command != "."):
            prev_command = command
        command = get_keypress_command().lower()
    print("User shut down 'keypress mode'.\n")

# Get search input.
get_search_input():
    search_input = input("Enter the word or phrase you wish to search for. Type 'Q' to exit.\nEnter: ")
    return search_input

# Searches for a string that is input from the user. The "space" button needs to be selected on the screen, otherwise there will be no spacing between the words.
def search_commands():
    search_input = get_search_input()
    while(search_input != 'Q' and search_input != 'q'):
        for i in search_input:
            if (i == " "):
                os.system(f"curl -d '' 'http://{IP}:{PORT}/keypress/select'")
            else:
                os.system(f"curl -d '' 'http://{IP}:{PORT}/keypress/Lit_{i}'")
        search_input = get_search_input()
    print("User shut down 'search engine mode'.\n")

# Shows Roku device information.
def device_info():
    os.system(f"curl http://{IP}:{PORT}/query/device-info")

if __name__ == "__main__":
    IP = get_ip()
    command_type = "*"
    while(command_type != 'q' and IP != 'q' and IP != 'Q'):
        command_type = get_command_type().lower()
        if (command_type == "1"):
            keypress_commands()
        elif (command_type == "2"):
            search_commands()
        elif (command_type == "3"):
            device_info()
    print("Until next time...")
