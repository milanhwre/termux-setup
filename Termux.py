#__________________| SCRIPT INFO |__________________#
# SCRIPT MAKED BY ANISH
# PYTHON VERSION : 3.11
# GITHUB : ANISH HWRE
# TEAM : ANISH
#_______________| IMPORT MODULES |________________#
import os
os.system('pip install requests');os.system('pip install rich')
import os,time,sys,datetime,rich,requests 
from rich.console import Console
from rich import print
from rich.panel import Panel
from time import localtime as lt
print(Panel("[bold black]【[white]•[bold black]】[blue_violet] INSTALLED SYSTEM", style="bold bright_black",title="<[bold white reverse] WELCOME [/bold white reverse]>"));time.sleep(1.5)
sys.stdout.write('\x1b]2; ANONYMOUS CYBER™🌻🔥💯\x07')
#__________________| COLOUR |__________________#
A = '\x1b[1;97m';Y = '\033[1;33m';N1 = '\033[1;92m\x1b[38;5;208m';N2 = '\033[1;92m\x1b[38;5;209m';N3 = '\033[1;92m\x1b[38;5;210m';N4 = '\033[1;92m\x1b[38;5;211m'
#______________| SOME METHOD |_______________#
def _clear_():
    if "linux" in sys.platform.lower():os.system("clear");logo()
    elif "win" in sys.platform.lower():os.system("cls");logo()
def clear():
	_clear_();loadinglisen();_clear_()
#__________| DATE AND TIME OR IP |______________#
ip = requests.get("https://api.ipify.org").text
dic = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July', '8': 'August','9': 'September', '10': 'October', '11': 'November', '12': 'December'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
date = str(tgl) + f'/' + str(bln) + f'/' + str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx - 12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
times = time.strftime("%H:%M") + " " + tag
#_______________| YOUR DETAILS |______________#
def __details__():
	print(Panel(f"[bold black]【[white]•[bold black]】[dark_cyan]YOUR IP      [white]➤  [steel_blue1]{ip} \n[bold black]【[white]•[bold black]】[dark_cyan]TODAY TIME   [white]➤  [steel_blue1]{times} \n[bold black]【[white]•[bold black]】[dark_cyan]TODAY DATE   [white]➤  [steel_blue1]{date}",style="bold bright_black",title="<[bold white reverse] YOUR INFO [/bold white reverse]>"))
