# Projektowanie systemu – SmartRoom

Dokumentacja techniczna zawierająca diagramy UML, które opisują strukturę danych oraz logikę działania systemu rezerwacji sal.

## 1. Diagram Klas (Class Diagram)
Diagram przedstawia strukturę bazy danych PostgreSQL oraz relacje między obiektami. Na jego podstawie zostaną stworzone modele w technologii Django.

```mermaid
classDiagram
    class Uzytkownik {
        +int id
        +string login
        +string email
        +string haslo
        +string rola
        +zaloguj()
    }
    class Sala {
        +int id
        +string numer
        +int pojemnosc
        +string wyposazenie
        +sprawdzDostepnosc()
    }
    class Rezerwacja {
        +int id
        +date data
        +time godzina_start
        +time godzina_koniec
        +string status
        +utworz()
        +anuluj()
    }

    Uzytkownik "1" -- "*" Rezerwacja : dokonuje
    Sala "1" -- "*" Rezerwacja : jest przedmiotem
2. Diagram Sekwencji (Sequence Diagram)
Przedstawia proces interakcji studenta z systemem podczas wyszukiwania и rezerwacji sali w czasie rzeczywistym
.
sequenceDiagram
    participant Student
    participant System
    participant BazaDanych

    Student->>System: Wyszukaj wolną salę (data, godzina)
    System->>BazaDanych: Zapytanie o dostępne sale
    BazaDanych-->>System: Lista dostępnych rekordów
    System-->>Student: Wyświetlenie wyników wyszukiwania
    Student->>System: Wybór sali i kliknięcie "Rezerwuj"
    System->>BazaDanych: Zapisanie nowej rezerwacji
    BazaDanych-->>System: Potwierdzenie zapisu
    System-->>Student: Komunikat: "Rezerwacja zakończona sukcesem"
3. Diagram Aktywności (Activity Diagram)
Opisuje logikę biznesową procesu rezerwacji, uwzględniając scenariusze alternatywne (np. brak wolnych sal)
.
graph TD
    A[Start: Chęć dokonania rezerwacji] --> B[Wprowadzenie daty i godziny]
    B --> C{Czy są wolne sale?}
    C -- Nie --> D[Komunikat o braku dostępnych miejsc]
    D --> B
    C -- Tak --> E[Wybór sali z listy]
    E --> F[Zatwierdzenie rezerwacji]
    F --> G[Zapisanie danych w systemie]
    G --> H[Wysłanie potwierdzenia e-mail]
    H --> I[Koniec procesu]
