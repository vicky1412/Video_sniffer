import requests
import re
import os
import time
from tkinter import messagebox
import tkinter
import subprocess
from colorama import init, Fore, Style




subprocess.call("title Video Sniffer", shell=True)


def progressbar(iteration, total, decimals=1, length=100, fill='█'):

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    x = float(percent)
    if x > 100:
        percent = "100.0"
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r'+"downloading"+"|"+bar+"|" + percent + "%",end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()


def main():

    print()
    print()
    print("          ""__     ___     _              ____        _  __  __           ")
    print("          ""\ \   / (_) __| | ___  ___   / ___| _ __ (_)/ _|/ _| ___ _ __")
    print("          "" \ \ / /| |/ _` |/ _ \/ _ \  \___ \| '_ \| | |_| |_ / _ \ '__|")
    print("          ""  \ V / | | (_| |  __/ (_) |  ___) | | | | |  _|  _|  __/ |")
    print("          ""   \_/  |_|\__,_|\___|\___/  |____/|_| |_|_|_| |_|  \___|_| ")
    print()
    print()

    init(convert=True)
    print(Fore.GREEN + "Enter the Section No : " + Style.RESET_ALL,end="")
    section = int(input())-1


    print()

    for i in range(30):
        pass_url = "https://www.learningcrux.com/video/ccnp-allin1-video-boot-camp-with-chris-bryant/"+str(section)+"/" + str(i)
        response = requests.get(pass_url)
        source_page = response.text
        if "Page Not Found!" in source_page or "404 Error" in source_page:
            break

        # Pattern to match in source page for (tile and filename)
        pattern1 = "(?:src=')(.*?sort')"
        if section+1 == 1:
            pattern2 = "(?:CCNP All-In-1 Video Boot Camp Preview: Let&#39;s Go!).* [^<]*"
        elif section+1 <13:
            pattern2 = "(?:CCNP SWITCH 300-115).* [^<]*"
        elif section+1 <25:
            pattern2 = "(?:CCNP ROUTE 300-101:).* [^<]*"
        elif section+1 <33:
            pattern2 = "(?:CCNP TSHOOT 300-135:).* [^<]*"
        else:
            dict = {33: "Your Free CCNA Security 210-260 Course Starts HERE!", 34: "CCNA Security 210-260, Section 2", 35: "CCNA Security 210-260: Privilege Levels", 36: "CCNA Security 210-160: Protecting The Control Plane", 37: "CCNA Security 210-260: VPNs", 38: "CCNA Security 210-260: Firewalls", 39: "CCNA Security 210-260: The IPS and IDS", 40: "CCNA Security: NAT Review", 41: "CCNA Security: NTP", 42: "CCNA Security: AAA, TACACS, RADIUS, and Dot1x"}
            pattern2 = "(?:"+dict[section+1]+").*[^<]*"

        try:

            # Extract link from source page
            link = re.findall(pattern1, source_page)

            # Seperating tile and filename
            title = re.findall(pattern2, source_page)
            title = title[0].replace(":", "-")              # replacing ':' to '-' , because folder name does not support ':'
            title = title.split(' - ')                      # split tile and filename '-'
            title = [title[0], ' - '.join(title[1::])]       # extra title splited by previous command jioning other except 1st
            title0 = str(section + 1)+" - "+ title[0]       # title
            title1 = title[1]
            title1 = title1[:len(title1) - 1:]              # filename



            final_url = str("http://www.learningcrux.com" + link[0])    # jioing extracted url with domain
            final_url = final_url[:len(final_url) - 1:]                 # to remove last newline character  '/n'
            url = final_url

            response = requests.get(url, stream=True)
            total_content = len(response.content)
            try:
                directory = title0
                parent_dir = "D:\courses\CCNP\Routing and Switching\Chris Bryant"
                path = os.path.join(parent_dir, directory)
                os.makedirs(path)
            except OSError:
                pass

            file_name = os.path.join(path, title1)
            file_name = str(file_name + ".mp4")

            loaded_bytes = 0
            i = 0
            print()
            progressbar(0, total_content, length=50)
            with open(file_name, "wb") as f:
                for chunk in response.iter_content(chunk_size=1048576):  # 1 MB
                    loaded_bytes += len(chunk)
                    f.write(chunk)
                    time.sleep(0.1)
                    progressbar(i + 1048576, total_content, length=50)
                    i += 1048576
                print()
                print()
            print("downloaded : " + title1)
        except Exception as e:
            break


    if 1 == 1:
        x = tkinter.Tk()
        x.withdraw()
        x.attributes('-topmost',1)
        messagebox.showinfo("Message", "Download Completed...!")

    print("\n\n\n")
    x = str(input("Do you want to continue? (y/n) : "))
    if x == 'y':
        subprocess.call("cls", shell=True)
        main()
    else:
        pass

main()




#simple:)












