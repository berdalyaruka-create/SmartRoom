# KARTA PROJEKTU - SmartRoom

## 1. Informacje ogólne
*   **Tytuł projektu:** SmartRoom – System Rezerwacji Sal Uczelnianych
*   **Akronim projektu:** SRSU 
*   **Data utworzenia:** 22.06.2026
*   **Wersja dokumentu:** 1.0
*   **Zespół projektowy:** Aruzhan Berdaly

## 2. Cel projektu
Celem projektu SmartRoom jest opracowanie i wdrożenie webowej aplikacji do rezerwacji sal uczelnianych, umożliwiającej [2]:
*   szybkie wyszukiwanie dostępnych sal przez studentów i wykładowców,
*   rezerwowanie terminów zajęć, konsultacji lub spotkań,
*   przeglądanie kalendarza dostępności w czasie rzeczywistym,
*   otrzymywanie powiadomień e-mail o potwierdzeniu lub anulowaniu rezerwacji.

## 3. Uzasadnienie projektu
Obecny proces rezerwacji odbywa się mailowo lub telefonicznie, co prowadzi do duplikowania rezerwacji и braku przejrzystości kalendarza. System zautomatyzuje i scentralizuje ten proces.

## 4. Zakres projektu
**W zakresie projektu:**
*   Opracowanie wymagań funkcjonalnych i niefunkcjonalnych.
*   Zaprojektowanie systemu z wykorzystaniem UML.
*   Implementacja aplikacji w technologii Django + Bootstrap.
*   Utworzenie relacyjnej bazy danych (PostgreSQL).
*   Stworzenie pełnej dokumentacji technicznej.

**Poza zakresem projektu:**
*   Integracja z systemami dziekanatowymi.
*   Mobilna wersja natywna.
*   Integracja z uczelnianym LDAP-em.

## 5. Główne wymagania
| Typ | Opis |
| --- | --- |
| **Funkcjonalne** | Rezerwacja sal, logowanie, wyszukiwanie według daty i sali, powiadomienia e-mail. |
| **Niefunkcjonalne** | Czas odpowiedzi max 3 sekundy, dostępność 99%, responsywność interfejsu. |
| **Bezpieczeństwo** | Logowanie z użyciem haseł SHA256, role: użytkownik/admin. |

## 6. Zasoby i narzędzia
*   **Repozytorium:** GitHub 
*   **Programowanie:** Python (Django), HTML/CSS/Bootstrap 
*   **Baza danych:** PostgreSQL 
*   **Analiza:** Visual Paradigm, Mermaid 

## 7. Harmonogram realizacji
1.  Karta projektu i struktura zespołu (Tydzień 1).
2.  Analiza wymagań (Tydzień 2).
3.  Projekt systemu – UML (Tydzień 3–4).
4.  Implementacja prototypu (Tydzień 6–7).
5.  Testowanie i dokumentacja końcowa (Tydzień 8–10).

## 8. Kryteria sukcesu
*   Wszystkie wymagania funkcjonalne zostały zaimplementowane.
*   Dokumentacja zawiera pełny zestaw diagramów UML.
*   Aplikacja uruchamia się lokalnie i działa poprawnie.

## 9. Akceptacja projektu
*   **Prowadzący:** mgr Wojciech Moniuszko
*   **Kierownik projektu:** Aruzhan Berdaly 