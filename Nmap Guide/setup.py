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

# Setup Notları:
# Bu programın çalışması için bilgisayarınızda python3-veya daha üst bir sürümün kurulu olması gerekmektedir!
# Bu programda nmapi kullanmak için bilgisayarınızda nmapin kurulu olması gerekmektedir!
# Bu program Windows Sistemler için kodlanmıştır Linux sistemler için En yakın zamanda yeni Nmap Guide sürümü gelecektir.
# FirewallNots/Konular/ScanNots isimli klasörlerde nmap hakkında birçok özellik kolay bir dil ile anlatılmıştır.
# Lütfen programın sabit çalışması için hiçbir klasörü silmeyiniz!
# Kod satırından tasaruf etmek için birçok şeyi dosyalara yazıp programda o dosyalar ile çalışılmasını sağladım.
################

# Nmap Kurulum:
# Nmap İndirme Sitesi: https://nmap.org/download.html
print("""########################################################

# Bu program rusy4li adlı coder tarafından kodlanmıştır!
# Github Hesabım: https://github.com/rusy4li
# Websitem: https://rusy4.xyz/
# İnstagram Hesabım: https://instagram.com/rusy4li

########################################################""")
time.sleep(1.5)
os.system("cls")
os.system("python -V")
print()
print(">>> Python yanında yazan [python 3.xx.x] sürümüdür. ")
