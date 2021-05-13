# Przed pierwszym uruchomieniem:
    pip install -r requirements.txt
należy wykonać z poziomu wyżej (korzenia drzewa plików paczki).



# Zadania 1 i 2:
Aby uruchomić kod trzeba podać flagę oraz scieżkę do pliku, np:

    python zad1_2.py ./nazwa_pliku (degreeSeq_zad1.txt)
    
# Zadanie 3
    python zad3.py --am ./nazwa_pliku
    --am -  macierz sąsiedztwa(musi sprawdzać założenia dla macierzy sąsiedztwa) (macierz_zad3.txt)
    --al -  lista sąsiedztwa (listaA.txt)
    --im -  macierz incydencji (macierzI.txt)

# Zadanie 4
    python zad4.py [n] [start]    np. python zad4.py 5 2  
    [n] - liczba wierzcholkow grafu
    [start] - numer wierzcholka z ktorego chcemy rozpoczac

# Zadanie 5
    python zad5.py [n] [k]    np. python zad5.py 7 2 
    n[int] - liczba wierzchołków grafy k-regularnego
    k[int] - stopień każdego z wierzchołków

# Zadanie 6
    python zad6.py ./nazwa_pliku (macierz sąsiedztwa, np. macierz_yes_ham_zad6.txt)
