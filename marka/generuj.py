"""Znak MATCODE „Łąka” (dwie górki w kształcie M, złote okna) i grafiki profilowe (GitHub, buycoffee.to).

  python marka/generuj.py   -> marka/matcode-awatar-*.png, marka/matcode-okladka-*.png, marka/znak*.svg

Geometria znaku na siatce 64 (jak w SVG): dwie górki o zaokrąglonych szczytach, każda z dwiema ścianami
(jaśniejsza lewa, ciemniejsza prawa), w każdej jedno złote okno z poświatą. Prawa górka leży przed lewą.
Krój okładki: Bricolage Grotesque (pobierany do %TEMP% z repozytorium Google Fonts). Wymaga Pillow.
"""
import os
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

TU = Path(__file__).parent
IMG = TU.parent / "img"
FONT_URL = "https://github.com/google/fonts/raw/main/ofl/bricolagegrotesque/BricolageGrotesque%5Bopsz%2Cwdth%2Cwght%5D.ttf"
FONT = Path(os.environ.get("TEMP", TU)) / "BricolageGrotesque.ttf"

GRAFIT, POWIERZCHNIA, LINIA, TEKST, SZARY = "#15171c", "#1d2026", "#2c3039", "#e8eaee", "#959dab"
ZIELEN = "#3fb46f"
JASNA = ("#6fd392", "#3fb46f")   # ściana lewa: góra -> dół
CIEMNA = ("#2f9a5e", "#1f6b42")  # ściana prawa
OKNO = ("#ffe08a", "#ffa63d")    # okno: lewy górny -> prawy dolny
POSWIATA = "#ffd36a"


def kroj(rozmiar: int, waga: str = "SemiBold") -> ImageFont.FreeTypeFont:
    if not FONT.exists():
        urllib.request.urlretrieve(FONT_URL, FONT)
    f = ImageFont.truetype(str(FONT), rozmiar)
    f.set_variation_by_name(waga)
    return f


def _hex(kolor: str) -> tuple[int, int, int]:
    return tuple(int(kolor[i:i + 2], 16) for i in (1, 3, 5))


def _gradient(szer: int, wys: int, od: str, do: str, ukos: bool = False) -> Image.Image:
    """Pionowy (albo ukośny) gradient RGB o zadanym rozmiarze - przez maskę z Image.linear_gradient (szybkie)."""
    maska = Image.linear_gradient("L")  # 256x256, 0 u góry -> 255 u dołu
    if ukos:
        maska = maska.rotate(45, resample=Image.BILINEAR, expand=False)
    maska = maska.resize((szer, wys), Image.BILINEAR)
    return Image.composite(Image.new("RGB", (szer, wys), do), Image.new("RGB", (szer, wys), od), maska)


def _gorka(apex_x: float, k: float):
    """Punkty jednej górki (siatka 64 -> piksele przez k): podstawa od apex-16 do apex+16, zaokrąglony szczyt."""
    pkt = [(apex_x - 16, 50), (apex_x - 2.4, 17.4)]
    # szczyt: krzywa kwadratowa (apex-2.4,17.4) -> (apex,12.4) -> (apex+2.4,17.4)
    p0, p1, p2 = (apex_x - 2.4, 17.4), (apex_x, 12.4), (apex_x + 2.4, 17.4)
    for i in range(1, 12):
        t = i / 12
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pkt.append((x, y))
    pkt += [(apex_x + 2.4, 17.4), (apex_x + 16, 50)]
    return [(x * k, y * k) for x, y in pkt]


