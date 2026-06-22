useCaseDiagram
    actor Student
    actor Wykładowca
    actor Administrator

    package "System SmartRoom" {
        usecase "Logowanie" as UC1
        usecase "Wyszukiwanie wolnych sal" as UC2
        usecase "Rezerwacja sali" as UC3
        usecase "Przeglądanie kalendarza" as UC4
        usecase "Zarządzanie bazą sal" as UC5
        usecase "Zarządzanie użytkownikami" as UC6
    }

    Student --> UC1
    Student --> UC2
    Student --> UC3
    Student --> UC4

    Wykładowca --> UC1
    Wykładowca --> UC2
    Wykładowca --> UC3
    Wykładowca --> UC4

    Administrator --> UC1
    Administrator --> UC5
    Administrator --> UC6

    UC3 ..> UC1 : <<include>>