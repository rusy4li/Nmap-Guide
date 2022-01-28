#!/usr/bin/env python

########################################################

# Bu program rusy4li adlı coder tarafından kodlanmıştır!
# Github Hesabım: https://github.com/rusy4li
# Websitem: https://rusy4.xyz/
# İnstagram Hesabım: https://instagram.com/rusy4li

########################################################
try:
    import os
except ImportError:
    print(">>> 'os' modül hatası!")
try:
    import time
except ImportError:
    print(">>> 'time' modül hatası!")
try:
    import colorama
    from colorama import Fore, Style
    colorama.init()
except ImportError:
    print(">>> 'colorama' modül hatası!")
try:
    import datetime
except ImportError:
    print(">>> 'datetime' modül hatası!")

user = "rusy4li"
license = "rusy4li tarafından kodlanmıştır!"


# temizle
def clear():
    clear = os.system("cls")
    return clear


# Yardım veya Bilgi alma fonksiyonları
def help():
    # help
    print("""
    ##################################

    Nmap Tarama Türleri
    ------------------
    [TCP SYN Scan: -sS]
    [TCP Connect Scan: -sT]
    [TCP ACK Scan: -sA]
    [UDP Scan: -sU]
    [FIN Scan: -sF]
    [Ping Scan: -sP]
    [Window Scan: -sW]
    [IP Protocol Scan: -sO]
    [Idle Scan: -sI]
    [Xmas Scan: -sX]
    [Null Scan: -sN]

    Firewall/IDS Atlatma Yöntemleri
    -------------------------------
    [MTU: -MTU xxx]
    [IP Spoofing: -D 1xx.xxx.x.xx(fake ip)]
    [f: -f]

    Tarama Sonuçlarını Dosyaya Aktarma
    ----------------------------------
    [Txt: -oN output.txt]
    [Xml: -oX output.xml]

    ##################################""")
    time.sleep(1)
    print()
    input(">>> Devam etmek için herhangi bir tuşa bas...")
    clear()


