import pyautogui
import keyboard
import os
import sys
import fade
import time
from colorama import Fore

pyautogui.FAILSAFE = False

pyautogui.PAUSE = 0.01  # Set a small pause between actions
pyautogui.MINIMUM_DURATION = 0.01  # Set the smallest possible duration

#AGENT CORDS

#Reyna
x_reyna_1 = 1117
y_reyna_1 = 910

x_reyna_2 = 955
y_reyna_2 = 738

#Neon
x_neon_1 = 796
y_neon_1 = 913

x_neon_2 = 955
y_neon_2 = 738
#Jett
x_jett_1 = 1291
y_jett_1 = 837

x_jett_2 = 955
y_jett_2 = 738

#Razeii
x_raze_1 = 1042
y_raze_1 = 922

x_raze_2 = 955
y_raze_2 = 738

#Phoenix
x_phoenix_1 = 958
y_phoenix_1 = 918

x_phoenix_2 = 955
y_phoenix_2 = 738

#Yoru
x_yoru_1 = 794
y_yoru_1 = 1001

x_yoru_2 = 955
y_yoru_2 = 738

#Iso
x_iso_1 = 953
y_iso_1 = 1010

x_iso_2 = 955
y_iso_2 = 738

#Omen
x_omen_1 = 875
y_omen_1 = 934

x_omen_2 = 916
y_omen_2 = 738


running = False 

