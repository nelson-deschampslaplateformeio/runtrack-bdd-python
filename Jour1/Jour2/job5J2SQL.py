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
cursor.execute("SELECT SUM(superficie) FROM etage")

# Récupérer le résultat
superficie_totale = cursor.fetchone()[0]

# Afficher le résultat formaté
print(f"La superficie de La Plateforme est de {superficie_totale} m2")

# Fermer la connexion
cursor.close()
conn.close()
