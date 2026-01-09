import time
import os

def ekran_temizle():
    # Codespaces terminali için en temiz yöntem
    print("\033[H\033[J", end="")

def virgulu_kaydir():
    while True:
        ekran_temizle()
        print("="*40)
        print("   ONDALIK ÇARPMA SİMÜLATÖRÜ")
        print("="*40)
        
        giris = input("\nBir ondalık sayı gir (Örn: 3.45): ").replace(',', '.')
        if '.' not in giris: giris += '.'
        sayi_listesi = list(giris)
        
        try:
            carpan = int(input("Çarpanı seç (10, 100, 1000): "))
            if carpan not in [10, 100, 1000]: raise ValueError
        except:
            print("Lütfen sadece 10, 100 veya 1000 girin!")
            time.sleep(2); continue

        adim = len(str(carpan)) - 1
        
        for i in range(adim):
            ekran_temizle()
            v_idx = sayi_listesi.index('.')
            if v_idx == len(sayi_listesi) - 1:
                sayi_listesi.pop(v_idx)
                sayi_listesi.append('0')
                sayi_listesi.append('.')
            else:
                sayi_listesi[v_idx], sayi_listesi[v_idx+1] = sayi_listesi[v_idx+1], sayi_listesi[v_idx]
            
            print(f"\nAdım {i+1}: {''.join(sayi_listesi).rstrip('.')}")
            time.sleep(1)

        print("\n" + "*"*20)
        print(f"SONUÇ: {''.join(sayi_listesi).rstrip('.')}")
        print("*"*20)
        
        if input("\nDevam mı? (e/h): ").lower() != 'e': break

if __name__ == "__main__":
    virgulu_kaydir()
