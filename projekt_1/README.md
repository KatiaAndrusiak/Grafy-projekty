# Przed pierwszym uruchomieniem:
	pip install -r requirements.txt
należy wykonać z poziomu wyżej (korzenia drzewa plików paczki).

# Aby uruchomić kod trzeba podać flagę oraz scieżkę do pliku, np:

# Zadanie 1
    python zad1-2.py --am ./nazwa_pliku
    --am -  macierz sąsiedztwa(musi sprawdzać założenia dla macierzy sąsiedztwa) (macierzA.txt)
    --al -  lista sąsiedztwa (listaA.txt)
    --im -  macierz incydencji (macierzI.txt)  
    --help - flaga pomocnicza

# Zadanie 3
    python zad3.py --gnl {n} {l}  przyklad python zad3.py --gnl 5 3
		   --gnp {n} {p}  przyklad python zad3.py --gnp 5 0.3
    n [int] - liczba wierzcholkow
    l [int] - liczba krawedzi do wygenerowania
    p [float] - prawdopodobienstwo wygenerowania krawedzi pomiedzy dwoma wierzcholkami
    --help - flaga pomocnicza
