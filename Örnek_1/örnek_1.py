"""
Kullanıcı tarafından girilen iki sayının toplamını veren program
"""

# Hata yönetimi ekleyerek kullanıcıdan giriş al
try:
    birinci_sayi = float(input("Birinci sayıyı giriniz: "))
    ikinci_sayi = float(input("İkinci sayıyı giriniz: "))

    toplam = birinci_sayi + ikinci_sayi
    print("İki sayının toplamı =", toplam)

except ValueError:
    print("Lütfen geçerli bir sayı giriniz.")
