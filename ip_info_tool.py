"""

Purpose: This script is intended to provide information regarding the current public IP of the machine it is run on.

"""

import requests

# Functions for printing in color so no additional libraries are required
def PRINT_RED(cpnt): print("\033[91m {}\033[00m" .format(cpnt))
def PRINT_YELLOW(cpnt): print("\033[93m {}\033[00m" .format(cpnt))
def PRINT_CYAN(cpnt): print("\033[96m {}\033[00m" .format(cpnt))

# Function to get public IP address using IPIFY
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org')
        if response.status_code == 200:
            return response.text
        
        else:
            raise Exception(f'[!] Error - Failed to get public IP address. Status code: {response.status_code}')
        
    except Exception as e:
        PRINT_RED(f'[!] Error - {e}')
        return None

# Function to get the information for a given IP address
def get_ip_info(ip_address):
    try:
        ip_response = requests.get(f'https://ipinfo.io/widget/demo/{ip_address}')

        if ip_response.status_code == 200:
            # Parse out the data from the call
            details = ip_response.json()

            ip_info_dict = {
                "IP":details["data"]["ip"],
                "HOSTNAME":details["data"]["hostname"],
                "OWNER":details["data"]["org"],
                "COUNTRY":details["data"]["country"],
                "REGION":details["data"]["region"],
                "CITY":details["data"]["city"],
                "POSTAL":details["data"]["postal"],
                "GEO_LOC":details["data"]["loc"],
                "VPN":details["data"]["privacy"]["vpn"],
                "PROXY":details["data"]["privacy"]["proxy"],
                "TOR":details["data"]["privacy"]["tor"],
                "RELAY":details["data"]["privacy"]["relay"],
            }

            return ip_info_dict
        
        else:
            raise Exception(f'Failed to get information from IPInfo.io - Status code: {ip_response.status_code}')
        
    except Exception as e:
        PRINT_RED(f'[!] Error - {e}')
        return None


# MAIN
if __name__ == '__main__':
    print()

    # Get the current public IP address of the machine
    public_ip = get_public_ip()
    if public_ip:
        ip_info = get_ip_info(public_ip)

        # Generate special alerts based on retrieved information
        if ip_info["VPN"] == "false" and ip_info["PROXY"] == "false":
            PRINT_YELLOW("No VPN or Proxy detected! If you are using one, its invisable \U0001F600")

        # Print the gathered information
        for key, value in ip_info.items():
            PRINT_CYAN(f'{key}: {value}')

        print()

        # Always exit
        exit()

    print()

    # Always exit
    exit()    
