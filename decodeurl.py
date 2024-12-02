import urllib.parse
import time
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

def print_welcome_message():
    print(Fore.GREEN + Style.BRIGHT + r"""
_  _ _   _ ____ ____ _    ____ _ ____ ___  ____ ____ ___ 
|\ |  \_/  |__| |__/ |    |__| | |__/ |  \ |__/ |  | |__]
| \|   |   |  | |  \ |    |  | | |  \ |__/ |  \ |__| |         
          """)
    print(Fore.GREEN + "Selamat datang di Program Decode URL Data tgWebApp\n")
    print(Fore.YELLOW + "Silakan simpan URL Data tgWebApp di file 'u.txt' dengan aturan 1 akun 1 baris data.")
    print(Fore.YELLOW + "Hasil Decode akan disimpan di 'data.txt'.")
    print(Fore.CYAN + "Telegram: https://t.me/nyariairdrop\n")

def process_account_data(line):
    # Mengambil substring setelah '#tgWebAppData=' sampai sebelum '&tgWebAppVersion'
    start = line.find('#tgWebAppData=') + len('#tgWebAppData=')
    end = line.find('&tgWebAppVersion=')
    
    if start != -1 and end != -1:
        # Mengambil data yang dienkode
        encoded_data = line[start:end]
        # Mendekode URL encoded data
        processed_data = urllib.parse.unquote(encoded_data)
        return processed_data
    else:
        return None

def process_file(input_file, output_file, delay=2):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
            input_count = len(lines)
        
        with open(output_file, 'w') as output:
            success_count = 0
            
            for i, line in enumerate(lines, 1):
                result = process_account_data(line.strip())
                
                if result:
                    output.write(f"{result}\n")
                    print(Fore.GREEN + f"Akun {i} berhasil diproses.")
                    success_count += 1
                else:
                    output.write(f"Failed to process account {i}: Invalid format.\n")
                    print(Fore.YELLOW + f"Akun {i} gagal diproses: Format tidak valid.")
                
                print(Fore.CYAN + f"Menunggu {delay} detik sebelum melanjutkan...\n")
                time.sleep(delay)  # Jeda waktu sebelum memproses akun berikutnya

        # Cetak informasi jumlah akun
        print(Fore.GREEN + f"Jumlah akun di '{input_file}': {input_count}")
        print(Fore.GREEN + f"Jumlah akun berhasil diproses di '{output_file}': {success_count}")
        print(Fore.YELLOW + f"Jumlah akun gagal diproses: {input_count - success_count}\n")

    except FileNotFoundError:
        print(Fore.RED + f"Error: File '{input_file}' tidak ditemukan.")
        print(Fore.YELLOW + "Solusi: Pastikan file tersebut berada di direktori yang sama dengan program ini.")
    
    except Exception as e:
        print(Fore.RED + f"Error: Terjadi kesalahan saat memproses file. {e}")
        print(Fore.YELLOW + "Solusi: Periksa isi file untuk memastikan format data benar dan tidak ada karakter yang merusak parsing.")

if __name__ == "__main__":
    print_welcome_message()
    process_file('u.txt', 'data.txt', delay=2)