def bilgi():
    i = 0
    while i == 0: 
        # bilgi
        print()
        print(">>> Hakkında bilgi almak istediğiniz konu nedir?")
        print("-----")
        print(">>> <(!)> Nmap ve Nmap Tarama Türleri:")
        print(">>> <(1)> Nmap hakkında bilgi")
        print(">>> <(2)> TCP Syn taraması")
        print(">>> <(3)> TCP Connect taraması")
        print(">>> <(4)> TCP ACK taraması")
        print(">>> <(5)> UDP taraması")
        print(">>> <(6)> FIN taraması")
        print(">>> <(7)> Ping taraması")
        print(">>> <(8)> Window taraması")
        print(">>> <(9)> IP Protocol taraması")
        print(">>> <(10)> Idle taraması")
        print(">>> <(11)> Xmas taraması")
        print(">>> <(12)> Null taraması")
        print("----------------------------------------------")
        print(">>> <(!)> Firewall/IDS Atlatma Yöntemleri")
        print(">>> <(13)> MTU İşlemi")
        print(">>> <(14)> IP Spoofing İşlemi")
        print(">>> <(15)> -f parametresini kullanma işlemi")
        print("----------------------------------------------")
        print(">>> <(!)> Nmap ile alakalı konular:")
        print(">>> <(16)> Tarama Sonuçlarını Dosyaya Aktarma")
        print("-----")
        sorgu = int(input("-> "))
        print()
        print(">>> Not Açılıyor:")
        if (sorgu == 1):
            i += 1
            with open("ScanNots/Nmap.txt", "r", encoding='utf-8') as dosya:
                print(dosya.read())
                time.sleep(1)
                print()
                input(">>> Devam etmek için herhangi bir tuşa bas...")
                clear()
        elif (sorgu == 2):
            i += 1
            with open("ScanNots/TCPSynScan.txt", "r", encoding='utf-8') as dosya:
                print(dosya.read())
                time.sleep(1)
                print()
                input(">>> Devam etmek için herhangi bir tuşa bas...")
                clear()
        elif (sorgu == 3):
            i += 1
            with open("ScanNots/TCPConnectScan.txt", "r", encoding='utf-8') as dosya:
                print(dosya.read())
                time.sleep(1)
                print()
                input(">>> Devam etmek için herhangi bir tuşa bas...")
                clear()
        elif (sorgu == 4):
            i += 1
            with open("ScanNots/TCPACKScan.txt", "r", encoding='utf-8') as dosya:
                print(dosya.read())
                time.sleep(1)
                print()
                input(">>> Devam etmek için herhangi bir tuşa bas...")
                clear()
        elif (sorgu == 5):
            i += 1
            with open("ScanNots/UDPScan.txt", "r", encoding='utf-8') as dosya:
                print(dosya.read())
                time.sleep(1)
                print()
                input(">>> Devam etmek için herhangi bir tuşa bas...")
                clear()
        elif (sorgu == 6):
            i += 1
            with open("ScanNots/FINScan.txt", "r", encoding='utf-8') as dosya:
                print(dosya.read())
                time.sleep(1)
                print()
                input(">>> Devam etmek için herhangi bir tuşa bas...")
                clear()
        elif (sorgu == 7):
            i += 1
            with open("ScanNots/PingScan.txt", "r", encoding='utf-8') as dosya:
                print(dosya.read())
                time.sleep(1)
                print()
                input(">>> Devam etmek için herhangi bir tuşa bas...")
                clear()
        elif (sorgu == 8):
            i += 1
            with open("ScanNots/WindowScan.txt", "r", encoding='utf-8') as dosya:
                print(dosya.read())
                time.sleep(1)
                print()
                input(">>> Devam etmek için herhangi bir tuşa bas...")
                clear()
        elif (sorgu == 9):
            i += 1
            with open("ScanNots/IPProtocolScan.txt", "r", encoding='utf-8') as dosya:
                print(dosya.read())
                time.sleep(1)
                print()
                input(">>> Devam etmek için herhangi bir tuşa bas...")
                clear()
        elif (sorgu == 10):
            i += 1
            with open("ScanNots/IdleScan.txt", "r", encoding='utf-8') as dosya:
                print(dosya.read())
                time.sleep(1)
                print()
                input(">>> Devam etmek için herhangi bir tuşa bas...")
                clear()
        elif (sorgu == 11):
            i += 1
            with open("ScanNots/XmasScan.txt", "r", encoding='utf-8') as dosya:
                print(dosya.read())
                time.sleep(1)
                print()
                input(">>> Devam etmek için herhangi bir tuşa bas...")
                clear()
        elif (sorgu == 12):
            i += 1
            with open("ScanNots/NullScan.txt", "r", encoding='utf-8') as dosya:
                print(dosya.read())
                time.sleep(1)
                print()
                input(">>> Devam etmek için herhangi bir tuşa bas...")
                clear()
        elif (sorgu == 13):
            i += 1
            with open("FirewallNots/MTU.txt", "r", encoding='utf-8') as dosya:
                print(dosya.read())
                time.sleep(1)
                print()
                input(">>> Devam etmek için herhangi bir tuşa bas...")
                clear()
        elif (sorgu == 14):
            i += 1
            with open("FirewallNots/IPSpoofing.txt", "r", encoding='utf-8') as dosya:
                print(dosya.read())
                time.sleep(1)
                print()
                input(">>> Devam etmek için herhangi bir tuşa bas...")
                clear()
        elif (sorgu == 15):
            i += 1
            with open("FirewallNots/-f.txt", "r", encoding='utf-8') as dosya:
                print(dosya.read())
                time.sleep(1)
                print()
                input(">>> Devam etmek için herhangi bir tuşa bas...")
                clear()
        elif (sorgu == 16):
            i += 1
            with open("Konular/Dosya.txt", "r", encoding='utf-8') as dosya:
                print(dosya.read())
                time.sleep(1)
                print()
                input(">>> Devam etmek için herhangi bir tuşa bas...")
                clear()
        else:
            os.system("cls")
            print("[!] Hata! 1-16 komutları girilebilir sadece")
            print()
            time.sleep(1.5)


