import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jaberwock10243@", 
    database="LaPlateforme"
)

cursor = conn.cursor()

# Exécuter la requête pour récupérer les noms et capacités des salles
cursor.execute("SELECT nom, capacite FROM salle")

# Récupérer tous les résultats
resultats = cursor.fetchall()

# Affichage du résultat
print(resultats)

# Fermer la connexion
cursor.close()
conn.close()
