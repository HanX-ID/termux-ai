#!/data/data/com.termux/files/usr/bin/bash

# Warna
hijau='\033[1;32m'
biru='\033[1;34m'
putih='\033[1;37m'
reset='\033[0m'

clear
echo -e "${biru}[+]${reset} ${putih}Menginstall paket yang dibutuhkan...${reset}"
echo

# Install paket
pkg update -y && pkg upgrade -y
pkg install python -y
pkg install python-pip -y

# Install modul requests
echo -e "${biru}[+]${reset} ${putih}Menginstall modul Python 'requests'...${reset}"
pip install requests

# Pindahkan main.py jadi perintah 'ai'
echo -e "${biru}[+]${reset} ${putih}Memasang script ke \$PREFIX/bin/ai...${reset}"
mv main.py $PREFIX/bin/ai
chmod +x $PREFIX/bin/ai

# Finishing
cd $HOME
clear
sleep 0.5

echo
echo -e "${hijau}[✓] Semua paket berhasil diinstall dan siap digunakan.${reset}"
echo -e "${putih}Ketik seperti berikut untuk mulai:${reset} ${biru}ai [pesan]${reset}"
echo