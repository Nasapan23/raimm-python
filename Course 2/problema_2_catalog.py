note_elev = {
    "Matematica": 8,
    "Romana": 9,
    "Fizica": 7,
}

print(f"Nota la Romana este: {note_elev['Romana']}")

note_elev["Matematica"] = 10
note_elev["Istorie"] = 9

print("Catalog final:")
print(note_elev)

# Extra
media_generala = sum(note_elev.values()) / len(note_elev)
print(f"Media generala este: {media_generala}")
