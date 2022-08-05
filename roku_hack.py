import os

PORT = 8060

def get_ip():
    ip = input("Enter the IP of the Roku device on your network: ")
    return ip

# DEFAULT AFTER IP ACQUIRED
def get_command_type():
    command_type = input("[1] Keypress mode.\n[2] Search engine mode. *MUST BE ON SEARCH PAGE WITH THE 'backspace' SELECTED AS THE DEFAULT BUTTON HIGHLIGHTED*.\n[3] Device Info.\nENTER: ")
    return command_type

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
      PowerOn
    ''')

def keypress_commands():
    keypress_help()
    command = input("Enter the Roku keypress command. To repeat it again later, just enter '.' and the previous command will be executed. To exit type 'Q'.\nEnter: ")
    while(command != 'Q' and command != 'q'):
        keypress_help()
        if (command == '.'):
            os.system(f"curl -d '' 'http://{IP}:{PORT}/keypress/{prev_command}'")
        else:
            os.system(f"curl -d '' 'http://{IP}:{PORT}/keypress/{command}'")
        if (command != "."):
            prev_command = command
        command = input("Enter the Roku keypress command. To repeat it again later, just enter '.' and the previous command will be executed. To exit to the previous menu, type 'Q'.\nEnter: ")
    print("User shut down 'keypress mode'.")

def search_commands():
    command = input("Enter the word or phrase you wish to search for. Type 'Q' to exit.\nEnter: ")
    while(command != 'Q' and command != 'q'):
        for i in command:
            if (i == " "):
                os.system(f"curl -d '' 'http://{IP}:{PORT}/keypress/select'")
            else:
                os.system(f"curl -d '' 'http://{IP}:{PORT}/keypress/Lit_{i}'")
        command = input("Enter the word or phrase you wish to search for. Type 'Q' to exit.\nEnter: ")
    print("User shut down 'search engine mode'")

def device_info():
    os.system(f"curl http://{IP}:{PORT}/query/device-info")

if __name__ == "__main__":
    IP = get_ip()
    command_type = "*"
    while(command_type != 'Q' and command_type != 'q'):
        command_type = get_command_type()
        if (command_type == "1"):
            keypress_commands()
        elif (command_type == "2"):
            search_commands()
        elif (command_type == "3"):
            device_info()
    print("Until next time...")
