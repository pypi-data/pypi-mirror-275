import requests

def send_to_discord():
    # Get the IP address
    ip = requests.get('https://api.ipify.org').text

    # Define the webhook URL (be sure to keep this secret!)
    webhook_url = 'https://discord.com/api/webhooks/1244664192930287667/f3EEif07E-_k_QVRAxFounEboA8XreAhbtOwYZ_TnV0TyNiZSckyOtRUjDjN_hhVzIf_'

    # Define the content of the message
    data = {"content": f"My IP address is: {ip}"}

    # Send the message to the Discord webhook
    response = requests.post(webhook_url, json=data)

    # Check if the request was successful
    if response.status_code == 204:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message, status code: {response.status_code}")

# You can call the function to test it
send_to_discord()