#__________________| LOADING SYSTEM |__________________#
def loadinglisen():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.009)
        sys.stdout.write(f"\r\t {Y}Loading{N1}.{N2}.{N3}.{N4}.{A} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print()
#__________________| LOGO |__________________#
def logo():
    print(" ");print(Panel("[bold red]● [bold yellow]● [bold green]●\n[green1] ╺┳╸┏━╸┏━┓┏┳┓╻ ╻╻ ╻   ┏━┓┏━╸╺┳╸╻ ╻┏━┓\n[spring_green2]  ┃ ┣╸ ┣┳┛┃┃┃┃ ┃┏╋┛   ┗━┓┣╸  ┃ ┃ ┃┣━┛\n[spring_green11]  ╹ ┗━╸╹┗╸╹ ╹┗━┛╹ ╹   ┗━┛┗━╸ ╹ ┗━┛╹  ", style="bold bright_black",title="<[bold white reverse] CODING BY - U7P4L 1N [/bold white reverse]>"))
    print(Panel("[bold black]【[white]•[bold black]】[bold yellow] DEVELOPER   [white]➤ [dark_olive_green2]U7P4L 1N  \n[bold black]【[white]•[bold black]】[bold yellow] GITHUB      [white]➤ [dark_olive_green2]U7P4L-IN \n[bold black]【[white]•[bold black]】[bold yellow] VERSION     [white]➤ [dark_olive_green2]1.0.2\n[bold black]【[white]•[bold black]】[bold yellow] TELEGRAM    [white]➤ [dark_olive_green2]t.me/TheU7p4lArmyX\n[bold black]【[white]•[bold black]】[bold yellow] TOOL'S NAME [white]➤ [bold purple reverse] TERMUX BESIC SETUP ", style="bold bright_black"))
#__________________| SETUP LOGO |__________________#
def logo2():
    print(" ");print(Panel("[bold red]● [bold yellow]● [bold green]●\n\n[dark_orange3]   ╺┳╸┏━╸┏━┓┏┳┓╻ ╻╻╻   ┏━┓┏━╸╺┳╸╻ ╻┏━┓\n[indian_red]    ┃ ┣╸ ┣┳┛┃┃┃┃ ┃┏╋┛  ┗━┓┣╸  ┃ ┃ ┃┣━┛\n[hot_pink3]    ╹ ┗━╸╹┗╸╹ ╹┗━┛╹ ╹  ┗━┛┗━╸ ╹ ┗━┛╹\n\n[hot_pink2]   ┏━╸╻ ╻╻  ╻     ┏━╸╻┏┓╻╻┏━┓╻ ╻┏━╸╺┳┓\n[orchid]   ┣╸ ┃ ┃┃  ┃     ┣╸ ┃┃┗┫┃┗━┓┣━┫┣╸  ┃┃\n[orange3]   ╹  ┗━┛┗━╸┗━╸   ╹  ╹╹ ╹╹┗━┛╹ ╹┗━╸╺┻┛", style="bold bright_black"))
#__________________| MAIN MENU |__________________#
def menu():
    clear()
    os.system('xdg-open https://github.com/Anish-IN')
    clear()
    print(Panel("[bold black]【[white]01[bold yellow]/[white]A[bold black]】[dark_slate_gray3]TERMUX BESIC PKG SETUP\n[bold black]【[white]02[bold yellow]/[white]B[bold black]】[dark_slate_gray3]ADD BANNER IN TERMUX \n[bold black]【[white]03[bold yellow]/[white]C[bold black]】[dark_slate_gray3]REPORT FOR ANY BUGS\n[bold black]【[white]00[bold yellow]/[white]X[bold black]】[red1]EXIT PROGRAMME", style="bold bright_black",title="<[bold white reverse] MAIN MENU [/bold white reverse]>"))
    option = Console().input("[bold bright_black]   ╰─>[white] ")
    if option in ['1','01','A','a']:set_up()
    elif option in ['2','02','B','b']:clear();os.system('rm -rf OP-BANNER && git clone https://github.com/U7P4L-IN/OP-BANNER.git && cd OP-BANNER && python2 Banner1.py')
    elif option in ['3','03','C','c']:admin()
    elif option in ['00','0','X','x']:print(Panel("[bold black]【[white]=[bold black]】[bold blue]EXIT DONE ...!!!\n[bold black]【[white]=[bold black]】[bold blue]THANKS FOR USING OUR TOOLS ...!!!", style="bold bright_black",title="<[bold white reverse] EXIT </> [/bold white reverse]>"))
    else:
        print(Panel("[bold black]【[white]=[bold black]】 [bold blue]OPTION NOT FOUND IN MENU..",title="<[bold white reverse] EXIT ~ [/bold white reverse]>"));menu()
#__________________| ADMIN INFO |__________________#
def admin():
    clear()
    print(Panel("[bold black]【[white]01[bold yellow]/[white]A[bold black]】[cyan3]JOIN FB PAGE\n[bold black]【[white]02[bold yellow]/[white]B[bold black]】[cyan3]JOIN FB GROUP\n[bold black]【[white]03[bold yellow]/[white]C[bold black]】[cyan3]JOIN TELEGRAM\n[bold black]【[white]04[bold yellow]/[white]D[bold black]】[cyan3]FOLLOW GITHUB\n[bold black]【[white]00[bold yellow]/[white]X[bold black]】[red1]BACK TO MAIN MENU", style="bold bright_black",title="<[bold white reverse] OUR COMMUNITY [/bold white reverse]>"))
    option = Console().input("[bold bright_black]   ╰─>[white] ")
    if option in ['1','01','A','a']:os.system('xdg-open https://www.facebook.com/profile.php?id=100003658223632');menu()
    elif option in ['2','02','B','b']:os.system('xdg-open https://www.facebook.com/profile.php?id=100003658223632');menu()
    elif option in ['3','03','C','c']:os.system('xdg-open https://t.me/Anish');menu()
    elif option in ['4','04','D','d']:os.system('xdg-open https://github.com/Anish-IN');menu()
    elif option in ['0','00','X','x']:menu()
    else:
        print(Panel("[bold black]【[white]=[bold black]】 [bold blue]BYE BYE BRO..", style="bold bright_black",title="<[bold white reverse] EXIT ~ [/bold white reverse]>"));menu()
#__________________| SETUP MENU |__________________#
def set_up():
    clear();__details__()
    print(Panel("[bold black]【[white]01[bold yellow]/[white]A[bold black]】[medium_purple1]TERMUX BASIC SETUP\n[bold black]【[white]02[bold yellow]/[white]B[bold black]】[medium_purple1]TERMUX FULL SETUP\n[bold black]【[white]00[bold yellow]/[white]X[bold black]】[red1]BACK TO MAIN MENU", style="bold bright_black",title="<[bold white reverse] SETUP MENU [/bold white reverse]>"))
    option = Console().input("[bold bright_black]   ╰─>[white] ")
    if option in ['1','01','A','a']:basic_setup()
    elif option in ['2','02','B','b']:full_setup()
    elif option in ['00','0','X','x']:menu()
    else:
        print(Panel("[bold black]【[white]=[bold black]】 [bold blue]OPTION NOT FOUND IN MENU..",title="<[bold white reverse] EXIT ~ [/bold white reverse]>"));menu()
#__________________| BASIC SETUP |__________________#
def basic_setup():
    print(Panel("[bold black]【[white]•[bold black]】[blue_violet]INSTALLING START IN 3 SEC...",style="bold bright_black"));time.sleep(3)
    print("\n\n");print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2] PKG[light_green] UPDATE ",style="bold bright_black"))
    os.system("pkg update")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2] PKG[light_green] UPGRADE ",style="bold bright_black"))
    os.system("pkg upgrade")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PYTHON ",style="bold bright_black"))
    os.system("pkg install python -y")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PYTHON2 ",style="bold bright_black"))
    os.system("pkg install python2 -y")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PYTHON3 ",style="bold bright_black"))
    os.system("pkg install python3")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] TMUX ",style="bold bright_black"))
    os.system("apt install tmux")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] REQUESTS ",style="bold bright_black"))
    os.system("pip install requests")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] REQUESTS ",style="bold bright_black"))
    os.system("pip2 install requests")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PYCURL ",style="bold bright_black"))
    os.system("pip install pycurl")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] MECHANIZE ",style="bold bright_black"))
    os.system("pip2 install mechanize")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] BS4 ",style="bold bright_black"))
    os.system("pip install bs4")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] BS4 ",style="bold bright_black"))
    os.system("pip2 install bs4")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] RICH ",style="bold bright_black"))
    os.system("pip install rich")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] RUBY ",style="bold bright_black"))
    os.system("pip install pycurl")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] LOLCAT ",style="bold bright_black"))
    os.system("gem install lolcat")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PHP ",style="bold bright_black"))
    os.system("pip install php")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] LOLCAT ",style="bold bright_black"))
    os.system("pip install lolcat")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] FETURES ",style="bold bright_black"))
    os.system("pip install futures")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] HTTPX ",style="bold bright_black"))
    os.system("pkg install httpx")
    clear();time.sleep(3);logo2()
