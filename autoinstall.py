import time
import os
cls = lambda:os.system("clear")
cls()

LOGO = r'''
///    ___           _        _ _       _   _             
///   |_ _|_ __  ___| |_ __ _| | | __ _| |_(_) ___  _ __  
///    | || '_ \/ __| __/ _` | | |/ _` | __| |/ _ \| '_ \ 
///    | || | | \__ \ || (_| | | | (_| | |_| | (_) | | | |
///   |___|_| |_|___/\__\__,_|_|_|\__,_|\__|_|\___/|_| |_|
'''
googlechrome = 'https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb'
dockerinstall = ('curl -Ls https://get.docker.com > dockerinstall.sh')

RUN1 = ('Run auto install ');RUN2 = ('Run in 3');RUN3 = ('Run in 2');RUN4 = ('Run in 1');RUN5 = ('Run Script install');RUN6 =('SUCCESS SCRIPT ! ! !')
OSshow1 = ('1. Neofetch on Ubuntu & Debian');OSshow2 = ('2. Google Chrome on Linux');OSshow3 = ('3. Install Docker');OSshow4 = ('4. Uninstall CentOS');OSshow5 = ('5. openSUSE')
print(LOGO),time.sleep(3),cls()
print(OSshow1),print(OSshow2),print(OSshow3)#,print(OSshow4),print(OSshow5)
OSTPYE = int(input('Enter Number : '))
if OSTPYE == 1:
  
  print(RUN1),time.sleep(0.5),cls()
  print(RUN2),time.sleep(0.5),cls()
  print(RUN3),time.sleep(0.5),cls()
  print(RUN4),time.sleep(0.5),cls()
  print(RUN5),time.sleep(0.5),cls()
  os.system('sudo apt update && sudo apt upgrade -y'),time.sleep(0.3)
  os.system('sudo apt-get install neofetch -y'),time.sleep(0.3)
  os.system('neofetch'),time.sleep(0.3)




elif OSTPYE == 2:
  print(RUN1),time.sleep(0.5),cls()
  print(RUN2),time.sleep(0.5),cls()
  print(RUN3),time.sleep(0.5),cls()
  print(RUN4),time.sleep(0.5),cls()
  print(RUN5),time.sleep(0.5),cls()
  os.system('sudo apt update && sudo apt upgrade -y'),time.sleep(0.3)
  os.system('sudo apt install wget -y'),time.sleep(0.3)
  os.system(f'wget {googlechrome}'),time.sleep(0.3)
  os.system('sudo dpkg -i google-chrome-stable_current_amd64.deb'),time.sleep(0.3)
  os.system('google-chrome'),time.sleep(0.3)
elif OSTPYE == 3:
  print(RUN1),time.sleep(0.5),cls()
  print(RUN2),time.sleep(0.5),cls()
  print(RUN3),time.sleep(0.5),cls()
  print(RUN4),time.sleep(0.5),cls()
  print(RUN5),time.sleep(0.5),cls()
  os.system('sudo apt update && sudo apt upgrade -y'),time.sleep(0.3)
  os.system('sudo apt install curl -y'),time.sleep(0.3)
  os.system(f'{dockerinstall}'),time.sleep(0.3)
  os.system('sudo bash dockerinstall.sh'),time.sleep(0.3)
  os.system('rm -r dockerinstall.sh'),time.sleep(0.3)
  os.system(f'echo {RUN6}'),time.sleep(0.3)
  os.system('clear')

else:
    print('Try Again')