# Firewall/IDS atlatma -güvenlik bölümü
def guvenlik():
    i = 0
    while i == 0:
        print()
        print("-----")
        print(">>> <(1)> Güvenlik olmasın!")
        print(">>> <(2)> -f parametresini kullan!")
        print("----")
        print(">>> Hangi Güvenlik seçeneğini istiyorsunuz")
        sorgu = input("-> ")
        if sorgu == "1":
            i += 1
            return ""
        elif sorgu == "2":
            i += 1
            return "-f"
        elif sorgu.lower() == "help" or sorgu.lower() == "help!" or sorgu.lower() == "yardım" or sorgu.lower() == "yardım!":
            help()
        elif sorgu.lower() == "bilgi" or sorgu.lower() == "bilgi!":
            bilgi()
        else:
            print("[!] Hata! 1-2 help!/bilgi! komutları girilebilir sadece")
            print()


# Port fonksiyonu
def port_tanilama():
    i = 0
    while i == 0:
        # Port Opsiyonları
        print("-----")
        print(">>> <(1)> Port Opsiyonu olmadan normal tarama yap")
        print(">>> <(2)> En sık kullanılan 100 Portu tara")
        print(">>> <(3)> Belirtecek olduğum Portu tara")
        print(">>> <(4)> Belirtecek olduğum Portları tara")
        print(">>> <(5)> Belirtecek olduğum aralıktaki Portları tara")
        print(">>> <(6)> 65.535 adet Portun hepsini tara")
        print("-----")
        print(">>> Hangi seçeneği istiyorsunuz")
        sorgu = input("-> ")
        if sorgu == "1":
            belirt = ""
            i += 1
            return belirt
        elif sorgu == "2":
            belirt = "-F"
            i += 1
            return belirt
        elif sorgu == "3":
            print(">>> Belirtecek olduğunuz Port nedir?")
            belirt1 = input("-> ")
            belirt = str("-p")
            i += 1
            return belirt+belirt1
        elif sorgu == "4":
            print(
                ">>> Belirtecek olduğunuz Portlar nedir? lütfen aralarına , koyun ve boşluk bırakmayın!")
            belirt1 = input("-> ")
            belirt = str("-p")
            i += 1
            return belirt+belirt1
        elif sorgu == "5":
            print(
                ">>> Belirtecek olduğunuz Port aralığı nedir? 1-100 gibi yazın lütfen!")
            belirt1 = input("-> ")
            belirt = str("-p")
            i += 1
            return belirt+belirt1
        elif sorgu == "6":
            belirt = "-p-"
            i += 1
            return belirt
        elif sorgu.lower() == "help" or sorgu.lower() == "help!" or sorgu.lower() == "yardım" or sorgu.lower() == "yardım!":
            help()
        elif sorgu.lower() == "bilgi" or sorgu.lower() == "bilgi!":
            bilgi()
        else:
            print("[!] Hata! 1-5 help!/bilgi! komutları girilebilir sadece")
            print()


i = 0
if user != "rusy4li" or license != "rusy4li tarafından kodlanmıştır!":
    i = 1
    while i == 1:
        print("""########################################################

# Bu program rusy4li adlı coder tarafından kodlanmıştır!
# Github Hesabım: https://github.com/rusy4li
# Websitem: https://rusy4.xyz/
# İnstagram Hesabım: https://instagram.com/rusy4li

########################################################""")
        time.sleep(1.5)
        os.system("cls")