def znak(bok: int, tlo: str | None = POWIERZCHNIA, promien: float = 0.0) -> Image.Image:
    """Znak w kwadracie bok x bok. tlo=None -> przezroczyste; promien (0..0.5) = zaokrąglenie rogów tła."""
    s = 4
    W = bok * s
    k = W / 64
    im = Image.new("RGBA", (W, W), (0, 0, 0, 0))
    if tlo:
        ImageDraw.Draw(im).rounded_rectangle((0, 0, W - 1, W - 1), radius=promien * W, fill=tlo)
    for apex in (22, 42):
        pkt = _gorka(apex, k)
        maska = Image.new("L", (W, W), 0)
        ImageDraw.Draw(maska).polygon(pkt, fill=255)
        szczyt, dol = round(12.4 * k), round(50 * k)
        for kolory, maska_sciany in ((CIEMNA, maska), (JASNA, None)):
            if maska_sciany is None:  # lewa ściana = górka przycięta do x < apex
                maska_sciany = maska.copy()
                ImageDraw.Draw(maska_sciany).rectangle((round(apex * k), 0, W, W), fill=0)
            grad = Image.new("RGB", (W, W), kolory[1])
            grad.paste(_gradient(W, dol - szczyt, kolory[0], kolory[1]), (0, szczyt))
            im.paste(grad, (0, 0), maska_sciany)
        # okno z poświatą
        ox, oy, ow, oh = (apex - 9) * k, 37 * k, 6 * k, 7 * k
        glow = Image.new("RGBA", (W, W), (0, 0, 0, 0))
        ImageDraw.Draw(glow).rounded_rectangle((ox, oy, ox + ow, oy + oh), radius=1.6 * k, fill=POSWIATA)
        glow = glow.filter(ImageFilter.GaussianBlur(1.8 * k))
        im.alpha_composite(glow)
        okno_maska = Image.new("L", (W, W), 0)
        ImageDraw.Draw(okno_maska).rounded_rectangle((ox, oy, ox + ow, oy + oh), radius=1.6 * k, fill=255)
        okno = Image.new("RGB", (W, W), OKNO[1])
        okno.paste(_gradient(round(ow) + 1, round(oh) + 1, OKNO[0], OKNO[1], ukos=True), (round(ox), round(oy)))
        im.paste(okno, (0, 0), okno_maska)
    return im.resize((bok, bok), Image.LANCZOS)


