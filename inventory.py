import sqlite3
db_path = 'sakila.db'

class Inventory():
	def __init__(self, inventory_id= None, film_id= None, store_id= None, last_update= None, title = None, description = None, rating=None, rental_rate=None):
		self.inventory_id = inventory_id
		self.film_id = film_id
		self.store_id = store_id
		self.last_update = last_update
		self.conn = sqlite3.connect(db_path)
		self.cursor = self.conn.cursor()
		self.title = title
		self.description = description
		self.rating = rating
		self.rental_rate = rental_rate

	def search_by_text(self,text,store_id):
		text = '%{}%'.format(text)
		query = '''SELECT * from inventory
			JOIN (SELECT film_id, description, title, rating, rental_rate from film) as film_table
			on inventory.film_id = film_table.film_id
			WHERE (film_table.description LIKE ? OR film_table.title LIKE ?) AND store_id = ?'''
		data = (text, text, store_id)
		self.cursor.execute(query, data)
		film_rows = self.cursor.fetchall()
		film_results = []
		for film in film_rows:
			print(film[0:len(film)])
			temp_film = Inventory(film[0],film[1],film[2],film[3],film[6],film[5],film[7],film[8])
			film_results.append(temp_film)

		return film_results