def main():
    global running
    print(f""" 
           {Fore.MAGENTA}  ▄█  ███▄▄▄▄      ▄████████     ███        ▄████████  ▄█        ▄██████▄   ▄████████    ▄█   ▄█▄ 
           {Fore.MAGENTA} ███  ███▀▀▀██▄   ███    ███ ▀█████████▄   ███    ███ ███       ███    ███ ███    ███   ███ ▄███▀ 
           {Fore.MAGENTA} ███▌ ███   ███   ███    █▀     ▀███▀▀██   ███    ███ ███       ███    ███ ███    █▀    ███▐██▀   
           {Fore.MAGENTA} ███▌ ███   ███   ███            ███   ▀   ███    ███ ███       ███    ███ ███         ▄█████▀    
           {Fore.MAGENTA} ███▌ ███   ███ ▀███████████     ███     ▀███████████ ███       ███    ███ ███        ▀▀█████▄    
           {Fore.MAGENTA} ███  ███   ███          ███     ███       ███    ███ ███       ███    ███ ███    █▄    ███▐██▄   
           {Fore.MAGENTA} ███  ███   ███    ▄█    ███     ███       ███    ███ ███▌    ▄ ███    ███ ███    ███   ███ ▀███▄ 
           {Fore.MAGENTA} █▀    ▀█   █▀   ▄████████▀     ▄████▀     ███    █▀  █████▄▄██  ▀██████▀  ████████▀    ███   ▀█▀ 
                                                     ▀                                 ▀                                                                                                                                                                             
                              {Fore.LIGHTBLUE_EX}
                                  [0] Exit                        [1] Reyna                                 
                                  [2] Neon                        [3] Jett
                                  [4] Raze                        [5] Phoenix
                                  [6] Yoru                        [7] Iso
                                  [8] Omen                        [9] Credits

    
                                  {Fore.LIGHTMAGENTA_EX}
                   """)

    cmd = input("            Agent>")

    if cmd == "0":
        sys.exit(0)
    if cmd == "1":
        if not running:  # If the loop is not running, start it on 'tab' press
            print("            Press 'tab' in the loading screen (AVOID MOVING YOUR MOUSE IN THIS PART)")
            print("            press 'tab' again after you instalocked your agent")
            while True:
                if keyboard.is_pressed('tab'):  
                    running = True
                    print("            Instalokcing... ")
                    time.sleep(0.2)  # Introduce a small delay
                    break

        while running:  # Loop will run until 'running' is set to False
            pyautogui.moveTo(x_reyna_1, y_reyna_1, duration=0.0001)
            pyautogui.click()
            pyautogui.moveTo(x_reyna_2, y_reyna_2, duration=0.0001)     
            pyautogui.click()

            if keyboard.is_pressed('tab'):  
                running = False 
                print("            instalock ended")
                print("            Press Enter to return to the main menu.")
                input()  # Wait for user input to continue after stopping loop
                onstart()  # Return to the main menu
    if cmd == "2":
        if not running:  # 
            print("            Press 'tab' in the loading screen (AVOID MOVING YOUR MOUSE IN THIS PART)")
            print("            press 'tab' again after you instalocked your agent")
            while True: 
                if keyboard.is_pressed('tab'):
                    running = True
                    print("            Instalokcing... ")
                    time.sleep(0.2)  # Introduce a small delay
                    break

        while running:  # Loop will run until 'running' is set to False
            pyautogui.moveTo(x_neon_1, y_neon_1, duration=0.0001)
            pyautogui.click()
            pyautogui.moveTo(x_neon_2, y_neon_2, duration=0.0001)
            pyautogui.click()

            if keyboard.is_pressed('tab'):  
                running = False
                print("            instalock ended")
                print("            Press Enter to return to the main menu.")
                input()  # Wait for user input to continue after stopping loop
                onstart()  # Return to the main menu


    if cmd == "3":
        if not running:  # 
            print("            Press 'tab' in the loading screen (AVOID MOVING YOUR MOUSE IN THIS PART)")
            print("            press 'tab' again after you instalocked your agent")
            while True:
                if keyboard.is_pressed('tab'):
                    running = True
                    print("            Instalokcing... ")
                    time.sleep(0.2)  # Introduce a small delay
                    break

        while running:  # Loop will run until 'running' is set to False
            pyautogui.moveTo(x_jett_1, y_jett_1, duration=0.0001)
            pyautogui.click()
            pyautogui.moveTo(x_jett_2, y_jett_2, duration=0.0001)
            pyautogui.click()

            if keyboard.is_pressed('tab'):  
                running = False
                print("            instalock ended")
                print("            Press Enter to return to the main menu.")
                input()  # Wait for user input to continue after stopping loop
                onstart()  # Return to the main menu
    if cmd == "4":
        if not running:  # 
            print("            Press 'tab' in the loading screen (AVOID MOVING YOUR MOUSE IN THIS PART)")
            print("            press 'tab' again after you instalocked your agent")
            while True:
                if keyboard.is_pressed('tab'):
                    running = True
                    print("            Instalokcing... ")
                    time.sleep(0.2)  # Introduce a small delay
                    break

        while running:  # Loop will run until 'running' is set to False
            pyautogui.moveTo(x_raze_1, y_raze_1, duration=0.0001)
            pyautogui.click()
            pyautogui.moveTo(x_raze_2, y_raze_2, duration=0.0001)
            pyautogui.click()

            if keyboard.is_pressed('tab'):  
                running = False
                print("            instalock ended")
                print("            Press Enter to return to the main menu.")
                input()  # Wait for user input to continue after stopping loop
                onstart()  # Return to the main menu
    if cmd == "5":
        if not running:  # 
            print("            Press 'tab' in the loading screen (AVOID MOVING YOUR MOUSE IN THIS PART)")
            print("            press 'tab' again after you instalocked your agent")
            while True:
                if keyboard.is_pressed('tab'):
                    running = True
                    print("            Instalokcing... ")
                    time.sleep(0.2)  # Introduce a small delay
                    break

        while running:  # Loop will run until 'running' is set to False
            pyautogui.moveTo(x_phoenix_1, y_phoenix_1, duration=0.0001)
            pyautogui.click()
            pyautogui.moveTo(x_phoenix_2, y_phoenix_2, duration=0.0001)
            pyautogui.click()

            if keyboard.is_pressed('tab'):  
                running = False
                print("            instalock ended")
                print("            Press Enter to return to the main menu.")
                input()  # Wait for user input to continue after stopping loop
                onstart()  # Return to the main menu
    if cmd == "6":
        if not running:  # 
            print("            Press 'tab' in the loading screen (AVOID MOVING YOUR MOUSE IN THIS PART)")
            print("            press 'tab' again after you instalocked your agent")
            while True:
                if keyboard.is_pressed('tab'):
                    running = True
                    print("            Instalokcing... ")
                    time.sleep(0.2)  # Introduce a small delay
                    break

        while running:  # Loop will run until 'running' is set to False
            pyautogui.moveTo(x_yoru_1, y_yoru_1, duration=0.0001)
            pyautogui.click()
            pyautogui.moveTo(x_yoru_2, y_yoru_2, duration=0.0001)
            pyautogui.click()

            if keyboard.is_pressed('tab'):  
                running = False
                print("            instalock ended")
                print("            Press Enter to return to the main menu.")
                input()  # Wait for user input to continue after stopping loop
                onstart()  # Return to the main menu
    if cmd == "7":
        if not running:  # 
            print("            Press 'tab' in the loading screen (AVOID MOVING YOUR MOUSE IN THIS PART)")
            print("            press 'tab' again after you instalocked your agent")
            while True:
                if keyboard.is_pressed('tab'):
                    running = True
                    print("            Instalokcing... ")
                    time.sleep(0.2)  # Introduce a small delay
                    break

        while running:  # Loop will run until 'running' is set to False
            pyautogui.moveTo(x_iso_1, y_iso_1, duration=0.0001)
            pyautogui.click()
            pyautogui.moveTo(x_iso_2, y_iso_2, duration=0.0001)
            pyautogui.click()

            if keyboard.is_pressed('tab'):  
                running = False
                print("            instalock ended")
                print("            Press Enter to return to the main menu.")
                input()  # Wait for user input to continue after stopping loop
                onstart()  # Return to the main menu
    if cmd == "8":
        if not running:  # 
            print("            Press 'tab' in the loading screen (AVOID MOVING YOUR MOUSE IN THIS PART)")
            print("            press 'tab' again after you instalocked your agent")
            while True:
                if keyboard.is_pressed('tab'):
                    running = True
                    print("            Instalokcing... ")
                    time.sleep(0.2)  # Introduce a small delay
                    break

        while running:  # Loop will run until 'running' is set to False
            pyautogui.moveTo(x_omen_1, y_omen_1, duration=0.0001)
            pyautogui.click()
            pyautogui.moveTo(x_omen_2, y_omen_2, duration=0.0001)
            pyautogui.click()

            if keyboard.is_pressed('tab'):  
                running = False
                print("            instalock ended")
                print("            Press Enter to return to the main menu.")
                input()  # Wait for user input to continue after stopping loop
                onstart()  # Return to the main menu
    if cmd == "9":
        banner = f"""
                                 _________                    .___.__  __          
                                 \_   ___ \_______   ____   __| _/|__|/  |_  ______
                                 /    \  \/\_  __ \_/ __ \ / __ | |  \   __\/  ___/
                                 \     \____|  | \/\  ___// /_/ | |  ||  |  \___ \ 
                                  \______  /|__|    \___  >____ | |__||__| /____  >
                                         \/             \/     \/               \/ 
                                           ╔════════════════════════════╗      
                                           ║    telegram : @KOWDO_G     ║     
                                           ║   discord : kowdonowdooo   ║  
                                           ║  https://github.com/KOWDOO ║  
                                           ╚════════════════════════════╝
                                              
             """
        faded_banner = fade.purplepink(banner)
        for x in faded_banner:
             time.sleep(0.0001)
             sys.stdout.write(x)
             sys.stdout.flush()
        
        input()
        onstart()

    else:
        print("            Please make sure you choose an existing command number.")
        print("            Press Enter to Continue...")
        input()
        onstart()
    
        
def onstart():
	os.system("cls && title Valorant Instalock - By kowdo")
	main()

onstart()