# Partea 1 - Sprintul Teoretic (Multitasking in Robotica)

## 1) Concurrency si Threading
- In cod secvential, instructiunile ruleaza una dupa alta.
- In robotica, vrem actiuni in paralel: motorul merge, senzorii citesc, alarma verifica.
- `threading.Thread(...)` creeaza un fir de executie separat.
- `start()` porneste firul.
- `join()` spune programului principal sa astepte terminarea firului.

## 2) Race Condition (Bataie pe resurse)
- Race condition apare cand doua thread-uri modifica aceeasi variabila simultan.
- Exemplu: motorul scade bateria, panoul solar o creste.
- Fara sincronizare, rezultatul poate fi gresit.

## 3) Lock (Lacatul)
- `threading.Lock()` protejeaza o resursa comuna.
- `with lacat:` garanteaza ca un singur thread modifica variabila in acel moment.
- Cu lock, rezultatul devine corect si predictibil.
