class Creator:
    def __init__(self, nume): # Constructor pentru clasa Creator
        self.nume = nume # Numele creatorului
        self.foame = 0 # Nivelul de foame al creatorului
        self.views = 10 # Numarul initial de views al creatorului

    def posteaza(self): # Metoda pentru a posta un clip normal
        self.views += 3 # Creste numarul de views cu 3
        self.foame += 2 # Creste nivelul de foame cu 2
        print("Am postat un clip normal!") 


class StreamerNPC(Creator): # Clasa StreamerNPC mosteneste de la Creator
    def __init__(self, nume, replica): # Constructor pentru clasa StreamerNPC
        super().__init__(nume)# Apeleaza constructorul clasei parinte pentru a initializa numele, foamea si views
        self.replica = replica # Replica specifica pentru acest NPC

    def face_live(self): # Metoda pentru a face un live
        self.views += 20 # Creste numarul de views cu 20
        self.foame += 5 # Creste nivelul de foame cu 5
        print(f"Trandafiri, trandafiri! {self.replica}")

    # Extra: Metoda de a adauga vizualizari suplimentare
    def adauga_views(self, numar_views):
        self.views += numar_views # Adauga numarul specificat de views la total
        print(f"Mersi de promovare sefuleee, au intrat {numar_views} oameni in plus!")


npc1 = StreamerNPC("Pinky", "Mmmm, inghetata!")

npc1.posteaza()
npc1.face_live()

#Aditional
npc1.adauga_views(50)

print(f"{npc1.nume} are acum {npc1.views} views si foame {npc1.foame}.")
