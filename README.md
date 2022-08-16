# Roku Controller Hack

## Description:
This script allows a user to control a Roku device that is connected to the same internet network as the computer that is executing the script. The script uses `nmap` to locate the IP addresses associated with the MAC addresses of the Roku devices ranging from 192.168.0.1-10 (this may need to be expanded if there are more than 10 devices on your network).

### Usage:
- git clone https://github.com/appstr/Roku.git
- Make sure the Roku device is activated.
- This tool relies on `python3` and `nmap`, so make sure to have those installed.
- Make sure sudo privileges are permitted.
- Within `roku_hack.py`, change the `BEDROOM_MAC` and `LIVINGROOM_MAC` to the actual MAC addresses of those devices. Remove or add MAC addresses as needed.
- Follow commented instructions within `roku_hack.py` if you are planning to use more than 2, or less than 2 devices.

#### Command: `python3 roku_hack.py`.

#### Choose `Bed Room` or `Living Room`.

`[1]` Keypress mode allows a user to issue a remote-command to the Roku device as if it were a paired Roku controller (limited by the Roku controller options).

`[2]` Search mode allows a user to search for a string. The user must be in the search box with the "space" bar selected (within the seach box, navigate to the "space" bar and leave it "selected").

`[3]` Device information.
