# Rama stron MATCODE

Jedna rama, wiele programów. Każdy program MATCODE ma własną stronę
(GitHub Pages w swoim repozytorium), ale wszystkie wyglądają jak rodzina:
ten sam krój pisma, te same odstępy, ta sama kolejność sekcji, ta sama
stopka. Różni je **jedna rzecz własna**: akcent wzięty z tematu programu
(Papuga: pasy piór ary). Zasada: *wspólna rama, inna dusza*.

Ten plik jest instrukcją dla człowieka i dla agenta, który robi stronę
kolejnego programu. Szablon startowy leży w `szablon/`.

## Adresy i repozytoria

| Co | Adres | Repozytorium | Lokalnie |
|---|---|---|---|
| Strona główna i rama | https://matmiccode.github.io/ | `matmiccode/matmiccode.github.io` | `C:\Users\it\matmiccode.github.io` |
| Profil GitHub (README) | https://github.com/matmiccode | `matmiccode/matmiccode` | `C:\Users\it\matmiccode` |
| Strona programu | `https://matmiccode.github.io/<program>/` | repo programu, katalog `docs/` | repo programu |

Arkusz ramy: `css/v1/matcode.css` w tym repozytorium, dostępny spod
`/css/v1/matcode.css`. Strona programu linkuje go **ścieżką od korzenia**
(`/css/v1/matcode.css`), bo strony programów żyją pod tą samą domeną.
Zmiana w arkuszu odświeża wszystkie strony; zmiana łamiąca = nowy katalog
`css/v2/`, stare strony zostają przy swojej.

Konto GitHub właściciela: `matmiccode` (`gh auth switch --user matmiccode`).

## Tokeny

**Kolory** (ciemny domyślnie, jasny za ustawieniem systemu przez
`prefers-color-scheme`; wymuszenie przez `data-theme` na `<html>`):

| Zmienna | Ciemny | Jasny | Rola |
|---|---|---|---|
| `--bg` | `#15171c` | `#f4f5f8` | tło strony (grafit, nie czerń; chłodna szarość, nie krem) |
| `--surface` | `#1d2026` | `#ffffff` | karty, pokaz, ramki |
| `--surface-2` | `#262a32` | `#eceef3` | tory pasków, pola |
| `--line` | `#2c3039` | `#dde1e8` | linie oddzielające |
| `--text` | `#e8eaee` | `#15171c` | tekst |
| `--muted` | `#959dab` | `#5b6472` | tekst drugorzędny |
| `--faint` | `#8a93a1` | `#8a93a1` | podpisy, drobny druk |
| `--accent` | `#3b82e0` | `#2563c7` | odnośniki, numery kroków |
| `--accent-strong` | `#2f74d0` | `#1f55ad` | przycisk główny |
| `--ok` | `#4fb47a` | `#2f8f5b` | potwierdzenie |

**Krój pisma:** Bricolage Grotesque (Google Fonts, zmienny, oś opsz), jeden
krój do wszystkiego, `font-optical-sizing: auto`. Tekst 17 px / 1.55.
Nagłówki 600, lekko ściśnięte (`letter-spacing: -0.02em`). Bez wersalików
w etykietach, bez kroju monospace do danych.

**Układ:** `.wrap` o szerokości 1080 px z marginesem 24 px, tekst do lewej,
sekcje po 56 px odstępu (40 px na telefonie), rozdzielone linią `--line`.
Promienie: 10 px karty, 6 px przyciski. Działa od 360 px szerokości.

**Ruch:** najwyżej jedna zaplanowana animacja na wejściu (np. pokaz w hero),
nic nie animuje się przy przewijaniu, `prefers-reduced-motion` wyłącza wszystko.

## Co daje rama (klasy w `matcode.css`)

- `.top`, `.marka` — nagłówek strony z ikoną i nazwą, `nav` z odnośnikami,
  ostatni jako `.btn.btn-primary.btn-sm` (Pobierz). `.ukryj-mobile` chowa
  odnośnik na telefonie.
