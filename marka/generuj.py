"""Znak MATCODE i grafiki profilowe (GitHub, buycoffee.to) w tokenach ramy (RAMA.md).

  python marka/generuj.py            -> marka/matcode-awatar-*.png, marka/matcode-okladka-*.png

Znak M = favicon strony głównej (ta sama ścieżka SVG na siatce 64), zaokrąglony kwadrat --accent-strong.
Krój: Bricolage Grotesque (pobierany do %TEMP% z repozytorium Google Fonts, jeśli go nie ma). Wymaga Pillow.
"""
import os
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

TU = Path(__file__).parent
IMG = TU.parent / "img"
FONT_URL = "https://github.com/google/fonts/raw/main/ofl/bricolagegrotesque/BricolageGrotesque%5Bopsz%2Cwdth%2Cwght%5D.ttf"
FONT = Path(os.environ.get("TEMP", TU)) / "BricolageGrotesque.ttf"
NIEBIESKI, GRAFIT, LINIA, TEKST, SZARY = "#2f74d0", "#15171c", "#2c3039", "#e8eaee", "#959dab"


def kroj(rozmiar: int, waga: str = "SemiBold") -> ImageFont.FreeTypeFont:
    if not FONT.exists():
        urllib.request.urlretrieve(FONT_URL, FONT)
    f = ImageFont.truetype(str(FONT), rozmiar)
    f.set_variation_by_name(waga)
    return f


def znak_m(bok: int, tlo: str = NIEBIESKI, kolor: str = "#ffffff") -> Image.Image:
    """Zaokrąglony kwadrat i litera M (siatka 64 jak w faviconie). Rysowane 4x i zmniejszane = gładkie krawędzie."""
    s = 4
    W = bok * s
    k = W / 64
    im = Image.new("RGBA", (W, W), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, W - 1, W - 1), radius=14 / 64 * W, fill=tlo)
    pkt = [(14, 46), (14, 18), (21, 18), (32, 35), (43, 18), (50, 18), (50, 46), (43, 46), (43, 30), (32, 46), (21, 30), (21, 46)]
    d.polygon([(x * k, y * k) for x, y in pkt], fill=kolor)
    return im.resize((bok, bok), Image.LANCZOS)


def awatary():
    for bok in (1024, 512, 400):
        znak_m(bok).save(TU / f"matcode-awatar-{bok}.png", optimize=True)
    # znak na grafitowym kole - wygląda tak samo, gdy serwis przycina awatar w kółko
    for bok in (1024, 400):
        s = 4
        W = bok * s
        im = Image.new("RGBA", (W, W), (0, 0, 0, 0))
        ImageDraw.Draw(im).ellipse((0, 0, W - 1, W - 1), fill=GRAFIT)
        z = znak_m(int(W * 0.62))
        im.paste(z, ((W - z.width) // 2, (W - z.height) // 2), z)
        im.resize((bok, bok), Image.LANCZOS).save(TU / f"matcode-awatar-kolo-{bok}.png", optimize=True)


def okladka():
    W, H = 1500, 500
    im = Image.new("RGB", (W, H), GRAFIT)
    d = ImageDraw.Draw(im)
    z = znak_m(132)
    im.paste(z, (96, 92), z)
    d.text((256, 84), "MATCODE", font=kroj(96, "Bold"), fill=TEKST)
    d.text((258, 208), "Małe programy, które robią jedną rzecz dobrze.", font=kroj(40, "Medium"), fill=TEKST)
    d.text((258, 262), "Działają na Twoim komputerze, nie w chmurze. Za darmo, z otwartym kodem, po polsku.",
           font=kroj(27, "Regular"), fill=SZARY)
    d.line((96, 356, W - 96, 356), fill=LINIA, width=2)
    x = 96
    for plik, nazwa, opis in (("papuga-256.png", "Papuga", "transkrypcje offline"),
                              ("nutka-256.png", "Nutka", "mp3 z YouTube i Spotify")):
        ik = Image.open(IMG / plik).convert("RGBA").resize((72, 72), Image.LANCZOS)
        im.paste(ik, (x, 392), ik)
        d.text((x + 90, 394), nazwa, font=kroj(30, "SemiBold"), fill=TEKST)
        d.text((x + 90, 434), opis, font=kroj(23, "Regular"), fill=SZARY)
        x += 420
    d.text((W - 96, 418), "matmiccode.github.io", font=kroj(26, "Medium"), fill=NIEBIESKI, anchor="rm")
    im.save(TU / "matcode-okladka-1500x500.png", optimize=True)
    im.resize((1920, 640), Image.LANCZOS).save(TU / "matcode-okladka-1920x640.png", optimize=True)


if __name__ == "__main__":
    awatary()
    okladka()
    print("gotowe:", sorted(p.name for p in TU.glob("matcode-*.png")))
