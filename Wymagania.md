# Specyfikacja wymagań – System SmartRoom

## 1. Wymagania funkcjonalne
| ID | Opis wymagania | Priorytet |
|----|----------------|-----------|
| F1 | Użytkownik może zalogować się do systemu. | Must |
| F2 | Użytkownik może wyszukać wolną salę według daty i godziny. | Must |
| F3 | Użytkownik może dokonać rezerwacji wybranej sali. | Must |
| F4 | Administrator może zarządzać bazą sal (dodawanie/usuwanie). | Should |

## 2. Wymagania niefunkcjonalne
* **Wydajność:** Maksymalny czas odpowiedzi systemu do 3 sekund.
* **Bezpieczeństwo:** Szyfrowanie haseł użytkowników (SHA256).
* **Dostępność:** Interfejs responsywny (RWD) działający na urządzeniach mobilnych.

## 3. Diagram przypadków użycia (UML Use Case)

```mermaid
flowchart LR

    Student[Student]
    Wykladowca[Wykładowca]
    Administrator[Administrator]

    subgraph System_SmartRoom
        UC1([Logowanie])
        UC2([Wyszukiwanie wolnych sal])
        UC3([Rezerwacja sali])
        UC4([Zarządzanie bazą sal])
    end

    Student --> UC1
    Student --> UC2
    Student --> UC3

    Wykladowca --> UC1
    Wykladowca --> UC2
    Wykladowca --> UC3

    Administrator --> UC1
    Administrator --> UC4
```