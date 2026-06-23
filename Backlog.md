# Product Backlog – SmartRoom (SRSU)

Ten dokument zawiera listę wszystkich funkcjonalności (User Stories) oraz zadań technicznych niezbędnych do realizacji systemu rezerwacji sal.

## 📊 Status realizacji (Sprint 1-2)

| ID | User Story (Wymaganie) | Priorytet | Punkty (SP) | Status |
|:---|:---|:---:|:---:|:---:|
| **US1** | **Wyszukiwanie:** Jako użytkownik, chcę filtrować sale według pojemności, aby szybko znaleźć odpowiednie miejsce. | P0 | 3 | ✅ Gotowe |
| **US2** | **Rezerwacja:** Jako użytkownik, chcę zarezerwować salę na konkretny czas, aby mieć pewność, że termin jest zajęty dla mnie. | P0 | 5 | ✅ Gotowe |
| **US3** | **Logowanie:** Jako użytkownik, chcę logować się do systemu, aby bezpiecznie zarządzać moimi rezerwacjami. | P0 | 3 | ✅ Gotowe |
| **US4** | **Moje rezerwacje:** Jako użytkownik, chcę widzieć listę moich aktualnych rezerwacji, aby kontrolować swój grafik. | P1 | 2 | ✅ Gotowe |
| **US5** | **Powiadomienia:** Jako użytkownik, chcę otrzymywać potwierdzenie e-mail, aby mieć dowód rezerwacji. | P2 | 5 | 🔄 W toku |
| **US6** | **Zarządzanie:** Jako administrator, chcę dodawać i edytować dane sal, aby baza była zawsze aktualna. | P1 | 8 | 📅 Do zrobienia |

## 🛠️ Zadania techniczne (Technical Tasks)
- [x] Konfiguracja środowiska (Django + PostgreSQL).
- [x] Projekt bazy danych (Modele Sala i Rezerwacja).
- [x] Implementacja logiki walidacji konfliktów czasowych (brak dublowania rezerwacji).
- [ ] Konfiguracja serwera SMTP do wysyłki powiadomień e-mai.

---
**Legenda:**
- **P0** - Krytyczne, **P1** - Ważne, **P2** - Opcjonalne.
- **Story Points (SP)** - Szacowany wysiłek według skali Fibonacciego.
