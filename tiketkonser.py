from tabulate import tabulate
import os
import random
import string
import sys
import time
from datetime import datetime
from colorama import Fore

os.system('cls')

selected_tickets = {}

def loading():
    chars = "/—\|"
    for i in range(50):
        sys.stdout.write(f"\r{Fore.YELLOW}Memuat... {chars[i % len(chars)]}")
        sys.stdout.flush()
        time.sleep(0.1)

    print(f"{Fore.GREEN}\nSelesai!{Fore.RESET}")

def generate_ticket_code():
    letters = string.ascii_uppercase
    numbers = ''.join(random.choices(string.digits, k=4))
    ticket_code = ''.join(random.choices(letters, k=3)) + numbers
    return ticket_code

def invoice():
    letters = string.ascii_uppercase
    numbers = ''.join(random.choices(string.digits, k=6))
    ticket_code = ''.join(random.choices(letters, k=5)) + numbers
    return ticket_code

def show_running_time():
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"{Fore.GREEN}{current_time}", end="\r")
        time.sleep(1)
        
# home
def display_ticket():
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")

    space = 36  # Jumlah spasi sebelum waktu dan tanggal

    print(f"{Fore.BLUE}===================================={Fore.RESET}")
    print(f"{Fore.LIGHTGREEN_EX}{' ' * ((space - len(current_time) - len(current_date)) // 2)}{current_time} - {current_date}{Fore.RESET}")
    print(f"{Fore.BLUE}===================================={Fore.RESET}")
    print(f"{Fore.LIGHTWHITE_EX}PILIH TIKET YANG INGIN DIBELI")
    print("1) HOTPLAY")
    print(f"2) MEMORIES{Fore.RESET}")
    print(f"{Fore.BLUE}-{Fore.RESET}" * 36)
    print(f"{Fore.LIGHTYELLOW_EX}0) Keluar{Fore.RESET}")
    print(f"{Fore.BLUE}===================================={Fore.RESET}")

#pilihan tiket
def select_ticket(selected_event, pilih_tiket):
    if pilih_tiket in {"1", "ZEUS", "ULTIMATE"}:
        ktg = "ULTIMATE" if selected_event == "Hotplay" else "ZEUS"
        harga = 2000000 if selected_event == "Hotplay" else 800000
    elif pilih_tiket in {"2", "POSEIDON", "FESTIVAL"}:
        ktg = "FESTIVAL" if selected_event == "Hotplay" else "POSEIDON"
        harga = 1000000 if selected_event == "Hotplay" else 500000
    elif pilih_tiket in {"3", "HADES", "TRIBUNE"}:
        ktg = "TRIBUNE" if selected_event == "Hotplay" else "HADES"
        harga = 700000 if selected_event == "Hotplay" else 300000
    else:
        print("Pilihan tidak valid, silakan pilih kategori tiket yang tersedia (ULTIMATE/FESTIVAL/TRIBUNE).")
        return None, None

    return ktg, harga

#memories
def tiket_memories(selected_event):
    print(f"{Fore.BLUE}===================================={Fore.RESET}")
    print("{:^36}".format("MEMORIES WORLD TOUR"))
    print(f"{Fore.BLUE}===================================={Fore.RESET}")
    print("{:^36}".format("Event Schedule"))
    print("{:^36}".format("Senin, 30 Februari 2024"))
    print("{:^36}".format("JAKARTA INTERNATIONAL STADIUM (JIS)"))
    print(f"{Fore.BLUE}====================================\n{Fore.RESET}")

    # Table tiket
    memories_tiket = [
        ["1)ZEUS", 50, "Rp.800.000"],
        ["2)POSEIDON", 100, "Rp.500.000"],
        ["3)HADES", 250, "Rp.300.000"],
    ]
    print(tabulate(memories_tiket, headers=["Kategori", "Tersedia", "Harga"], tablefmt="pretty"))
    
    print(f"{Fore.BLUE}\n===================================={Fore.RESET}")
    print("Note : Pembelian hanya bisa dilakukan 1 kali dan max 5 tiket untuk menghindari calo tiket!")
    print("Note : 1)ZEUS, 2)POSEIDON, 3)HADES")
    
    while True:
        tiket = input("Pilih tiket (1/2/3) : ")
        if tiket in {"1", "ZEUS", "2", "POSEIDON", "3", "HADES"}:
            return select_ticket(selected_event, tiket)
        else:
            print("Pilihan tidak valid, silakan pilih kategori tiket yang tersedia.")
            continue