datetime_modulü = datetime.datetime.now()
vakitT = datetime_modulü.strftime("%Y-%M-%D")
vakits = datetime_modulü.strftime("%I:%M:%S")
vakit = datetime_modulü.strftime(Fore.BLUE + "%I:%M:%S")
nm = Style.RESET_ALL
os.system("cls")
# http://patorjk.com/software/taag/#p=display&f=Star%20Wars&t=Nmap%20Guide%0A
print(Fore.GREEN + """
.__   __. .___  ___.      ___      .______        _______  __    __   __   _______   _______
|  \ |  | |   \/   |     /   \     |   _  \      /  _____||  |  |  | |  | |       \ |   ____|
|   \|  | |  \  /  |    /  ^  \    |  |_)  |    |  |  __  |  |  |  | |  | |  .--.  ||  |__
|  . `  | |  |\/|  |   /  /_\  \   |   ___/     |  | |_ | |  |  |  | |  | |  |  |  ||   __|
|  |\   | |  |  |  |  /  _____  \  |  |         |  |__| | |  `--'  | |  | |  '--'  ||  |____
|__| \__| |__|  |__| /__/     \__\ | _|          \______|  \______/  |__| |_______/ |_______|


""")
print(Style.RESET_ALL)
print("[!] This program is not made for malicious use! We take no responsibility if it is misused.")
print()
print(Style.RESET_ALL +
      "[*] !help/!bilgi starting @ {} /{}/".format(vakits, vakitT))
