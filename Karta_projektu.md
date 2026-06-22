# KARTA PROJEKTU - SmartRoom

## 1. Informacje ogólne
*   **Tytuł projektu:** SmartRoom – System Rezerwacji Sal Uczelnianych [1]
*   **Akronim projektu:** SRSU [1]
*   **Data utworzenia:** 22.06.2026
*   **Wersja dokumentu:** 1.0
*   **Zespół projektowy:** Aruzhan Berdaly [1]

## 2. Cel projektu
Celem projektu SmartRoom jest opracowanie i wdrożenie webowej aplikacji do rezerwacji sal uczelnianych, umożliwiającej [2]:
*   szybkie wyszukiwanie dostępnych sal przez studentów i wykładowców,
*   rezerwowanie terminów zajęć, konsultacji lub spotkań,
*   przeglądanie kalendarza dostępności w czasie rzeczywistym,
*   otrzymywanie powiadomień e-mail o potwierdzeniu lub anulowaniu rezerwacji [2].

## 3. Uzasadnienie projektu
Obecny proces rezerwacji odbywa się mailowo lub telefonicznie, co prowadzi do duplikowania rezerwacji и braku przejrzystości kalendarza [3]. System zautomatyzuje i scentralizuje ten proces [3].

## 4. Zakres projektu
**W zakresie projektu [3]:**
*   Opracowanie wymagań funkcjonalnych i niefunkcjonalnych.
*   Zaprojektowanie systemu z wykorzystaniem UML.
*   Implementacja aplikacji w technologii Django + Bootstrap.
*   Utworzenie relacyjnej bazy danych (PostgreSQL).
*   Stworzenie pełnej dokumentacji technicznej.

**Poza zakresem projektu [4]:**
*   Integracja z systemami dziekanatowymi.
*   Mobilna wersja natywna.
*   Integracja z uczelnianym LDAP-em.

## 5. Główne wymagania
| Typ | Opis |
| --- | --- |
| **Funkcjonalne** | Rezerwacja sal, logowanie, wyszukiwanie według daty i sali, powiadomienia e-mail [4]. |
| **Niefunkcjonalne** | Czas odpowiedzi max 3 sekundy, dostępność 99%, responsywność interfejsu [4]. |
| **Bezpieczeństwo** | Logowanie z użyciem haseł SHA256, role: użytkownik/admin [4]. |

## 6. Zasoby i narzędzia
*   **Repozytorium:** GitHub [5]
*   **Programowanie:** Python (Django), HTML/CSS/Bootstrap [5]
*   **Baza danych:** PostgreSQL [5]
*   **Analiza:** Visual Paradigm, Mermaid [5]

## 7. Harmonogram realizacji
1.  Karta projektu i struktura zespołu (Tydzień 1) [6].
2.  Analiza wymagań (Tydzień 2) [6].
3.  Projekt systemu – UML (Tydzień 3–4) [6].
4.  Implementacja prototypu (Tydzień 6–7) [6].
5.  Testowanie i dokumentacja końcowa (Tydzień 8–10) [6].

## 8. Kryteria sukcesu
*   Wszystkie wymagania funkcjonalne zostały zaimplementowane [7].
*   Dokumentacja zawiera pełny zestaw diagramów UML [7].
*   Aplikacja uruchamia się lokalnie i działa poprawnie [7].

## 9. Akceptacja projektu
*   **Prowadzący:** mgr Wojciech Moniuszko
*   **Kierownik projektu:** Aruzhan Berdaly [8]