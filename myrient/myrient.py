#!/usr/bin/env python3

import os
import subprocess
import sys

full_rips = [
    # NES
    "/files/No-Intro/Nintendo - Nintendo Entertainment System (Headered)/",
    "/files/No-Intro/Nintendo - Nintendo Entertainment System (Headered) (Private)/",
    # SNES
    "/files/No-Intro/Nintendo - Super Nintendo Entertainment System/",
    "/files/No-Intro/Nintendo - Super Nintendo Entertainment System (Private)/",
    "/files/No-Intro/Nintendo - Satellaview/",
    "/files/No-Intro/Nintendo - Satellaview (Aftermarket)/",
    # SEGA
    "/files/No-Intro/Sega - Mega Drive - Genesis/",
    "/files/No-Intro/Sega - Mega Drive - Genesis (Aftermarket)/",
    "/files/No-Intro/Sega - Mega Drive - Genesis (Private)/",
    "/files/No-Intro/Sega - 32X/",
    "/files/No-Intro/Sega - 32X (Aftermarket)/",
    # GB
    "/files/No-Intro/Nintendo - Game Boy/",
    "/files/No-Intro/Nintendo - Game Boy (Private)/",
    # GBC
    "/files/No-Intro/Nintendo - Game Boy Color/",
    "/files/No-Intro/Nintendo - Game Boy Color (Private)/",
    # GBA
    "/files/No-Intro/Nintendo - Game Boy Advance/",
    "/files/No-Intro/Nintendo - Game Boy Advance (Multiboot)/",
    "/files/No-Intro/Nintendo - Game Boy Advance (Play-Yan)/",
    "/files/No-Intro/Nintendo - Game Boy Advance (Private)/",
    "/files/No-Intro/Nintendo - Game Boy Advance (Video)/",
    "/files/No-Intro/Nintendo - Game Boy Advance (e-Reader)/",
    # N64
    "/files/No-Intro/Nintendo - Nintendo 64 (BigEndian)/",
    "/files/No-Intro/Nintendo - Nintendo 64 (BigEndian) (Private)/",
    "/files/No-Intro/Nintendo - Nintendo 64DD/",
    # NDS
    "/files/No-Intro/Nintendo - Nintendo DS (DSvision SD cards)/",
    "/files/No-Intro/Nintendo - Nintendo DS (Decrypted)/",
    "/files/No-Intro/Nintendo - Nintendo DS (Decrypted) (Private)/",
    "/files/No-Intro/Nintendo - Nintendo DS (Download Play)/",
    "/files/No-Intro/Nintendo - Nintendo DSi (Decrypted)/",
    "/files/No-Intro/Nintendo - Nintendo DSi (Digital)/",
    "/files/No-Intro/Nintendo - Nintendo DSi (Digital) (CDN) (Decrypted)/",
    # NEC shit
    "/files/No-Intro/NEC - PC Engine - TurboGrafx-16/",
    "/files/No-Intro/NEC - PC Engine - TurboGrafx-16 (Aftermarket)/",
    "/files/No-Intro/NEC - PC Engine - TurboGrafx-16 (Private)/",
    "/files/No-Intro/NEC - PC Engine SuperGrafx/",
    "/files/No-Intro/NEC - PC Engine SuperGrafx (Aftermarket)/",
    #iQue
    "/files/No-Intro/iQue - iQue (CDN)/",
    "/files/No-Intro/iQue - iQue (Decrypted)/",
    # XBOX 360 TITLE UPDATES
    "/files/No-Intro/Unofficial - Microsoft - Xbox 360 (Title Updates)/",
    # misc
    # "/files/No-Intro/Nintendo - Misc/",
]

