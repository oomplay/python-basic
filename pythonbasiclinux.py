import time
import os
cls = lambda:os.system("clear")
cls()
LOADING = r'''
 _                    _ _              
| |    ___   __ _  __| (_)_ __   __ _  
| |   / _ \ / _` |/ _` | | '_ \ / _` | 
| |__| (_) | (_| | (_| | | | | | (_| | 
|_____\___/ \__,_|\__,_|_|_| |_|\__, | 
                                |___/  
'''
LOADING1 = r'''
 _                    _ _                 
| |    ___   __ _  __| (_)_ __   __ _     
| |   / _ \ / _` |/ _` | | '_ \ / _` |    
| |__| (_) | (_| | (_| | | | | | (_| |  _ 
|_____\___/ \__,_|\__,_|_|_| |_|\__, | (_)
                                |___/     
'''
LOADING2 = r'''
 _                    _ _                      
| |    ___   __ _  __| (_)_ __   __ _          
| |   / _ \ / _` |/ _` | | '_ \ / _` |         
| |__| (_) | (_| | (_| | | | | | (_| |  _   _  
|_____\___/ \__,_|\__,_|_|_| |_|\__, | (_) (_) 
                                |___/          
'''
LOADING3 = r'''
 _                    _ _                         
| |    ___   __ _  __| (_)_ __   __ _             
| |   / _ \ / _` |/ _` | | '_ \ / _` |            
| |__| (_) | (_| | (_| | | | | | (_| |  _   _   _ 
|_____\___/ \__,_|\__,_|_|_| |_|\__, | (_) (_) (_)
                                |___/             
'''

DONE1 = r'''
 ____  _   _  ____ ____ _____ ____ ____    _     ___    _    ____  ____ ___ _   _  ____ 
/ ___|| | | |/ ___/ ___| ____/ ___/ ___|  | |   / _ \  / \  |  _ \|  _ \_ _| \ | |/ ___|
\___ \| | | | |  | |   |  _| \___ \___ \  | |  | | | |/ _ \ | | | | | | | ||  \| | |  _ 
 ___) | |_| | |__| |___| |___ ___) |__) | | |__| |_| / ___ \| |_| | |_| | || |\  | |_| |
|____/ \___/ \____\____|_____|____/____/  |_____\___/_/   \_\____/|____/___|_| \_|\____|
'''

LOGO = r'''
                         ___                                            
                        (   )                                           
 ___  ___  ___   .--.    | |    .--.      .--.    ___ .-. .-.     .--.  
(   )(   )(   ) /    \   | |   /    \    /    \  (   )   '   \   /    \ 
 | |  | |  | | |  .-. ;  | |  |  .-. ;  |  .-. ;  |  .-.  .-. ; |  .-. ;
 | |  | |  | | |  | | |  | |  |  |(___) | |  | |  | |  | |  | | |  | | |
 | |  | |  | | |  |/  |  | |  |  |      | |  | |  | |  | |  | | |  |/  |
 | |  | |  | | |  ' _.'  | |  |  | ___  | |  | |  | |  | |  | | |  ' _.'
 | |  ; '  | | |  .'.-.  | |  |  '(   ) | '  | |  | |  | |  | | |  .'.-.
 ' `-'   `-' ' '  `-' /  | |  '  `-' |  '  `-' /  | |  | |  | | '  `-' /
  '.__.'.__.'   `.__.'  (___)  `.__,'    `.__.'  (___)(___)(___) `.__.' 
                                                                        
                                                                        
 ___                                                                    
(   )                                                                   
 | |_       .--.                                                        
(   __)    /    \                                                       
 | |      |  .-. ;                                                      
 | | ___  | |  | |                                                      
 | |(   ) | |  | |                                                      
 | | | |  | |  | |                                                      
 | ' | |  | '  | |                                                      
 ' `-' ;  '  `-' /                                                      
  `.__.    `.__.'                                                       
                                                                        
                                                                        
                      ___       ___                                     
                     (   )     (   )                                    
   .-..    ___  ___   | |_      | | .-.     .--.    ___ .-.             
  /    \  (   )(   ) (   __)    | |/   \   /    \  (   )   \            
 ' .-,  ;  | |  | |   | |       |  .-. .  |  .-. ;  |  .-. .            
 | |  . |  | |  | |   | | ___   | |  | |  | |  | |  | |  | |            
 | |  | |  | '  | |   | |(   )  | |  | |  | |  | |  | |  | |            
 | |  | |  '  `-' |   | | | |   | |  | |  | |  | |  | |  | |            
 | |  ' |   `.__. |   | ' | |   | |  | |  | '  | |  | |  | |            
 | `-'  '   ___ | |   ' `-' ;   | |  | |  '  `-' /  | |  | |            
 | \__.'   (   )' |    `.__.   (___)(___)  `.__.'  (___)(___)           
 | |        ; `-' '                                                     
(___)        .__.'                                                      
'''

HELP1 = ('1.Update && Upgrade -y');HELP2 = ('2.Ping 1.1.1.1 TEST');HELP3 = ('3.3x-ui Install');HELP4 = ('4.NoT')
#Link
xuiurl = "https://raw.githubusercontent.com/mhsanaei/3x-ui/master/install.sh"


print(LOADING),time.sleep(0.3),cls()
print(LOADING1),time.sleep(0.3),cls()
print(LOADING2),time.sleep(0.3),cls()
print(LOADING3),time.sleep(0.3),cls()

print(LOADING),time.sleep(0.3),cls()
print(LOADING1),time.sleep(0.3),cls()
print(LOADING2),time.sleep(0.3),cls()
print(LOADING3),time.sleep(0.3),cls()
print(DONE1),time.sleep(1),cls()
print(LOGO),time.sleep(1.5),cls()
time.sleep(0.2)
print(HELP1),print(HELP2),print(HELP3),print(HELP4)
H_NUM = int(input("Enter Number 1-4 : "))
if H_NUM == 1:
  print("Update && Upgrade -y"),time.sleep(1.5),cls()
  print("RUN >>> sudo apt update && sudo apt upgrade -y"),time.sleep(1.5),cls()
  os.system("sudo apt update && sudo apt upgrade -y")
elif H_NUM == 2:
  print("Ping 1.1.1.1 TEST"),time.sleep(1.5),cls()
  time.sleep(0.3)
  print(">>>ctrl c for stop ping<<<"),time.sleep(2),cls()
  print("RUN >>> ping 1.1.1.1"),time.sleep(1.5),cls()
  os.system(f"ping 1.1.1.1 ")
elif H_NUM == 3:
  print("3.3x-ui Install"),time.sleep(1.5),cls()
  os.system(f"wget {xuiurl}")
  time.sleep(0.3)
  os.system("bash ./install.sh")
  time.sleep(0.3)
  os.system("rm -r install.sh")

elif H_NUM == 4:
  print("YES THAT IS N O T ")
else:
    print('Try Again')

