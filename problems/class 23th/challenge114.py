import requests
green = '\033[1;32m'
red = '\033[1;31m'
color_reset = '\033[m'
def url_up(link):
    try:
        response = requests.head(link)
        if response.status_code == 200:
            return f"{green}up{color_reset}"
        else:
            return f"{red}down{color_reset}"
    except requests.ConnectionError as e:
        return f"\033[1;31m{e}\033[m"
    
url = "http://www.pudim.com.br"
ok = url_up(url)
print(f"the {url} is {ok}")