#!/usr/bin/env python3

import sys
import requests
import re
import time

BIRU = '\033[94m'
PUTIH = '\033[97m'
RESET = '\033[0m'

def bersihin(teks):
    teks = re.sub(r'[\*\`\\]','', teks)
    return teks

def ketik_berderet(teks, warna_teks=PUTIH, delay=0.02):
    for char in teks:
        print(f"{warna_teks}{char}{RESET}", end='', flush=True)
        time.sleep(delay)
    print()

def main():
    if len(sys.argv) < 2:
        print(f"{BIRU}\nGunakan : ai [pesan]{RESET}\n")
        return

    pesan = ' '.join(sys.argv[1:])
    url = f"https://api.nekorinn.my.id/ai/ai4chat?text={pesan}"

    try:
        res = requests.get(url)
        data = res.json()

        if data.get("status") and "result" in data:
            hasil = bersihin(data["result"])
            print(f"\n{BIRU}[ PESAN AI ] {RESET}", end='')
            ketik_berderet(hasil, warna_teks=PUTIH)
        else:
            print(f"\n{BIRU}[ PESAN AI ] {RESET}", end='')
            ketik_berderet("Server AI sedang Error!", warna_teks=PUTIH)

    except Exception as e:
        print(f"\n{BIRU}[ PESAN AI ] {RESET}", end='')
        ketik_berderet(f"Error -> {e}", warna_teks=PUTIH)

if __name__ == "__main__":
    main()
