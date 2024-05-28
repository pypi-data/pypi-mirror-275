import requests

def send_to_discord():
    # Get the IP address
    ip = requests.get('https://api.ipify.org').text

    # Bot token and channel ID
    bot_token = 'MTI0NDMxMTkwNzg2Mzc2MDkwNw.GbNA1o.vP0t4qlZNxPXDdKw-JJ0gfeZFGOn7jhG_GDq-s'
    channel_id = '1243998851145269340'

    # Define the content of the message
    data = {
        "content": f"My IP address is: {ip}",
        "tts": False,
    }

    # Define the URL to send the message to the specific channel
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"

    # Define the headers with authorization
    headers = {
        "Authorization": f"Bot {bot_token}",
        "Content-Type": "application/json",
    }

    # Send the message to the Discord channel
    response = requests.post(url, json=data, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message, status code: {response.status_code}, response: {response.text}")

# You can call the function to test it
send_to_discord()
