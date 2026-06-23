# SmartRoom – System Rezerwacji Sal Uczelnianych (SRSU)

## 🎯 Cel projektu
SmartRoom to webowa aplikacja stworzona w celu zautomatyzowania procesu rezerwacji sal dydaktycznych. System umożliwia studentom i wykładowcom szybkie wyszukiwanie dostępnych zasobów oraz eliminację duplikowania rezerwacji.

## ✨ Główne funkcjonalności (User Stories)
*   **US1: Wyszukiwanie sal** – Filtrowanie sal według minimalnej pojemności.
*   **US2: Rezerwacja sal** – System rezerwacji w czasie rzeczywistym z walidacją konfliktów czasowych.
*   **US3: Bezpieczeństwo** – Autoryzacja użytkowników z wykorzystaniem hashowania haseł (SHA256).

## 🛠️ Stos technologiczny
*   **Backend:** Python 3.x, Django Framework.
*   **Frontend:** HTML5, CSS3, Bootstrap 5 (Responsive Web Design).
*   **Baza danych:** PostgreSQL.
*   **Kontrola wersji:** Git / GitHub.

## 🚀 Instrukcja uruchomienia
1. Sklonuj repozytorium: `git clone <url-twojego-repozytorium>`
2. Zainstaluj wymagane biblioteki: `pip install django psycopg2`
3. Skonfiguruj bazę danych PostgreSQL w `settings.py`.
4. Wykonaj migracje: `python manage.py migrate`
5. Uruchom serwer: `python manage.py runserver`

## 📈 Status projektu
Obecnie projekt znajduje się na etapie **8. Testowanie i poprawki** (zgodnie z harmonogramem). Wszystkie wymagania funkcjonalne (US1-US3) zostały pomyślnie zaimplementowane w prototypie.

---
**Prowadzący:** mgr Wojciech Moniuszko
**Autor:** Aruzhan Berdaly