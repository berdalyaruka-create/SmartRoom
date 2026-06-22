# Specyfikacja wymagań – System SmartRoom

## 1. Wymagania funkcjonalne
| ID | Opis wymagania | Priorytet |
|----|----------------|-----------|
| F1 | Użytkownik może zalogować się do systemu. | Must [13] |
| F2 | Użytkownik może wyszukać wolną salę według daty i godziny. | Must [13] |
| F3 | Użytkownik może dokonać rezerwacji wybranej sali. | Must [13] |
| F4 | Administrator może zarządzać bazą sal (dodawanie/usuwanie). | Should [13] |

## 2. Wymagania niefunkcjonalne
* **Wydajność:** Maksymalny czas odpowiedzi systemu do 3 sekund [14], [15].
* **Bezpieczeństwo:** Szyfrowanie haseł użytkowników (SHA256) [14], [15].
* **Dostępność:** Interfejs responsywny (RWD) działający na urządzeniach mobilnych [16].

## 3. Diagram przypadków użycia (UML Use Case)

```mermaid
useCaseDiagram
    actor Student
    actor Wykładowca
    actor Administrator

    package "System SmartRoom" {
        usecase "Logowanie" as UC1
        usecase "Wyszukiwanie wolnych sal" as UC2
        usecase "Rezerwacja sali" as UC3
        usecase "Zarządzanie bazą sal" as UC4
    }

    Student --> UC1
    Student --> UC2
    Student --> UC3
    
    Wykładowca --> UC1
    Wykładowca --> UC2
    Wykładowca --> UC3
    
    Administrator --> UC1
    Administrator --> UC4
