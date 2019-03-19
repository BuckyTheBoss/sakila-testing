import sqlite3
import datetime as DT

db_path = 'sakila.db'

class Rental():
	def __init__(self, rental_id=None, rental_date=None, inventory_id=None, customer_id=None, return_date=None, staff_id=None, last_update=None, cust_name=None, email=None, postal_code=None):
		self.conn = sqlite3.connect(db_path)
		self.cursor = self.conn.cursor()
		self.conn.row_factory = sqlite3.Row

		self.rental_id = rental_id
		self.rental_date = rental_date
		self.inventory_id = inventory_id
		self.customer_id = customer_id
		self.return_date = return_date
		self.staff_id = staff_id
		self.last_update = last_update
		self.cust_name = cust_name
		self.email = email
		self.postal_code = postal_code

	def return_rental(self, rental_id):
		query = 'UPDATE rental SET return_date = datetime() WHERE rental_id = ?'
		self.cursor.execute(query, (rental_id,))
		self.conn.commit()
		self.conn.close()

	def all_unreturned(self):
		query = 'select * from rental join customer on rental.customer_id = customer.customer_id join address on customer.address_id = address.address_id where return_date is NULL'
		self.cursor.execute(query)
		results = self.cursor.fetchall()
		film_list = []
		for result in results:
			temp_object = Rental(result[0],result[1], result[2],result[3], result[4],result[5],result[6],result[9] + ' ' + result[10], result[11],result[21])
			film_list.append(temp_object)
		return film_list

	def compute_owed(self, rental_id):
		query = '''select rental.rental_id, film.rental_duration, film.rental_rate, 
		rental.rental_date from rental join inventory on rental.inventory_id = inventory.inventory_id 
		join film on film.film_id = inventory.film_id where rental_id = ?'''
		self.cursor.execute(query,(rental_id,))
		result = self.cursor.fetchone()		
		rental_time = DT.datetime.strptime(result[3],'%Y-%m-%d %H:%M:%S.%f')
		days = DT.datetime.now() - rental_time
		return (days.days / result[1] * result[2])

	# join film to rental to inventory where rental_id = rental_id
	# check day diff between rental date and current date
	# divide output of previous line by rental duration 
	# multiply by rental_cost