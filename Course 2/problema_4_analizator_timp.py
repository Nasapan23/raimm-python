minute = int(input("Introdu numarul de minute: "))

ore = minute // 60
minute_ramase = minute % 60

print(f"{minute} minute inseamna {ore} ore si {minute_ramase} minute.")
