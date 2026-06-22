# User Stories – System SmartRoom

Poniżej znajdują się historie użytkowników opisujące kluczowe funkcjonalności systemu SmartRoom z perspektywy różnych ról.

## 1. Lista User Stories

| ID | Jako... (Rola) | Chcę... (Akcja) | Aby... (Korzyść) |
|----|----------------|-----------------|------------------|
| US1 | Student | Wyszukać wolną salę po dacie i godzinie | Szybko znaleźć miejsce do nauki lub pracy grupowej. |
| US2 | Student | Dokonać natychmiastowej rezerwacji online | Mieć pewność, że wybrana sala będzie dla mnie dostępna. |
| US3 | Wykładowca | Rezerwować sale na dodatkowe konsultacje | Umożliwić studentom spotkanie w wyznaczonym miejscu i czasie. |
| US4 | Administrator | Zarządzać bazą sal (dodawać i usuwać obiekty) | System zawsze zawierał aktualne informacje o dostępnych zasobach. |
| US5 | Użytkownik | Zresetować zapomniane hasło przez e-mail | Odzyskać dostęp do swojego konta bez pomocy administratora. |

## 2. Kryteria Akceptacji (Acceptance Criteria)

Zgodnie ze standardem INVEST, każda historia posiada jasne kryteria określające, kiedy zadanie uznaje się za gotowe.

### Przykład dla US2: Rezerwacja sali
**Scenario:** Poprawna rezerwacja sali przez studenta
* **Given:** Student jest zalogowany do systemu i wybrał dostępną salę.
* **When:** Student klika przycisk "Rezerwuj" i potwierdza wybór.
* **Then:** System zapisuje rezerwację w bazie danych.
* **And:** Student widzi komunikat: "Rezerwacja zakończona sukcesem".
* **And:** Sala zmienia status na "Zajęta" w wybranym przedziale czasowym.

### Przykład dla US5: Reset hasła
**Scenario:** Odzyskiwanie dostępu do konta
* **Given:** Użytkownik znajduje się na stronie logowania.
* **When:** Wpisuje swój adres e-mail в formularzu "Zapomniałem hasła".
* **Then:** System wysyła link aktywacyjny na podany adres e-mail.