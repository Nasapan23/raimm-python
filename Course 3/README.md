# Crash Course Python (102) - RAIMM

Acest folder contine rezolvari complete pentru **Course 3**, pe baza ghidului:
- threading/concurrency
- race condition + lock
- OOP cu fire de executie
- exercitii de laborator (nivel 1/2/3)
- 10 provocari finale de robotica

## Structura
- `teorie_multitasking.md` - recapitulare teoretica scurta
- `exemplul_1_threads_baza.py` - robotul merge si citeste senzori simultan
- `exemplul_2_oop_baterie_lock.py` - baterie + lock in OOP
- `recap_*` - recapitulare 101 + 102
- `problema_1_...` pana la `problema_10_...` - setul SOLO Work

## Rulare
Din radacina proiectului:

```bash
python "Course 3/exemplul_1_threads_baza.py"
python "Course 3/problema_4_dezastrul_bateriei_race_condition.py"
python "Course 3/problema_10_robot_os.py"
```

Fisierele care cer comenzi din tastatura:
- `recap_nivel_2_robot_comenzi.py` (scrie `stop`)
- `problema_6_robotul_ascultator.py` (scrie `STOP`)
- `problema_10_robot_os.py` (scrie `oprire`)
