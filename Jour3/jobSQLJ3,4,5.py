import mysql.connector
import tkinter as tk
from tkinter import messagebox
import csv
from database import connect_db
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jaberwock10243@",
        database="store"
    )


class StockManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de Stock")

        # Labels et Entrées
        tk.Label(root, text="Nom du produit:").grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        tk.Label(root, text="Description:").grid(row=1, column=0)
        self.desc_entry = tk.Entry(root)
        self.desc_entry.grid(row=1, column=1)

        tk.Label(root, text="Prix:").grid(row=2, column=0)
        self.price_entry = tk.Entry(root)
        self.price_entry.grid(row=2, column=1)

        tk.Label(root, text="Quantité:").grid(row=3, column=0)
        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.grid(row=3, column=1)

        tk.Label(root, text="Catégorie ID:").grid(row=4, column=0)
        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=4, column=1)

        # Boutons
        tk.Button(root, text="Ajouter", command=self.add_product).grid(row=5, column=0)
        tk.Button(root, text="Modifier", command=self.update_product).grid(row=5, column=1)
        tk.Button(root, text="Supprimer", command=self.delete_product).grid(row=6, column=0)
        tk.Button(root, text="Exporter CSV", command=self.export_csv).grid(row=6, column=1)

        # Zone d'affichage
        self.result_label = tk.Label(root, text="", fg="blue")
        self.result_label.grid(row=7, column=0, columnspan=2)

        self.load_products()

    def load_products(self):
        """Charge et affiche la liste des produits"""
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, price, quantity FROM product")
        products = cursor.fetchall()
        conn.close()

        display_text = "\n".join([f"{p[0]} - {p[1]} | {p[2]}€ | {p[3]} en stock" for p in products])
        self.result_label.config(text=display_text)

    def add_product(self):
        """Ajoute un produit à la base de données"""
        name = self.name_entry.get()
        desc = self.desc_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()
        category = self.category_entry.get()

        if not all([name, desc, price, quantity, category]):
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
            return

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)",
                       (name, desc, price, quantity, category))
        conn.commit()
        conn.close()

        messagebox.showinfo("Succès", "Produit ajouté avec succès.")
        self.load_products()

    def update_product(self):
        """Modifie un produit"""
        product_id = self.name_entry.get()
        new_price = self.price_entry.get()
        new_quantity = self.quantity_entry.get()

        if not all([product_id, new_price, new_quantity]):
            messagebox.showerror("Erreur", "ID, prix et quantité doivent être remplis.")
            return

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE product SET price=%s, quantity=%s WHERE id=%s",
                       (new_price, new_quantity, product_id))
        conn.commit()
        conn.close()

        messagebox.showinfo("Succès", "Produit mis à jour.")
        self.load_products()

    def delete_product(self):
        """Supprime un produit"""
        product_id = self.name_entry.get()

        if not product_id:
            messagebox.showerror("Erreur", "Veuillez entrer l'ID du produit à supprimer.")
            return

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM product WHERE id=%s", (product_id,))
        conn.commit()
        conn.close()

        messagebox.showinfo("Succès", "Produit supprimé.")
        self.load_products()

    def export_csv(self):
        """Exporte les produits en fichier CSV"""
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM product")
        products = cursor.fetchall()
        conn.close()

        with open("stocks.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nom", "Description", "Prix", "Quantité", "ID Catégorie"])
            writer.writerows(products)

        messagebox.showinfo("Succès", "Exportation terminée.")

if __name__ == "__main__":
    root = tk.Tk()
    app = StockManager(root)
    root.mainloop()