curated = {
    # XBOX
    "/files/Redump/Microsoft - Xbox/" : [
        "Halo - Combat Evolved (USA).zip",
        "Halo 2 (USA, Europe) (En,Ja,Fr,De,Es,It,Zh,Ko).zip",
        "Super Monkey Ball Deluxe (USA).zip",
    ],
    # XBOX 360
    "/files/Redump/Microsoft - Xbox 360/" : [
        "DoDonPachi Dai-Ou-Jou Black Label Extra (Japan).zip",
        "DoDonPachi Daifukkatsu Black Label (Japan).zip",
        "DoDonPachi Daifukkatsu Ver 1.5 (Japan).zip",
        "DoDonPachi Saidaioujou (Japan).zip",
        "Muchi Muchi Pork! & Pink Sweets (Japan).zip",
        "Espgaluda II Black Label (Japan) (Shokai Genteiban).zip",
        "Espgaluda II Black Label (Japan).zip",
        "Mushihimesama Futari Ver 1.5 (Japan).zip",
        "Mushihimesama HD (Japan).zip",
        "Raiden IV (USA).zip",
        "Raiden Fighters Aces (USA).zip",
        "Akai Katana (USA).zip",
        "Deathsmiles (USA).zip",
        "Deathsmiles II X - Makai no Merry Christmas (Japan).zip",
        "Ketsui - Kizuna Jigoku-tachi Extra (Japan).zip",
        "Gears of War (World) (En,Fr,De,Es,It,Zh,Ko).zip",
    ],
    # XBLA
    "/files/No-Intro/Microsoft - Xbox 360 (Digital)/" : [
        "Guwange (World) (XBLA).zip",
        "Radiant Silvergun (World) (XBLA).zip",
        "RayStorm HD (World) (XBLA).zip",
    ],
    # GCN
    "/files/Redump/Nintendo - GameCube - NKit RVZ [zstd-19-128k]/" : [
        "Legend of Zelda, The - The Wind Waker (USA, Canada).zip",
        "Legend of Zelda, The - Twilight Princess (USA).zip",
        "Legend of Zelda, The - Four Swords Adventures (USA).zip",
        "F-Zero GX (USA).zip",
        "Sonic Mega Collection (USA).zip",
        "Sonic Gems Collection (USA).zip",
        "Sonic Adventure DX - Director's Cut (USA) (En,Ja,Fr,De,Es).zip",
        "Sonic Adventure 2 - Battle (USA) (En,Ja,Fr,De,Es).zip",
        "Sonic Heroes (USA) (En,Ja,Fr,De,Es,It).zip",
        "Shadow the Hedgehog (USA) (En,Ja,Fr,De,Es,It).zip",
        "Kirby Air Ride (USA).zip",
        "Legend of Zelda, The - Collector's Edition (USA, Canada).zip",
        "Metroid Prime (USA).zip",
        "Metroid Prime (USA) (Rev 2).zip",
        "Metroid Prime 2 - Echoes (USA).zip",
        "Metroid Prime 2 - Echoes (USA, Canada) (Bonus Disc).zip",
        "Paper Mario - The Thousand-Year Door (USA).zip",
        "Soulcalibur II (USA).zip",
        "Super Monkey Ball (USA).zip",
        "Super Monkey Ball 2 (USA).zip",
        "Super Smash Bros. Melee (USA) (En,Ja).zip",
        "Super Smash Bros. Melee (USA) (En,Ja) (Rev 1).zip",
        "Super Smash Bros. Melee (USA) (En,Ja) (Rev 2).zip",
        "WarioWare, Inc. - Mega Party Game$! (USA).zip",
        "Super Mario Sunshine (USA, Canada).zip",
        "Cubivore - Survival of the Fittest (USA).zip",
        "I-Ninja (USA).zip",
    ],
    # Wii
    "/files/Redump/Nintendo - Wii - NKit RVZ [zstd-19-128k]/" : [
        "Legend of Zelda, The - Skyward Sword (USA) (En,Fr,Es) (Rev 2).zip",
        "Legend of Zelda, The - Twilight Princess (USA) (En,Fr,Es) (Rev 2).zip",
        "Super Mario Galaxy (USA) (En,Fr,Es).zip",
        "Super Mario Galaxy 2 (USA) (En,Fr,Es).zip",
        "Rhythm Heaven Fever (USA).zip",
        "Super Paper Mario (USA) (Rev 2).zip",
        "Metroid Prime Trilogy (USA).zip",
        "Excite Truck (USA).zip",
        "WarioWare - Smooth Moves (USA) (En,Fr,Es).zip",
    ],
    # PS2
    "/files/Redump/Sony - PlayStation 2/" : [
        "Onimusha - Warlords (USA).zip",
        "Espgaluda (Japan).zip",
        "DoDonPachi Dai-Ou-Jou (Japan).zip",
        "Mushihimesama (Japan).zip",
    ],
}

if len(sys.argv) < 2:
    print("Usage: myrient [ROM_PATH]")
    sys.exit(1)

CONFIG_PATH = os.path.abspath("rclone.conf")
ROM_PATH = sys.argv[1]
os.chdir(ROM_PATH)

for p in full_rips:
    d = os.path.basename(os.path.normpath(p))
    os.makedirs(d, exist_ok=True)
    os.chdir(d)
    print(f"copying {d}")
    subprocess.run(
        [
            "rclone",
            "--config", CONFIG_PATH,
            "copy",
            f"myrient:{p}",
            ".",
            "--progress",
            "--http-no-head",
            "--size-only",
        ],
        check=True,
    )
    os.chdir(ROM_PATH)

for source_dir, filenames in curated.items():
    dest_dir = os.path.basename(os.path.normpath(source_dir))
    os.makedirs(dest_dir, exist_ok=True)
    target_dir = os.path.abspath(dest_dir)

    for filename in filenames:
        print(f"copying {filename}")
        subprocess.run(
            [
                "rclone",
                "--config", CONFIG_PATH,
                "copy",
                f"myrient:{source_dir}",
                target_dir,
                "--include", filename,
                "--progress",
                "--size-only",
                "--http-no-head",
            ],
            check=True,
        )