- `.btn`, `.btn-primary`, `.btn-quiet`, `.btn-sm`, `.cta` (rząd przycisków).
- `section` + `.wrap`, `.sekcja-naglowek` (h2 + jedno zdanie).
- `.kroki` — numerowane kroki; **tylko** gdy treść jest kolejnością.
- `.cechy` — lista `dl` w dwóch kolumnach: nazwa + zdanie, bez kafelków.
- `figure` + `figcaption` — zrzut ekranu z cienką ramką.
- `table` — wymagania (`th` nazwa, `td` wartość).
- `.uwaga` — ramka na jedną ważną informację (np. ostrzeżenie SmartScreen).
- `.programy` / `.program` — lista programów na stronie głównej.
- `footer` — stopka: po lewej „MATCODE · inne programy”, po prawej odnośniki.
- `.piora` — pasek 4 px z gradientu `--pioro-1..4` (podpis Papugi; inny
  program ustawia własne barwy albo go nie używa).
- `.odstep`, `.odstep-duzy`, `.muted`, `.small`.

## Co dokłada strona programu

Plik `docs/<program>.css` obok `index.html`: własne zmienne (np. barwy
podpisu), układ hero i **jeden** element własny — pokaz w hero, który
odpowiada na pytanie „co ten program robi” w pięć sekund. Dla Papugi to
transkrypcja pojawiająca się linijka po linijce z paskiem w barwach piór.
Dla innego programu to będzie coś z jego świata: podgląd wyniku, animacja
jednej operacji, prawdziwy fragment danych. Nie: duża liczba z podpisem,
gradientowe tło, trzy identyczne kafelki z ikonami.

Bohaterem strony jest treść, nie dekoracja. Nagłówek h1 mówi, co program
robi i gdzie (u Ciebie, nie w chmurze); akapit pod nim dodaje jedno zdanie
o tym, czego **nie** robi (nie wysyła, nie wymaga konta). Zdania krótkie,
zdaniową wielkością liter, po polsku, bez emoji.

## Kolejność sekcji strony programu

1. **Hero:** h1, akapit, przyciski „Pobierz <Program> dla Windows”
   (główny) i „Kod źródłowy” (cichy), drobny druk z wersją, systemem,
   licencją. Po prawej pokaz.
2. **Jak to działa** — kroki tylko wtedy, gdy naprawdę są kolejne.
3. **Co potrafi** — `.cechy`, 4–6 pozycji, każda nazwa + jedno zdanie.
4. **Tak wygląda praca** — prawdziwy zrzut okna (nie makieta), podpis.
5. **Prywatność** — co liczy się lokalnie, z czym program się łączy i kiedy,
   otwarty kod, podpisane wydania. Tylko prawda z kodu.
6. **Zanim pobierzesz** — tabela wymagań, `.uwaga` o SmartScreen, drugi raz
   przyciski pobierania, odnośnik do zgłoszeń.
7. **Stopka** — MATCODE · inne programy; Postaw kawę autorowi; licencje;
   GitHub.

Sekcję, która dla danego programu nie ma treści, usuwa się, nie wypełnia
na siłę.

## Nowy program — lista kroków

1. W repozytorium programu: katalog `docs/` z plikami z `szablon/`
   (`index.html` → uzupełnić, `program.css` → przemianować na
   `<program>.css`), `.nojekyll`, `favicon.ico`, `img/` z ikoną 256 px
   i prawdziwym zrzutem okna. Ikona z narzędzia programu, nie z sieci.
2. Podgląd lokalny z układem jak na Pages: katalog roboczy, w nim kopia
   tego repozytorium w korzeniu i `docs/` programu jako `/<program>/`;
   `python -m http.server` i zrzuty (agent-browser) w trybie ciemnym,
   jasnym i przy 390 px szerokości. Sprawdzić: h1 w 2–3 liniach, przyciski
   obok siebie, zrzut się wczytuje (bez `loading="lazy"`).
