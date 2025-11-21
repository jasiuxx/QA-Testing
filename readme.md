# Projekt - Test vod.film

---

## OPIS
Projekt ma na celu zaprezentować moje rozwiązanie na testowanie workflow oraz api na stronie `https://vod.film/filmy`. W projekcie zostały utworzone testy za pomocą Playwright oraz Pytest. Testy sprawdzają poprawność wyszukiwania fraz za pomocą UI oraz endpointu API. Dodatkowo do projektu jest dołączony plik raport_bledow.md będacy wynikiem testu manualnego sekcji sortowania.

## Spis treści
1. [Opis](#opis)
2. [Wymagania wstępne](#wymagania-wstępne)
3. [Struktura projektu](#struktura-projektu)
4. [Uruchomienie projektu](#uruchomienie-projektu)
5. [Workflow testów](#workflow-testów)
6. [Konteneryzacja](#konteneryzacja)
7. [Rozwiązywanie problemów](#rozwiązywanie-problemów)
8. [Raporty](#raporty)
9. [Uzasadnienie wyboru playwright](#uzasadnienie-wyboru-playwright)
10. [Raport błędów](#raport-błedów)


## Workflow 1 Test E2E
1. Wejście na stronę vod.film
2. Wyszukanie frazy
3. Sprawdzenie czy fraza jest dostępna na liśćie filmów
4. Wejście na stronę szczegółów filmu 
5. Sprawdzenie czy fraza zawiera sie w h1
6. Sprawdzenie dostępności przycisku play
7. Kliknięcie popup w odstępie 1-60 sekund od startu odtwarzania
8. Przejście na stronę z popup


## Workflow 2 Test API
1. **Identyfikacja endpointu:**
   - Request URL: https://vod.film/search-route
   - Request method: POST
   - Input data: host(adres), locale(region/język), searchTerm(fraza)
   - Accept: application/json 
   - Content-type applicaiton/json
2. Stworzenie testu pytającego API
3. Zapytanie o fraze
4. Weryfikacja statusu 2xx
5. Sprawdzenie czy fraza jest w odpowiedzi API

## Workflow 3 Test manualny
1. Analiza problemu sortowania
2. Sprawdzenie konsoli oraz Network
3. Poszukiwanie innego błędu
4. Inny błąd znaleziony to niepoprawna obsługa filtrowania na mobile
5. Wykonanie raportu 

## Struktura projektu
1. Test workflow nr 1 znajduje się w tests/pom_vod_test.py
2. Test workflow nr 2 znajduje się w tests/api/test_api_get.py

## Uruchomienie projektu 

## Wymagania wstępne
- Python 3.10
- Docker Desktop (dla konteneryzacji)

**Lokalnie** 
1. pip install -r requirements.txt
2. playwright install --with-deps chromium chrome
3. pytest

**Github actions**
Testy uruchamiają się automatycznie przy każdym push/pull request
Plik konfiguracyjny: `.github/workflows/pytest.yml`

## Konteneryzacja

### Uruchomienie 
0. Wymagane pliki Dockerfile oraz docker-compose.yml
1. Budowa kontenera  
- docker-compose build
2. Jednorazowe wykonanie w kontenerze wszystkich testów
- docker-compose run --rm playwright-tests
3. Jednorawzowe wykonanie tylko testów api 
- docker-compose run --rm playwright-tests pytest tests/api/
4. Jednorawzowe wykonanie tylko testów api 
- docker-compose run --rm playwright-tests pytest tests/pom_vod_test.py






## Uzasadnienie wyboru playwright
Wybrałem playwright z racji tego, że jest nowszym nardzędziem, szybszym i łatwiejszym do nauki niż Selenium. Dowiedziałem się tego na podstawie opinii użytkowników w sieci oraz Perplexity.






# RAPORT BŁĘDÓW
---

## 1. INFORMACJE PODSTAWOWE

| **Tytuł** | Przycisk "Wyczyść" nie resetuje sortowania listy |
| **Data Zgłoszenia** | 21-11-2025 |
| **Zgłaszający** | Jan Szczudło |
| **Priorytet** | Niski |
| **Status** | Nowy |
| **Wersja** | Nieznana |
| **Środowisko** | Produkcyjne |

---

## 2. OPIS PROBLEMU

**Streszczenie:**

### Błąd sortowania w wersji Desktop:
Przycisk "Wyczyść" znajdujący się obok listy rozwijanej sortowania nie wykonuje żadnej akcji po kliknięciu. Oczekiwanym zachowaniem jest resetowanie zastosowanego sortowania do wartości domyślnej, jednak przycisk jest nieaktywny / nie reaguje na interakcję użytkownika.

### Błąd sortowania w wersji Mobile:
Po kliknięciu opcji sortowania, użytkownik ma dostęp do rozszerzonych opcji filtrowania:
- **Gatunki** - przycisk "Wyczyść" **działa częściowo** (zaznaczone wartości są czyszczone w UI, ale filtrowanie nadal pozostaje aktywne i nie jest usuwane)
- **Ocena** - przycisk "Wyczyść" **działa częściowo** (filtr jest czyszczony i usuwany, ale wybrana wartość pozostaje zaznaczona w UI)
- **Rok wydania** - przycisk "Wyczyść" **działa częściowo** (filtr jest czyszczony i usuwany, ale wybrana wartość pozostaje zaznaczona w UI)
- **Sortuj wg** - przycisk "Wyczyść" **nie działa** (sortowanie nie jest resetowane i wybrana wartość pozostaje zaznaczona w UI); dodatkowo dostępne są tylko 3 opcje sortowania w wersji mobilnej (w wersji przeglądarki dostępnych jest 6 opcji)

**Zakres Wpływu:**
- Kosmetyczny błąd UI

---

## 3. KROKI DO REPRODUKCJI

### Wersja Web (Desktop):
1. Otwórz stronę: `https://vod.film/filmy`
2. Zlokalizuj sekcję z listą elementów
3. Kliknij w rozwijaną listę "Sortuj wg."
4. Wybierz dowolną opcję sortowania (np. "Oceny rosnąco")
5. **Zweryfikuj, że lista została posortowana**
6. Kliknij przycisk "Wyczyść" znajdujący się obok listy rozwijanej
7. **Zaobserwuj błąd:** Sortowanie nie zostaje zresetowane

### Wersja Mobile:
1. Otwórz stronę: `https://vod.film/filmy` na urządzeniu mobilnym
2. Kliknij w rozwijaną listę "Sortuj wg."
3. Dostępne opcje filtrowania: Gatunki, Ocena, Rok wydania, Sortuj wg
4. **Test 1 - Gatunki:**
   - Wybierz dowolny gatunek
   - Kliknij "Wyczyść"
   - **Zaobserwuj błąd:** Zaznaczone wartości są czyszczone w UI, ale filtrowanie nadal pozostaje aktywne (lista nie wraca do stanu niefiltrowanego)
5. **Test 2 - Ocena:**
   - Wybierz wartość (np. 8.1)
   - Kliknij "Wyczyść"
   - **Zaobserwuj błąd:** Filtr jest czyszczony i usuwany, ale wartość 8.1 pozostaje zaznaczona w UI
6. **Test 3 - Rok wydania:**
   - Wybierz rok
   - Kliknij "Wyczyść"
   - **Zaobserwuj błąd:** Filtr jest czyszczony i usuwany, ale wybrana wartość pozostaje zaznaczona w UI
7. **Test 4 - Sortuj wg:**
   - Zauważ, że dostępne są tylko 3 opcje (w wersji desktop jest 6)
   - Wybierz dowolną opcję sortowania
   - Kliknij "Wyczyść"
   - **Zaobserwuj błąd:** Sortowanie nie zostaje zresetowane i wybrana wartość pozostaje zaznaczona w UI

**Częstotliwość:** 
Zawsze 

**Pierwsze wykrycie:** 
21.11.2025

---

## 4. OCZEKIWANY REZULTAT

Po kliknięciu przycisku "Wyczyść":
- Zastosowane sortowanie/filtrowanie zostaje anulowane
- Lista powraca do sortowania domyślnego 
- Rozwijana lista "Sortuj wg" nie wyświetla żadnej zaznaczonej opcji
- Wszystkie wybrane wartości filtrów są usuwane z UI

---

## 5. RZECZYWISTY REZULTAT

### Wersja Web (Desktop):
Po kliknięciu przycisku "Wyczyść":
- Brak jakiejkolwiek reakcji UI
- URL pozostaje z parametrami: `?vote_average=asc&popularity=desc&release_date=asc`
- Sortowanie pozostaje aktywne
- Lista nie zmienia kolejności elementów
- W konsoli przeglądarki brak błędów
- W zakładce Network:
    - Brak zapytania do aplikacji (GET/POST do `/filmy` lub API)
    - Widoczne tylko zapytanie Facebook Pixel tracking: `facebook.com/privacy_sandbox/pixel/register/trigger/` z parametrem `buttonText=Wyczyść`

### Wersja Mobile:
Po kliknięciu przycisku "Wyczyść" w poszczególnych sekcjach:
- **Gatunki:** Zaznaczone wartości są czyszczone w interfejsie użytkownika, ale filtrowanie nadal pozostaje aktywne (lista nie wraca do stanu niefiltrowanego)
- **Ocena:** Filtr jest usuwany z URL/zapytania i lista wraca do stanu niefiltrowanego, ale w interfejsie użytkownika wybrana wartość (np. 8.1) pozostaje zaznaczona
- **Rok wydania:** Filtr jest usuwany z URL/zapytania i lista wraca do stanu niefiltrowanego, ale w interfejsie użytkownika wybrana wartość pozostaje zaznaczona
- **Sortuj wg:** Brak reakcji - sortowanie pozostaje aktywne i wybrana wartość pozostaje zaznaczona w UI; dodatkowo w wersji mobilnej widoczne są tylko 3 opcje sortowania zamiast 6 dostępnych w wersji desktop

---

## 6. DANE TECHNICZNE

### Środowisko Testowe
- **Przeglądarka:** [Chrome 142.0.7444.163 / Chrome 143.0.7499.38 Mobile / Firefox 144.0 / Safari mobile]
- **System OS:** [Windows 11 version 25H2 / iOS 18.6.2]
- **Urządzenie:** [Desktop / Mobile]






