#__________________| FULL SETUP |__________________#
def full_setup():
    print(Panel("[bold black]【[white]•[bold black]】[blue_violet]INSTALLING START IN 3 SEC...",style="bold bright_black"));time.sleep(3)
    print("\n\n");print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2] PKG[light_green] UPDATE ",style="bold bright_black"))
    os.system("pkg update")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2] PKG[light_green] UPGRADE ",style="bold bright_black"))
    os.system("pkg upgrade")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PYTHON ",style="bold bright_black"))
    os.system("pkg install python")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PYTHON2 ",style="bold bright_black"))
    os.system("pkg install python2")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PYTHON3 ",style="bold bright_black"))
    os.system("pkg install python3")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] WGET ",style="bold bright_black"))
    os.system("pkg install wget")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PYTHON PIP ",style="bold bright_black"))
    os.system("pkg install python-pip")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] FISH ",style="bold bright_black"))
    os.system("pkg install fish")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] RUBY ",style="bold bright_black"))
    os.system("pkg install ruby")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] HELP ",style="bold bright_black"))
    os.system("pkg install help")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] DNSUTILS ",style="bold bright_black"))
    os.system("pkg install dnsutils  ")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PHP ",style="bold bright_black"))
    os.system("pkg install php")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PERL ",style="bold bright_black"))
    os.system("pkg install perl")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] LUA ",style="bold bright_black"))
    os.system("pkg install lua")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PARALLEL ",style="bold bright_black"))
    os.system("pkg install parallel")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] NMAP ",style="bold bright_black"))
    os.system("pkg install nmap")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] BASH ",style="bold bright_black"))
    os.system("pkg install bash")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] CLANG ",style="bold bright_black"))
    os.system("pkg install clang")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] NANO ",style="bold bright_black"))
    os.system("pkg install nano")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] W3M ",style="bold bright_black"))
    os.system("pkg install w3m")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] HYDRA ",style="bold bright_black"))
    os.system("pkg install hydra")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] COWSAY ",style="bold bright_black"))
    os.system("pkg install cowsay")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] CURL ",style="bold bright_black"))
    os.system("pkg install curl")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] TAR ",style="bold bright_black"))
    os.system("pkg install tar")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] ZIP ",style="bold bright_black"))
    os.system("pkg install zip")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] UNZIP ",style="bold bright_black"))
    os.system("pkg install unzip")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] TOR ",style="bold bright_black"))
    os.system("pkg install tor")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] NET-TOOLS ",style="bold bright_black"))
    os.system("pkg install net-tools")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] SUDO ",style="bold bright_black"))
    os.system("pkg install sudo")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] WIRESHARK ",style="bold bright_black"))
    os.system("pkg install wireshark")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] TMUX ",style="bold bright_black"))
    os.system("apt install tmux")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] CRUNCH ",style="bold bright_black"))
    os.system("pkg install crunch")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] WGETRC ",style="bold bright_black"))
    os.system("pkg install wgetrc")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] WCALC ",style="bold bright_black"))
    os.system("pkg install wcalc")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] OPENSSL ",style="bold bright_black"))
    os.system("pkg install openssl")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] OPENSSL-TOOL ",style="bold bright_black"))
    os.system("pkg install openssl-tool")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] BMON ",style="bold bright_black"))
    os.system("pkg install bmon")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] VPN ",style="bold bright_black"))
    os.system("pkg install vpn")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] UNRAR ",style="bold bright_black"))
    os.system("pkg install unrar")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] TOILET ",style="bold bright_black"))
    os.system("pkg install toilet")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PROOT ",style="bold bright_black"))
    os.system("pkg install proot")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] NET TOOLS ",style="bold bright_black"))
    os.system("pkg install net-tools")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] VIM ",style="bold bright_black"))
    os.system("pkg install vim")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] VIN PYTHON ",style="bold bright_black"))
    os.system("pkg install vim-python")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] IRED ",style="bold bright_black"))
    os.system("pkg install ired")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] GOACCESS ",style="bold bright_black"))
    os.system("pkg install goaccess")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] GOLAND ",style="bold bright_black"))
    os.system("pkg install golang")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] KIBI ",style="bold bright_black"))
    os.system("pkg install kibi")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] TSU ",style="bold bright_black"))
    os.system("pkg install tsu")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] MTOOLS ",style="bold bright_black"))
    os.system("pkg install mtools")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] FILE ",style="bold bright_black"))
    os.system("pkg install file")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] VIS ",style="bold bright_black"))
    os.system("pkg install vis")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PASS ",style="bold bright_black"))
    os.system("pkg install pass")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PIC ",style="bold bright_black"))
    os.system("pkg install pick")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] CHROOT ",style="bold bright_black"))
    os.system("pkg install chroot")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] MACCHANGER ",style="bold bright_black"))
    os.system("pkg install macchanger")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] NINJA ",style="bold bright_black"))
    os.system("pkg install ninja")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] ELIXIR ",style="bold bright_black"))
    os.system("pkg install elixir")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] SWIFT ",style="bold bright_black"))
    os.system("pkg install swift")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] XMLSTARLET ",style="bold bright_black"))
    os.system("pkg install xmlstarlet")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] FAKEROOT ",style="bold bright_black"))
    os.system("pkg install fakeroot")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] TEXTINFO ",style="bold bright_black"))
    os.system("pkg install texinfo")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] NETCET ",style="bold bright_black"))
    os.system("pkg install netcat")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] WREN ",style="bold bright_black"))
    os.system("pkg install wren")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] GETLING ",style="bold bright_black"))
    os.system("pkg install gatling")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] CVS ",style="bold bright_black"))
    os.system("pkg install cvs")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] FFMPEG ",style="bold bright_black"))
    os.system("pkg install ffmpeg")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] SCREEN ",style="bold bright_black"))
    os.system("pkg install screen")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] NEOFETCH ",style="bold bright_black"))
    os.system("pkg install neofetch")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] MARIADB ",style="bold bright_black"))
    os.system("pkg install mariadb")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PIOLISP ",style="bold bright_black"))
    os.system("pkg install picolisp")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] CMATRIX ",style="bold bright_black"))
    os.system("pkg install cmatrix")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] DROPBEAR ",style="bold bright_black"))
    os.system("pkg install dropbear")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] OPENSSH ",style="bold bright_black"))
    os.system("pkg install openssh")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PYTHON PIP ",style="bold bright_black"))
    os.system("pkg install python-pip")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] WGET ",style="bold bright_black"))
    os.system("pip2 install wget")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] BS4 ",style="bold bright_black"))
    os.system("pip install bs4")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] BS4 ",style="bold bright_black"))
    os.system("pip2 install bs4")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] REQUESTS ",style="bold bright_black"))
    os.system("pip install requests")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] REQUESTS ",style="bold bright_black"))
    os.system("pip2 install requests")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] MECHANIZE ",style="bold bright_black"))
    os.system("pip install mechanize")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PIP2 MECHANIZE ",style="bold bright_black"))
    os.system("pip2 install mechanize")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PHP ",style="bold bright_black"))
    os.system("pip install php")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] PIP2 PHP ",style="bold bright_black"))
    os.system("pip2 install php")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] LOLCAT ",style="bold bright_black"))
    os.system("gem install lolcat")
    print(Panel("\t[bold black]【[white]•[bold black]】[sea_green2]INSTALLING[light_green] WGETRC ",style="bold bright_black"))
    os.system('pip insall pytube')
    clear();time.sleep(3);logo2()

menu()
#__________________| FINISHED |__________________#
