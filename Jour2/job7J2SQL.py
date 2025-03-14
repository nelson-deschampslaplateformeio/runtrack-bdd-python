import mysql.connector

class Employe:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Jaberwock10243@",  
            database="entreprise"
        )
        self.cursor = self.conn.cursor()

    def ajouter_employe(self, nom, prenom, salaire, id_service):
        sql = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (nom, prenom, salaire, id_service))
        self.conn.commit()
        print("Employé ajouté avec succès.")

    def afficher_employes(self):
        self.cursor.execute("SELECT * FROM employe")
        employes = self.cursor.fetchall()
        for emp in employes:
            print(emp)

    def modifier_salaire(self, employe_id, nouveau_salaire):
        sql = "UPDATE employe SET salaire = %s WHERE id = %s"
        self.cursor.execute(sql, (nouveau_salaire, employe_id))
        self.conn.commit()
        print("Salaire mis à jour.")

    def supprimer_employe(self, employe_id):
        sql = "DELETE FROM employe WHERE id = %s"
        self.cursor.execute(sql, (employe_id,))
        self.conn.commit()
        print("Employé supprimé.")

    def fermer_connexion(self):
        self.cursor.close()
        self.conn.close()

# Test de la classe
if __name__ == "__main__":
    employe_manager = Employe()
    
    # Ajouter un employé
    employe_manager.ajouter_employe("Test", "User", 3500.00, 1)
    
    # Afficher tous les employés
    print("\nListe des employés :")
    employe_manager.afficher_employes()
    
    # Modifier un salaire
    employe_manager.modifier_salaire(1, 3800.00)

    # Supprimer un employé
    employe_manager.supprimer_employe(1)

    # Fermer la connexion
    employe_manager.fermer_connexion()
