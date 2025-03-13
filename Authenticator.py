#Kütüphane
import random
import time
from PIL import Image
from pyzbar.pyzbar import decode
import threading

#Random authcode fonksiyonu
authcode = None
def codeloop():
    global authcode
    while True:
        authcode = random.randint(100000,999999)
        print(authcode)
        time.sleep(15)

#QR kod çalıştırma
QRPath = input("QR Kod Pathinizi Giriniz.")
QR = Image.open(QRPath)
QROku = decode(QR)
for obj in QROku:
    QRIcerigi = obj.data.decode("utf-8")
if QRIcerigi == "Authcode Basarili":
    print("QR Kod Geçerli, Auth Code üretiliyor...")
    while True:
        threading.Thread(target=codeloop, daemon=True).start()
        authconfirm = input("Doğrulama Kodunuzu Giriniz: ")
        if int(authconfirm) == authcode:
            print("Doğrulama Başarılı")
            break
        else:
            print("Doğrulama Kodu Yanlış")
            authconfirm = input("Doğrulama Kodunuzu Giriniz: ")


else:
    print("QR Kod Geçersiz.")
    exit()






