import mysql.connector

class ZooManager:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Jaberwock10243@",
            database="zoo"
        )
        self.cursor = self.conn.cursor()

    

    def ajouter_cage(self, superficie, capacite_max):
        sql = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
        self.cursor.execute(sql, (superficie, capacite_max))
        self.conn.commit()
        print("Cage ajoutée avec succès.")

    def supprimer_cage(self, cage_id):
        sql = "DELETE FROM cage WHERE id = %s"
        self.cursor.execute(sql, (cage_id,))
        self.conn.commit()
        print("Cage supprimée.")

    def afficher_cages(self):
        self.cursor.execute("SELECT * FROM cage")
        cages = self.cursor.fetchall()
        print("\nListe des cages :")
        for cage in cages:
            print(cage)

   

    def ajouter_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        sql = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (nom, race, id_cage, date_naissance, pays_origine))
        self.conn.commit()
        print("Animal ajouté avec succès.")

    def supprimer_animal(self, animal_id):
        sql = "DELETE FROM animal WHERE id = %s"
        self.cursor.execute(sql, (animal_id,))
        self.conn.commit()
        print("Animal supprimé.")

    def modifier_animal(self, animal_id, nouveau_nom, nouvelle_cage):
        sql = "UPDATE animal SET nom = %s, id_cage = %s WHERE id = %s"
        self.cursor.execute(sql, (nouveau_nom, nouvelle_cage, animal_id))
        self.conn.commit()
        print("Animal mis à jour.")

    def afficher_animaux(self):
        self.cursor.execute("SELECT * FROM animal")
        animaux = self.cursor.fetchall()
        print("\nListe des animaux :")
        for animal in animaux:
            print(animal)

    def afficher_animaux_par_cage(self):
        sql = """
        SELECT a.nom, a.race, c.id AS cage_id 
        FROM animal a
        LEFT JOIN cage c ON a.id_cage = c.id
        ORDER BY c.id
        """
        self.cursor.execute(sql)
        animaux = self.cursor.fetchall()
        print("\nAnimaux par cage :")
        for animal in animaux:
            print(animal)

    def calculer_superficie_totale(self):
        sql = "SELECT SUM(superficie) FROM cage"
        self.cursor.execute(sql)
        superficie_totale = self.cursor.fetchone()[0]
        print(f"\nSuperficie totale des cages : {superficie_totale} m²")

    def fermer_connexion(self):
        self.cursor.close()
        self.conn.close()
    
    def menu():
        zoo_manager = ZooManager()
    
        while True:
            print("\nMenu Gestion du Zoo")
            print("1️⃣ Ajouter une cage")
            print("2️⃣ Supprimer une cage")
            print("3️⃣ Afficher toutes les cages")
            print("4️⃣ Ajouter un animal")
            print("5️⃣ Supprimer un animal")
            print("6️⃣ Modifier un animal")
            print("7️⃣ Afficher tous les animaux")
            print("8️⃣ Afficher les animaux par cage")
            print("9️⃣ Calculer la superficie totale des cages")
            print("0️⃣ Quitter")

            choix = input("👉 Choisissez une option : ")

            if choix == "1":
                superficie = float(input("Superficie de la cage : "))
                capacite = int(input("Capacité maximale : "))
                zoo_manager.ajouter_cage(superficie, capacite)

            elif choix == "2":
                cage_id = int(input("ID de la cage à supprimer : "))
                zoo_manager.supprimer_cage(cage_id)

            elif choix == "3":
                zoo_manager.afficher_cages()

            elif choix == "4":
                nom = input("Nom de l'animal : ")
                race = input("Race de l'animal : ")
                id_cage = int(input("ID de la cage : "))
                date_naissance = input("Date de naissance (AAAA-MM-JJ) : ")
                pays_origine = input("Pays d'origine : ")
                zoo_manager.ajouter_animal(nom, race, id_cage, date_naissance, pays_origine)

            elif choix == "5":
                animal_id = int(input("ID de l'animal à supprimer : "))
                zoo_manager.supprimer_animal(animal_id)

            elif choix == "6":
                animal_id = int(input("ID de l'animal à modifier : "))
                nouveau_nom = input("Nouveau nom : ")
                nouvelle_cage = int(input("Nouvelle cage : "))
                zoo_manager.modifier_animal(animal_id, nouveau_nom, nouvelle_cage)

            elif choix == "7":
                zoo_manager.afficher_animaux()

            elif choix == "8":
                zoo_manager.afficher_animaux_par_cage()

            elif choix == "9":
                zoo_manager.calculer_superficie_totale()

            elif choix == "0":
                zoo_manager.fermer_connexion()
                print("Au revoir !")
                break

            else:
                print("Option invalide, essayez à nouveau.")

    if __name__ == "__main__":
        menu()