#hotplay
def tiket_hotplay(selected_event):
    print(f"{Fore.BLUE}===================================={Fore.RESET}")
    print("{:^36}".format("HOTPLAY WORLD TOUR"))
    print(f"{Fore.BLUE}===================================={Fore.RESET}")
    print("{:^36}".format("Event Schedule"))
    print("{:^36}".format("Minggu, 30 April 2024"))
    print("{:^36}".format("Gelora Bung Karno Stadium Jakarta"))
    print(f"{Fore.BLUE}====================================\n{Fore.RESET}")

    hotplay_tickets = [
        ["1)ULTIMATE", 50, "Rp.2.000.000"],
        ["2)FESTIVAL", 100, "Rp.1.000.000"],
        ["3)TRIBUNE", 300, "Rp.700.000"],
    ]

    print(tabulate(hotplay_tickets, headers=["Kategori", "Tersedia", "Harga"], tablefmt="pretty"))

    print(f"{Fore.BLUE}\n===================================={Fore.RESET}")
    print("Note : Pembelian hanya bisa dilakukan 1 kali dan max 5 tiket untuk menghindari calo tiket!")
    print("Note : 1)ULTIMATE, 2)FESTIVAL, 3)TRIBUNE")
    
    while True:
        tiket = input("Pilih tiket (1/2/3) : ")
        if tiket in {"1", "ULTIMATE", "2", "FESTIVAL", "3", "TRIBUNE"}:
            return select_ticket(selected_event, tiket)
        else:
            print("Pilihan tidak valid, silakan pilih kategori tiket yang tersedia.")
            continue
        
kode_tiket = generate_ticket_code()
kode_tiket2 = invoice()

def banyak_tiket_dibeli():
    while True:
        try:
            quantity = int(input("Berapa banyak : "))
            if quantity < -1:
                print("Masukkan jumlah tiket yang valid.")
            else:
                return quantity
        except ValueError:
                print("Harap masukkan angka!")

def payment_proses():
    print("Sudah melakukan pembayaran? [Y/N/0]")
    print("[Y] Yes")
    print("[N] No")
    print("[0] Keluar")

def BCA():
    print("Detail Pembayaran:")
    print(f"{Fore.BLUE}========================================\n{Fore.RESET}")
    print("Metode Pembayaran: BCA")
    print("Nomor Rekening    : 2240395910")
    print(f"Total Harga Tiket (belum termasuk ppn) : Rp.{total}")
    print(f"PPN 10% : Rp. {ppn}")
    print(f"Total Pembayaran  : Rp. {alltotal}")
    print("Silahkan lakukan pembayaran ke nomor rekening di atas.")
    print("\nJika Sudah Melakukan Pembayaran, Silahkan Kirimkan Bukti Pembayarannya Ke Email Di Bawah Ini:")
    print("Email : admin-invoice@tiketbuy.com")
    print(f"{Fore.BLUE}========================================{Fore.RESET}")

    payment_proses()
    while True:
        bayar = (input("[Y/N/0] : ")).upper()
        os.system('cls')
        loading()
        if bayar == "Y":
            now = datetime.now()
            date_time = now.strftime("%Y-%m-%d %H:%M:%S")
            print(f"\nTanggal dan Waktu : {date_time}")

            eticket = [
                ["",nama],
                [kode_tiket,email,selected_tickets[ktg],f'{Fore.GREEN}Rp.{alltotal}{Fore.RESET}',kode_tiket2],
                ["",nope]
            ]
            print(tabulate(eticket, headers=["E-TICKET","FORM DATA", "BANYAK","TOTAL HARGA","INVOICE"], tablefmt="pretty"))
            exit()
            break
        elif bayar == "N":
            print("Belum melakukan pembayaran.")
            print("Kembali ke menu pembayaran")
            return BCA()
        elif bayar == "0":
            print(f"{Fore.RED}Terima kasih! Anda telah keluar!")    
            sys.exit()
        else:
            print("Mohon masukkan Y atau N untuk menanggapi pertanyaan.")
            payment_proses()
            