3. Włączyć Pages z `docs/` gałęzi `main` (albo `master`, jeśli repo tak ma – Nutka):
   `gh api -X POST repos/matmiccode/<repo>/pages -f build_type=legacy -f "source[branch]=main" -f "source[path]=/docs"`.
4. Strona główna (to repo): dodać `<li class="program">` w `index.html`
   (ikona 96 px do `img/`, nazwa, jedno zdanie, system i licencja,
   przyciski „Strona programu” i „Pobierz”), dopisać program do tabeli niżej,
   `git push`.
5. Profil (`C:\Users\it\matmiccode`): wiersz w tabeli `README.md`, ikona
   96 px do `img/`, `git push`.
6. Przycisk „Pobierz” celuje w `releases/latest`; skrypt na stronie podmienia
   go na bezpośredni plik z najnowszego wydania, gdy API GitHuba odpowie.

## Marka: znak, awatar i okładka

Autora i katalog oznacza znak **„Łąka”**: dwie górki o miękkich, zaokrąglonych szczytach ułożone w literę M, każda z dwiema
ścianami (jaśniejsza lewa, ciemniejsza prawa, jak złożony papier) i jednym złotym oknem z poświatą. Znaczenie: M jak MATCODE,
dwa małe domy = małe programy, które mieszkają u Ciebie, a światło w oknie = ktoś w środku pracuje. Zieleń #6fd392/#3fb46f
(ściana jasna) i #2f9a5e/#1f6b42 (ciemna), okno #ffe08a→#ffa63d, tło #1d2026. Programy mają własne ikony (Papuga, Nutka);
znak nigdy ich nie zastępuje. Strona główna huba nosi zieleń znaku jako `--accent` (nadpisanie w jej `<style>`); strony
programów zostają przy swoich akcentach.

Źródła i pliki w `marka/` (`python marka/generuj.py`, Pillow; krój pobierany automatycznie):

- `znak.svg` (bez tła), `znak-kwadrat.svg` (zaokrąglony kwadrat, favicon huba), `znak-kolo.svg` – wektory, jedyne źródło prawdy.
- `matcode-awatar-1024.png` – zdjęcie profilowe na GitHub i buycoffee.to: pełny grafitowy kwadrat, serwis sam przytnie w kółko;
  `matcode-awatar-kolo-1024.png` – to samo w kole z przezroczystym tłem; `matcode-ikona-*.png` – zaokrąglony kwadrat do ikon i kart.
- `matcode-okladka-1500x500.png` (i `-1920x640`) – okładka profilu: grafit, znak, nazwa, hasło, ikony programów, adres w zieleni.
- `teksty-buycoffee.md` – nazwa, opis, cel, podziękowanie na buycoffee.to/matcode, w tonie stron MATCODE.

Nowy program: dopisać go do okładki (`generuj.py`, lista ikon) i wygenerować pliki ponownie. Zmiana znaku = zmiana
`ZNAK_SVG` i funkcji `znak()` w jednym miejscu.

## Programy w ramie

| Program | Repozytorium | Strona | Podpis własny |
|---|---|---|---|
| Papuga – transkrypcje offline | `matmiccode/papuga` | https://matmiccode.github.io/papuga/ | pasy piór ary (`--pioro-1..4`), pokaz transkrypcji |
| Nutka – mp3 z YouTube i Spotify | `matmiccode/nutka` | https://matmiccode.github.io/nutka/ | barwy ikony róż→fiolet (`--nuta-1..3`, pasek `.nuty`, własny `--accent`), pokaz: wpisany tytuł zamienia się w mp3; instrukcja `instrukcja.html` na tej samej ramie, kopiowana obok exe z migawką `matcode.css` |