print()
print("{}>>> Hangi İşlemi yapmak istiyorsunuz?".format(nm))
while True:
    print(">>> <(1)> Alan adı tarama")
    print(">>> <(2)> IP adresi/Port tarama")
    neistiyon = input("-> ")
    if neistiyon == "1":
        i = 0
        while i == 0:
            print(
                ">>> Taramak istediğiniz Alan adı'nı giriniz lütfen")

            soru = input("-> ")
            print()
            if soru.lower() == "help" or soru.lower() == "help!" or soru.lower() == "yardım" or soru.lower() == "yardım!":
                help()
            elif soru.lower() == "bilgi" or soru.lower() == "bilgi!":
                bilgi()
            else:
                i += 1
                print("Başlıyor...")
                time.sleep(1)
                os.system("nmap -sV {}".format(soru))
        time.sleep(1)
        print()
        input(">>> Devam etmek için herhangi bir tuşa bas...")
    #############################################
    elif neistiyon == "2":
        # Tarama Yöntemi seçme ekranı!
        print(
            ">>> Hangi tarama yöntemini kullanacaksınız?")
        print("--------")
        print(">>> <(1)> nmap ile TCP Syn taraması yapma")
        print(">>> <(2)> nmap ile TCP Connect taraması yapma")
        print(">>> <(3)> nmap ile TCP ACK taraması yapma")
        print(">>> <(4)> nmap ile UDP taraması yapma")
        print(">>> <(5)> nmap ile FIN taraması yapma")
        print(">>> <(6)> nmap ile Ping taraması yapma")
        print(">>> <(7)> nmap ile Window taraması yapma")
        print(">>> <(8)> nmap ile IP Protocol taraması yapma")
        print(">>> <(9)> nmap ile Idle taraması yapma")
        print(">>> <(10)> nmap ile Xmas taraması yapma")
        print(">>> <(11)> nmap ile Null taraması yapma")
        print(">>> <(12)> nmap ile Dosya çıktısı alma")
        print("--------")
        sorgu = input("->> ")
        # Tarama Yöntemini seçti
        if sorgu == "1":
            print(
                ">>> TCP Syn taraması yapmak istediğiniz ip adresini girin lütfen")
            soru_hedef = input("-> ")

            # Port Opsiyonları bölümü:
            print()
            soru_port_tanilama = port_tanilama()
            # Port Opsiyonları bölümü bitti

            # Firewall/IDS atlatma -güvenlik bölümü
            guvenlik = guvenlik()
            if guvenlik == "":

                # tarama başlıyor!
                print()
                print("Başlıyor...")
                time.sleep(1)
                if soru_port_tanilama == "":
                    os.system("nmap -sS {}".format(soru_hedef))
                else:
                    os.system(
                        "nmap -sS {} {}".format(soru_port_tanilama, soru_hedef))
            else:

                # tarama başlıyor!
                print()
                print("Başlıyor...")
                time.sleep(1)
                if soru_port_tanilama == "":
                    os.system("nmap -sS {} {}".format(guvenlik, soru_hedef))
                else:
                    os.system(
                        "nmap -sS {} {} {}".format(guvenlik, soru_port_tanilama, soru_hedef))
            time.sleep(1)
            print()
            input(">>> Devam etmek için herhangi bir tuşa bas...")
        ############################################################

        elif sorgu == "2":
            print(
                ">>> TCP Connect taraması yapmak istediğiniz ip adresini girin lütfen")
            soru_hedef = input("-> ")

            # Port Opsiyonları bölümü:
            print()
            soru_port_tanilama = port_tanilama()
            # Port Opsiyonları bölümü bitti

            # Firewall/IDS atlatma -güvenlik bölümü
            guvenlik = guvenlik()
            if guvenlik == "":

                # tarama başlıyor!
                print()
                print("Başlıyor...")
                time.sleep(1)
                if soru_port_tanilama == "":
                    os.system("nmap -sT {}".format(soru_hedef))
                else:
                    os.system(
                        "nmap -sT {} {}".format(soru_port_tanilama, soru_hedef))
            else:
                # tarama başlıyor!
                print()
                print("Başlıyor...")
                time.sleep(1)
                if soru_port_tanilama == "":
                    os.system("nmap -sT {} {}".format(guvenlik, soru_hedef))
                else:
                    os.system(
                        "nmap -sT {} {} {}".format(guvenlik, soru_port_tanilama, soru_hedef))
            time.sleep(1)
            print()
            input(">>> Devam etmek için herhangi bir tuşa bas...")
            
        ############################################################

        elif sorgu == "3":
            print(
                ">>> TCP ACK taraması yapmak istediğiniz ip adresini girin lütfen")
            soru_hedef = input("-> ")

            # Port Opsiyonları bölümü:
            print()
            soru_port_tanilama = port_tanilama()
            # Port Opsiyonları bölümü bitti

            # Firewall/IDS atlatma -güvenlik bölümü
            guvenlik = guvenlik()
            if guvenlik == "":

                # tarama başlıyor!
                print()
                print("Başlıyor...")
                time.sleep(1)
                if soru_port_tanilama == "":
                    os.system("nmap -sA {}".format(soru_hedef))
                else:
                    os.system(
                        "nmap -sA {} {}".format(soru_port_tanilama, soru_hedef))
            else:
                # tarama başlıyor!
                print()
                print("Başlıyor...")
                time.sleep(1)
                if soru_port_tanilama == "":
                    os.system("nmap -sA {} {}".format(guvenlik, soru_hedef))
                else:
                    os.system(
                        "nmap -sA {} {} {}".format(guvenlik, soru_port_tanilama, soru_hedef))
            time.sleep(1)
            print()
            input(">>> Devam etmek için herhangi bir tuşa bas...")
            
        ############################################################

        elif sorgu == "4":
            print(
                ">>> UDP taraması yapmak istediğiniz ip adresini girin lütfen")
            soru_hedef = input("-> ")

            # Port Opsiyonları bölümü:
            print()
            soru_port_tanilama = port_tanilama()
            # Port Opsiyonları bölümü bitti

            # Firewall/IDS atlatma -güvenlik bölümü
            guvenlik = guvenlik()
            if guvenlik == "":

                # tarama başlıyor!
                print()
                print("Başlıyor...")
                time.sleep(1)
                if soru_port_tanilama == "":
                    os.system("nmap -sU {}".format(soru_hedef))
                else:
                    os.system(
                        "nmap -sU {} {}".format(soru_port_tanilama, soru_hedef))
            else:
                # tarama başlıyor!
                print()
                print("Başlıyor...")
                time.sleep(1)
                if soru_port_tanilama == "":
                    os.system("nmap -sU {} {}".format(guvenlik, soru_hedef))
                else:
                    os.system(
                        "nmap -sU {} {} {}".format(guvenlik, soru_port_tanilama, soru_hedef))
            time.sleep(1)
            print()
            input(">>> Devam etmek için herhangi bir tuşa bas...")
            
        ############################################################

        elif sorgu == "5":
            print(
                ">>> FIN taraması yapmak istediğiniz ip adresini girin lütfen")
            soru_hedef = input("-> ")

            # Port Opsiyonları bölümü:
            print()
            soru_port_tanilama = port_tanilama()
            # Port Opsiyonları bölümü bitti

            # Firewall/IDS atlatma -güvenlik bölümü
            guvenlik = guvenlik()
            if guvenlik == "":

                # tarama başlıyor!
                print()
                print("Başlıyor...")
                time.sleep(1)
                if soru_port_tanilama == "":
                    os.system("nmap -sF {}".format(soru_hedef))
                else:
                    os.system(
                        "nmap -sF {} {}".format(soru_port_tanilama, soru_hedef))
            else:
                # tarama başlıyor!
                print()
                print("Başlıyor...")
                time.sleep(1)
                if soru_port_tanilama == "":
                    os.system("nmap -sF {} {}".format(guvenlik, soru_hedef))
                else:
                    os.system(
                        "nmap -sF {} {} {}".format(guvenlik, soru_port_tanilama, soru_hedef))
            time.sleep(1)
            print()
            input(">>> Devam etmek için herhangi bir tuşa bas...")
            
        ############################################################

        elif sorgu == "6":
            print(
                ">>> Ping taraması yapmak istediğiniz ip adresini girin lütfen")
            soru_hedef = input("-> ")

            # Port Opsiyonları bölümü:
            print()
            soru_port_tanilama = port_tanilama()
            # Port Opsiyonları bölümü bitti

            # Firewall/IDS atlatma -güvenlik bölümü
            guvenlik = guvenlik()
            if guvenlik == "":

                # tarama başlıyor!
                print()
                print("Başlıyor...")
                time.sleep(1)
                if soru_port_tanilama == "":
                    os.system("nmap -sP {}".format(soru_hedef))
                else:
                    os.system(
                        "nmap -sP {} {}".format(soru_port_tanilama, soru_hedef))
            else:
                # tarama başlıyor!
                print()
                print("Başlıyor...")
                time.sleep(1)
                if soru_port_tanilama == "":
                    os.system("nmap -sP {} {}".format(guvenlik, soru_hedef))
                else:
                    os.system(
                        "nmap -sP {} {} {}".format(guvenlik, soru_port_tanilama, soru_hedef))
            time.sleep(1)
            print()
            input(">>> Devam etmek için herhangi bir tuşa bas...")
            
        ############################################################

        elif sorgu == "7":
            print(
                ">>> Window taraması yapmak istediğiniz ip adresini girin lütfen")
            soru_hedef = input("-> ")

            # Port Opsiyonları bölümü:
            print()
            soru_port_tanilama = port_tanilama()
            # Port Opsiyonları bölümü bitti

            # Firewall/IDS atlatma -güvenlik bölümü
            guvenlik = guvenlik()
            if guvenlik == "":

                # tarama başlıyor!
                print()
                print("Başlıyor...")
                time.sleep(1)
                if soru_port_tanilama == "":
                    os.system("nmap -sW {}".format(soru_hedef))
                else:
                    os.system(
                        "nmap -sW {} {}".format(soru_port_tanilama, soru_hedef))
            else:
                # tarama başlıyor!
                print()
                print("Başlıyor...")
                time.sleep(1)
                if soru_port_tanilama == "":
                    os.system("nmap -sW {} {}".format(guvenlik, soru_hedef))
                else:
                    os.system(
                        "nmap -sW {} {} {}".format(guvenlik, soru_port_tanilama, soru_hedef))
            time.sleep(1)
            print()
            input(">>> Devam etmek için herhangi bir tuşa bas...")
            
        ############################################################

        elif sorgu == "8":
            print(
                ">>> IP Protocol taraması yapmak istediğiniz ip adresini girin lütfen")
            soru_hedef = input("-> ")

            # Port Opsiyonları bölümü:
            print()
            soru_port_tanilama = port_tanilama()
            # Port Opsiyonları bölümü bitti

            # Firewall/IDS atlatma -güvenlik bölümü
            guvenlik = guvenlik()
            if guvenlik == "":

                # tarama başlıyor!
                print()
                print("Başlıyor...")
                time.sleep(1)
                if soru_port_tanilama == "":
                    os.system("nmap -sO {}".format(soru_hedef))
                else:
                    os.system(
                        "nmap -sO {} {}".format(soru_port_tanilama, soru_hedef))
            else:
                # tarama başlıyor!
                print()
                print("Başlıyor...")
                time.sleep(1)
                if soru_port_tanilama == "":
                    os.system("nmap -sO {} {}".format(guvenlik, soru_hedef))
                else:
                    os.system(
                        "nmap -sO {} {} {}".format(guvenlik, soru_port_tanilama, soru_hedef))
            time.sleep(1)
            print()
            input(">>> Devam etmek için herhangi bir tuşa bas...")
            
        ############################################################

        elif sorgu == "9":
            print(
                ">>> Idle taraması yapmak istediğiniz ip adresini girin lütfen")
            soru_hedef = input("-> ")

            # Port Opsiyonları bölümü:
            print()
            soru_port_tanilama = port_tanilama()
            # Port Opsiyonları bölümü bitti

            # Firewall/IDS atlatma -güvenlik bölümü
            guvenlik = guvenlik()
            if guvenlik == "":

                # tarama başlıyor!
                print()
                print("Başlıyor...")
                time.sleep(1)
                if soru_port_tanilama == "":
                    os.system("nmap -sI {}".format(soru_hedef))
                else:
                    os.system(
                        "nmap -sI {} {}".format(soru_port_tanilama, soru_hedef))
            else:
                # tarama başlıyor!
                print()
                print("Başlıyor...")
                time.sleep(1)
                if soru_port_tanilama == "":
                    os.system("nmap -sI {} {}".format(guvenlik, soru_hedef))
                else:
                    os.system(
                        "nmap -sI {} {} {}".format(guvenlik, soru_port_tanilama, soru_hedef))
            time.sleep(1)
            print()
            input(">>> Devam etmek için herhangi bir tuşa bas...")
            
        ############################################################

        elif sorgu == "10":
            print(
                ">>> Xmas taraması yapmak istediğiniz ip adresini girin lütfen")
            soru_hedef = input("-> ")

            # Port Opsiyonları bölümü:
            print()
            soru_port_tanilama = port_tanilama()
            # Port Opsiyonları bölümü bitti

            # Firewall/IDS atlatma -güvenlik bölümü
            guvenlik = guvenlik()
            if guvenlik == "":

                # tarama başlıyor!
                print()
                print("Başlıyor...")
                time.sleep(1)
                if soru_port_tanilama == "":
                    os.system("nmap -sX {}".format(soru_hedef))
                else:
                    os.system(
                        "nmap -sX {} {}".format(soru_port_tanilama, soru_hedef))
            else:
                # tarama başlıyor!
                print()
                print("Başlıyor...")
                time.sleep(1)
                if soru_port_tanilama == "":
                    os.system("nmap -sX {} {}".format(guvenlik, soru_hedef))
                else:
                    os.system(
                        "nmap -sX {} {} {}".format(guvenlik, soru_port_tanilama, soru_hedef))
            time.sleep(1)
            print()
            input(">>> Devam etmek için herhangi bir tuşa bas...")
            
        ############################################################

        elif sorgu == "11":
            print(
                ">>> Null taraması yapmak istediğiniz ip adresini girin lütfen")
            soru_hedef = input("-> ")

            # Port Opsiyonları bölümü:
            print()
            soru_port_tanilama = port_tanilama()
            # Port Opsiyonları bölümü bitti

            # Firewall/IDS atlatma -güvenlik bölümü
            guvenlik = guvenlik()
            if guvenlik == "":

                # tarama başlıyor!
                print()
                print("Başlıyor...")
                time.sleep(1)
                if soru_port_tanilama == "":
                    os.system("nmap -sN {}".format(soru_hedef))
                else:
                    os.system(
                        "nmap -sN {} {}".format(soru_port_tanilama, soru_hedef))
            else:
                # tarama başlıyor!
                print()
                print("Başlıyor...")
                time.sleep(1)
                if soru_port_tanilama == "":
                    os.system("nmap -sN {} {}".format(guvenlik, soru_hedef))
                else:
                    os.system(
                        "nmap -sN {} {} {}".format(guvenlik, soru_port_tanilama, soru_hedef))
            time.sleep(1)
            print()
            input(">>> Devam etmek için herhangi bir tuşa bas...")
            
        ############################################################

        elif sorgu == "12":
            print(
                ">>> TCP Syn taraması yapmak istediğiniz ip adresini girin lütfen")
            soru_hedef = input("-> ")
            print(">>> Dosya ismi giriniz lütfen")
            soru_dosya = input("-> ")
            print(">>> Dosya Çıktısı alınıyor...")
            time.sleep(1)
            os.system("nmap -sS -oN {} {}".format(soru_hedef, soru_dosya))
            time.sleep(1)
            print()
            input(">>> Devam etmek için herhangi bir tuşa bas...")
            
        ############################################################

        elif sorgu.lower() == "help" or sorgu.lower() == "help!" or sorgu.lower() == "yardım" or sorgu.lower() == "yardım!":
            help()
        elif sorgu.lower() == "bilgi" or sorgu.lower() == "bilgi!":
            bilgi()
        else:
            print("[!] Hata! 1-11 help!/bilgi! komutları girilebilir sadece")
            print()
    elif neistiyon.lower() == "help" or neistiyon.lower() == "help!" or neistiyon.lower() == "yardım" or neistiyon.lower() == "yardım!":
        help()
    elif neistiyon.lower() == "bilgi" or neistiyon.lower() == "bilgi!":
        bilgi()
    else:
        print("[!] Hata! 1-3 help!/bilgi! komutları girilebilir sadece")
        print()
    clear()
    # http://patorjk.com/software/taag/#p=display&f=Star%20Wars&t=Nmap%20Guide%0A
    print(Fore.GREEN + """
.__   __. .___  ___.      ___      .______        _______  __    __   __   _______   _______ 
|  \ |  | |   \/   |     /   \     |   _  \      /  _____||  |  |  | |  | |       \ |   ____|
|   \|  | |  \  /  |    /  ^  \    |  |_)  |    |  |  __  |  |  |  | |  | |  .--.  ||  |__   
|  . `  | |  |\/|  |   /  /_\  \   |   ___/     |  | |_ | |  |  |  | |  | |  |  |  ||   __|  
|  |\   | |  |  |  |  /  _____  \  |  |         |  |__| | |  `--'  | |  | |  '--'  ||  |____ 
|__| \__| |__|  |__| /__/     \__\ | _|          \______|  \______/  |__| |_______/ |_______|
                                                                                             
                                                                                             """)
    print(Style.RESET_ALL)