def BRI():
    print("Detail Pembayaran:")
    print(f"{Fore.BLUE}========================================\n{Fore.RESET}")
    print("Metode Pembayaran: BRI")
    print("Nomor Rekening    : 1982732101")
    print(f"Total Harga Tiket (belum termasuk ppn) : Rp.{total}")
    print(f"PPN 10% : Rp. {ppn}")
    print(f"Total Pembayaran  : Rp. {alltotal}")
    print("Silahkan lakukan pembayaran ke nomor rekening di atas.")
    print("\nJika Sudah Melakukan Pembayaran, Silahkan Kirimkan Bukti Pembayarannya Ke Email Di Bawah Ini:")
    print("Email : admin-invoice@tiketbuy.com")
    print(f"{Fore.BLUE}========================================{Fore.RESET}")

    payment_proses()
    while True:
        bayar = (input("[Y/N/0] : ")).upper().strip()
        os.system('cls')
        loading()
        if bayar == "Y":
            now = datetime.now()
            date_time = now.strftime("%Y-%m-%d %H:%M:%S")
            print(f"\nTanggal dan Waktu : {date_time}")

            eticket = [
                ["",nama],
                [kode_tiket,email,selected_tickets[ktg],f'{Fore.GREEN}Rp.{alltotal}{Fore.RESET}',kode_tiket2],
                ["",nope]
            ]
            print(tabulate(eticket, headers=["E-TICKET","FORM DATA", "BANYAK","TOTAL HARGA","INVOICE"], tablefmt="pretty"))
            exit()
            break
        elif bayar == "N":
            print("Belum melakukan pembayaran.")
            print("Kembali ke menu pembayaran")
            return BRI()
        elif bayar == "0":
            print(f"{Fore.RED}Terima kasih! Anda telah keluar!")    
            sys.exit()
        else:
            print("Mohon masukkan Y atau N untuk menanggapi pertanyaan.")
            payment_proses()

def MANDIRI():
    print("Detail Pembayaran:")
    print(f"{Fore.BLUE}========================================\n{Fore.RESET}")
    print("Metode Pembayaran: MANDIRI")
    print("Nomor Rekening    : 4563829202")
    print(f"Total Harga Tiket (belum termasuk ppn) : Rp.{total}")
    print(f"PPN 10% : Rp. {ppn}")
    print(f"Total Pembayaran  : Rp. {alltotal}")
    print("Silahkan lakukan pembayaran ke nomor rekening di atas.")
    print("\nJika Sudah Melakukan Pembayaran, Silahkan Kirimkan Bukti Pembayarannya Ke Email Di Bawah Ini:")
    print("Email : admin@tiketbuy.com\n")
    print(f"{Fore.BLUE}========================================{Fore.RESET}")
    
    payment_proses()
    while True:
        bayar = (input("[Y/N/0] : ")).upper().strip()
        os.system('cls')
        loading()
        if bayar == "Y":
            now = datetime.now()
            date_time = now.strftime("%Y-%m-%d %H:%M:%S")
            print(f"\nTanggal dan Waktu : {date_time}")

            eticket = [
                ["",nama],
                [kode_tiket,email,selected_tickets[ktg],f'{Fore.GREEN}Rp.{alltotal}{Fore.RESET}',kode_tiket2],
                ["",nope]
            ]
            print(tabulate(eticket, headers=["E-TICKET","FORM DATA", "BANYAK","TOTAL HARGA","INVOICE"], tablefmt="pretty"))
            exit()
            break
            
        elif bayar == "N":
            print("Belum melakukan pembayaran.")
            print("Kembali ke menu pembayaran")
            return MANDIRI()
        elif bayar == 0:
            print(f"{Fore.RED}Terima kasih! Anda telah keluar!")    
            sys.exit()
        else:
            print("Mohon masukkan Y atau N untuk menanggapi pertanyaan.")
            payment_proses()

