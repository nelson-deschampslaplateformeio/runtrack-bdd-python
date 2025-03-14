import mysql.connector

# Connexion à la base de données
try:
    conn = mysql.connector.connect(
        host="localhost", 
        user="root",      
        password="Jaberwock10243@",
        database="LaPlateforme"  
    )

    cursor = conn.cursor()

   
    cursor.execute("SELECT * FROM etudiant")

   
    resultats = cursor.fetchall()

   
    print("Liste des étudiants :")
    for etudiant in resultats:
        print(etudiant)

except mysql.connector.Error as err:
    print(f"Erreur : {err}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
