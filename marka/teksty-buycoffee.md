# Teksty marki MATCODE (buycoffee.to/matcode, GitHub, okładki)

Ton: krótko, lekko, po ludzku, bez emoji w treści (poza podziękowaniem), bez proszenia i bez „celów zbiórki”.
Kawa to zwykłe „dzięki, przydało się”. Programy są i zostaną darmowe. Wersje angielskie idą pod polskimi.

## Nazwa wyświetlana

MATCODE

## Hasło (hub `index.html`, okładki w `generuj.py`, bio GitHub)

PL: Małe programy na Windows. Klikasz i działa. Bez chmury i zakładania kont.
EN: Small Windows apps. Click and it works. No cloud, no sign-up.

Okładki: wiersz 1 „Małe programy na Windows. Klikasz i działa.”, wiersz 2 „Bez chmury i zakładania kont. Za darmo, z otwartym kodem, po polsku.”

## Bio GitHub (137 znaków, limit 160)

Małe programy na Windows. Klikasz i działa. Bez chmury i zakładania kont. · Small Windows apps. Click and it works. No cloud, no sign-up.

## Opis na buycoffee („Dlaczego warto Cię wesprzeć?”, limit 2000 znaków)

Cześć, tu MATCODE. Robię małe darmowe programy na Windows, bo zmęczyło mnie,
że do każdej drobnej rzeczy trzeba dziś zakładać konto i płacić abonament.

Papuga spisuje nagrania i wie, kto mówi, a nagrania nigdzie z Twojego komputera nie wychodzą.
Nutka robi z YouTube i Spotify porządne mp3 z okładką i tagami, także całe playlisty.
Oba są za darmo, po polsku, z otwartym kodem. I takie zostaną.

Kawa to zwykłe „dzięki, przydało się”. Programy nic na niej nie zyskują,
za to ja mam paliwo na kolejną poprawkę, gdy YouTube znów coś zmieni.

Pomysł albo błąd: github.com/matmiccode. Wszystkie programy: matmiccode.github.io

—

Hi, MATCODE here. I make small free Windows apps, because I got tired of needing
an account and a subscription for every little thing.

Papuga transcribes recordings and knows who said what. Your recordings never leave your computer.
Nutka turns YouTube and Spotify into proper mp3s with cover art and tags, whole playlists too.
Both are free and open source, and they'll stay that way. The interface is Polish for now,
English is on the way.

A coffee is a simple "thanks, that helped". The apps gain nothing from it,
but I get fuel for the next fix when YouTube changes something again.

Ideas or bugs: github.com/matmiccode. All apps: matmiccode.github.io

## Podziękowanie po wpłacie

PL: Grazie! Kawa dotarła! Myślę o Tobie ciepło :)
EN: Grazie! The coffee has arrived! Warm thoughts your way :)

## Sugerowane kwoty

10 zł · 20 zł · 30 zł (domyślne platformy; bez nazw poziomów, bez „nagród”).

## Linki

- Strona: https://matmiccode.github.io
- GitHub: https://github.com/matmiccode

## Grafiki (ten folder)

- Zdjęcie profilowe: `matcode-awatar-1024.png` (dwie zielone górki w M, pełny grafitowy kwadrat; serwis sam przytnie w kółko).
  Ten sam plik na GitHub (Settings → Public profile → Profile picture) i na buycoffee.to.
  Kadrowanie na buycoffee (vue-advanced-cropper) nie obejmie kołem całego kwadratu – obraz da się oddalić kółkiem myszy tylko do
  ok. 86 % – więc tam wgrany został ten sam znak zmniejszony do 870 px na grafitowym tle 1024 px (plik tymczasowy, bez repo).
- Okładka: `matcode-okladka-1500x500.png` (3:1, baner README profilu = `matmiccode/img/matcode-okladka.png`) albo `-1920x640` –
  od 2026-10-07 też bez znaku i nazwy (na stronie profilu GitHub awatar i „MATCODE” stoją obok README).
  **buycoffee.to kadruje tło profilu do 4:1** i na szerokim ekranie pokazuje tylko środkowy pas ok. 6:1 (awatar nachodzi na lewy dolny róg) –
  tam idzie `matcode-okladka-2000x500.png` (`okladka_4x1()` w `generuj.py`: treść w pasie y 85..415, lewy dolny róg pusty,
  **bez znaku i nazwy** – są już w awatarze i nagłówku profilu; tylko hasło PL/EN z zielonym akcentem i programy po prawej).
- Awatar na buycoffee: `matcode-awatar-pierscien-1024.png` (jasny pierścień, bo koło nachodzi na ciemną okładkę); kadrowanie oddalić do maksimum.
  Po zmianie hasła: `generuj.py` (Pillow z `build\venv` Nutki), skopiować 1500x500 do profilu, wgrać 2000x500 na buycoffee
  (kadrowanie → „Zapisz” w oknie → „Zapisz” pod sekcją, dopiero to zapisuje).
- Ikony programów zostają własne (Papuga, Nutka); znak „Łąka” oznacza autora i katalog.
