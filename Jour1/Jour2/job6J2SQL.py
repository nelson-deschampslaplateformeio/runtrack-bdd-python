import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jaberwock10243@", 
    database="LaPlateforme"
)

cursor = conn.cursor()

# Exécuter la requête SQL
cursor.execute("SELECT SUM(capacite) FROM salle")

# Récupérer le résultat
capacite_totale = cursor.fetchone()[0]

# Afficher le résultat formaté
print(f"La capacité de toutes les salles est de : {capacite_totale}")

# Fermer la connexion
cursor.close()
conn.close()