ZNAK_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
<defs>
<clipPath id="cl-L"><rect width="22" height="64"/></clipPath><clipPath id="cl-R"><rect width="42" height="64"/></clipPath>
<filter id="glow" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="1.8"/></filter>
<linearGradient id="okno" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffe08a"/><stop offset="1" stop-color="#ffa63d"/></linearGradient>
<linearGradient id="jasna" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6fd392"/><stop offset="1" stop-color="#3fb46f"/></linearGradient>
<linearGradient id="ciemna" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2f9a5e"/><stop offset="1" stop-color="#1f6b42"/></linearGradient>
</defs>
{TLO}
<path d="M6 50 L19.6 17.4 Q22 12.4 24.4 17.4 L38 50 Z" fill="url(#ciemna)"/><path d="M6 50 L19.6 17.4 Q22 12.4 24.4 17.4 L38 50 Z" fill="url(#jasna)" clip-path="url(#cl-L)"/>
<path d="M26 50 L39.6 17.4 Q42 12.4 44.4 17.4 L58 50 Z" fill="url(#ciemna)"/><path d="M26 50 L39.6 17.4 Q42 12.4 44.4 17.4 L58 50 Z" fill="url(#jasna)" clip-path="url(#cl-R)"/>
<rect x="13" y="37" width="6" height="7" rx="1.6" fill="#ffd36a" filter="url(#glow)"/><rect x="45" y="37" width="6" height="7" rx="1.6" fill="#ffd36a" filter="url(#glow)"/>
<rect x="13" y="37" width="6" height="7" rx="1.6" fill="url(#okno)"/><rect x="45" y="37" width="6" height="7" rx="1.6" fill="url(#okno)"/>
</svg>
"""


def wektory():
    (TU / "znak.svg").write_text(ZNAK_SVG.replace("{TLO}\n", ""), encoding="utf-8")
    (TU / "znak-kwadrat.svg").write_text(ZNAK_SVG.replace("{TLO}", '<rect width="64" height="64" rx="16" fill="#1d2026"/>'), encoding="utf-8")
    (TU / "znak-kolo.svg").write_text(ZNAK_SVG.replace("{TLO}", '<circle cx="32" cy="32" r="32" fill="#1d2026"/>'), encoding="utf-8")


def awatary():
    for bok in (1024, 512, 400):
        znak(bok, POWIERZCHNIA, 0).save(TU / f"matcode-awatar-{bok}.png", optimize=True)        # pełny kwadrat: GitHub, buycoffee
        znak(bok, POWIERZCHNIA, 0.25).save(TU / f"matcode-ikona-{bok}.png", optimize=True)      # zaokrąglony kwadrat: ikony, karty
    for bok in (1024, 400):
        s = 4
        W = bok * s
        kolo = Image.new("RGBA", (W, W), (0, 0, 0, 0))
        ImageDraw.Draw(kolo).ellipse((0, 0, W - 1, W - 1), fill=POWIERZCHNIA)
        kolo = kolo.resize((bok, bok), Image.LANCZOS)
        kolo.alpha_composite(znak(bok, None))  # znak sam robi swoje nadpróbkowanie - nie mnożyć go przez s
        kolo.save(TU / f"matcode-awatar-kolo-{bok}.png", optimize=True)  # koło z przezroczystym tłem


def okladka():
    W, H = 1500, 500
    im = Image.new("RGBA", (W, H), GRAFIT)
    d = ImageDraw.Draw(im)
    z = znak(180, None)
    im.alpha_composite(z, (72, 60))
    d.text((276, 84), "MATCODE", font=kroj(96, "Bold"), fill=TEKST)
    d.text((278, 208), "Małe programy na Windows. Klikasz i działa.", font=kroj(40, "Medium"), fill=TEKST)
    d.text((278, 262), "Bez chmury i zakładania kont. Za darmo, z otwartym kodem, po polsku.",
           font=kroj(27, "Regular"), fill=SZARY)
    d.line((96, 356, W - 96, 356), fill=LINIA, width=2)
    x = 96
    for plik, nazwa, opis in (("papuga-256.png", "Papuga", "transkrypcje offline"),
                              ("nutka-256.png", "Nutka", "mp3 z YouTube i Spotify")):
        ik = Image.open(IMG / plik).convert("RGBA").resize((72, 72), Image.LANCZOS)
        im.alpha_composite(ik, (x, 392))
        d.text((x + 90, 394), nazwa, font=kroj(30, "SemiBold"), fill=TEKST)
        d.text((x + 90, 434), opis, font=kroj(23, "Regular"), fill=SZARY)
        x += 420
    d.text((W - 96, 418), "matmiccode.github.io", font=kroj(26, "Medium"), fill=ZIELEN, anchor="rm")
    im = im.convert("RGB")
    im.save(TU / "matcode-okladka-1500x500.png", optimize=True)
    im.resize((1920, 640), Image.LANCZOS).save(TU / "matcode-okladka-1920x640.png", optimize=True)


def okladka_4x1():
    """Okładka 4:1 dla buycoffee.to (kadrowanie tła profilu wymusza 4:1, a na szerokim ekranie widać tylko środkowy
    pas ~6:1, na lewy dolny róg nachodzi awatar) - cała treść w pasie y 85..415, lewy dolny róg pusty."""
    W, H = 2000, 500
    im = Image.new("RGBA", (W, H), GRAFIT)
    d = ImageDraw.Draw(im)
    im.alpha_composite(znak(200, None), (110, 150))
    d.text((350, 146), "MATCODE", font=kroj(104, "Bold"), fill=TEKST)
    d.text((354, 282), "Małe programy na Windows. Klikasz i działa.", font=kroj(40, "Medium"), fill=TEKST)
    d.text((354, 338), "Bez chmury i zakładania kont. Za darmo, z otwartym kodem, po polsku.",
           font=kroj(27, "Regular"), fill=SZARY)
    d.line((1500, 160, 1500, 340), fill=LINIA, width=2)
    x, y = 1560, 160
    for plik, nazwa, opis in (("papuga-256.png", "Papuga", "transkrypcje offline"),
                              ("nutka-256.png", "Nutka", "mp3 z YouTube i Spotify")):
        ik = Image.open(IMG / plik).convert("RGBA").resize((64, 64), Image.LANCZOS)
        im.alpha_composite(ik, (x, y))
        d.text((x + 80, y + 2), nazwa, font=kroj(28, "SemiBold"), fill=TEKST)
        d.text((x + 80, y + 38), opis, font=kroj(21, "Regular"), fill=SZARY)
        y += 96
    d.text((W - 110, 372), "matmiccode.github.io", font=kroj(26, "Medium"), fill=ZIELEN, anchor="rm")
    im.convert("RGB").save(TU / "matcode-okladka-2000x500.png", optimize=True)


if __name__ == "__main__":
    wektory()
    awatary()
    okladka()
    okladka_4x1()
    print("gotowe:", sorted(p.name for p in TU.glob("matcode-*.png")) + sorted(p.name for p in TU.glob("znak*.svg")))
