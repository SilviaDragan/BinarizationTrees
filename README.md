# MPS-Proiect

## Rulare:
### Binarizare globala:
python3 run_final.py -> va popula fisierul winners/winners din directorul global_binarization cu top 3 
cei mai buni arbori gasiti in urma rularii pe fisierele de training.

### Binarizarea locala:
Pentru binarizarea locala se alege cel mai bun tree din fiecare fisier. Pentru fiecare pixel se genereaza un tree, acestia sunt sortati dupa functia de evaluare si se salveaza cel mai bun.
Rularea locala se face automat dupa cea globala in fisierul run_training_tests.py