#input home
while True:
    display_ticket()

    selected_option = input("Pilih : ".upper())
    os.system('cls')

    if selected_option == "1":
        selected_event = "Hotplay"
        ktg, harga = tiket_hotplay(selected_event)
    elif selected_option == "2":
        selected_event = "Memories"
        ktg, harga = tiket_memories(selected_event)
    elif selected_option == "0":
        print(f"{Fore.RED}Terima kasih!")    
        sys.exit()
    else:
        print(f"\n{Fore.RED}Pilihan tidak valid, silakan pilih kategori tiket yang tersedia (1/2/0).{Fore.RESET}")
        continue

    if ktg is None:
        continue

    while True:
        banyak = banyak_tiket_dibeli()
    
    # Memastikan total pembelian tidak melebihi 5 tiket
        if banyak + selected_tickets.get(ktg, 0) < 6 :
            total = banyak * harga
            break
        else:
            print(f"{Fore.RED}Maaf, total tiket yang Anda pilih melebihi batas maksimum (5). Silakan kurangi jumlah tiket.{Fore.RESET}")
            continue

    # Menambahkan jumlah tiket yang dipilih ke dalam keranjang pembelian
    if ktg in selected_tickets:
        selected_tickets[ktg] += banyak
    else:
        selected_tickets[ktg] = banyak

    ppn = 0.1 * total
    alltotal = ppn + total
    # Output
    pesanan = [
        [ktg, f'{Fore.GREEN}Rp {harga:,}{Fore.RESET}', selected_tickets[ktg], f'{Fore.GREEN}Rp {total:,}{Fore.RESET}']
    ]
    print(f"{Fore.BLUE}====================================\n{Fore.RESET}")
    print(tabulate(pesanan, headers=["Kategori", "Harga", "Banyak", "Total"], tablefmt="pretty"))

    while True:
        print(f"{Fore.LIGHTYELLOW_EX}\nApakah Anda ingin melanjutkan pembayaran atau kembali ke menu awal?{Fore.RESET}")
        print('[Y] Pembayaran')
        print('[K] Kembali ke awal')
        ulg = input("Y/K: ").lower()
        os.system('cls')

        if ulg in {"y"}:
            # data diri
            print(f"{Fore.LIGHTYELLOW_EX}Melanjutkan proses pembayaran, mohon isi form data diri!{Fore.RESET}")
            print(f"{Fore.BLUE}========================================{Fore.RESET}")
            print("{:^40}".format("INPUT DATA DIRI ANDA"))
            print(f"{Fore.BLUE}========================================{Fore.RESET}")
            nama = input(f"Nama : ")
            while True:
                try:
                    nope = int(input(f"No. Hp : "))
                    break
                except ValueError:
                    print("Harap masukkan angka!")
                
            email = input(f"Email : ")
            os.system('cls')

            # form
            print(f"{Fore.BLUE}========================================{Fore.RESET}")
            print("{:^40}".format("DATA DIRI ANDA"))
            print(f"{Fore.BLUE}========================================{Fore.RESET}")
            print(f"Nama {nama}")
            print(f"No. Hp : {nope}")
            print(f"Email : {email}")
            print(f"{Fore.BLUE}========================================{Fore.RESET}")
            print("Pilih Pembayaran Anda")
            print("[1] BCA \n[2] BRI \n[3] MANDIRI \n ")

            while True:
                try:
                    bayar = int(input("Pilih pembayaran yang tersedia : "))  
                    if bayar == 1:
                        BCA()
                        break
                    elif bayar==2:
                        BRI()
                        break
                    elif bayar==3:
                        MANDIRI()
                        break
                    else:
                        print(f"{Fore.RED}Input yang anda masukkan salah, silahkan input kembali.{Fore.RESET}")
                        continue
                except ValueError: 
                    print("Masukkan Inputan yang")
            break
        elif ulg in {"K", "k"}:
            os.system('')
            print(f"{Fore.YELLOW}Anda kembali ke menu awal!{Fore.RESET}")
            break
        else:
            print(f"{Fore.RED}Mohon masukkan Y atau K untuk melanjutkan atau kembali ke menu awal.{Fore.RESET}")