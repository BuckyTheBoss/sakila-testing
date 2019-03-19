import sqlite3
db_path = 'sakila.db'
class Customer():
	def __init__(self, customer_id=None, email=None, first_name=None, last_name=None, store_id=None, address_id=None, create_date=None, last_update=None):
		self.conn = sqlite3.connect(db_path)
		self.cursor = self.conn.cursor()
		self.customer_id = customer_id
		self.email = email
		self.first_name = first_name
		self.last_name = last_name
		self.store_id = store_id
		self.address_id = address_id
		self.create_date = create_date
		self.last_update = last_update

	def save(self):
		query = '''UPDATE customer SET store_id = ?, first_name = ?, last_name = ?, email = ?, address_id = ?, active = ?, create_date = ?, last_update = ? where customer_id = ?'''
		data = (self.store_id, self.first_name, self.last_name, self.email, self.address_id,self.active, self.create_date, self.last_update, self.customer_id)
		self.cursor.execute(query, data)
		self.cursor.commit()
		self.cursor.close()

	def search_by_email(self, email):
		query = 'select customer_id, email, first_name, last_name, store_id, address_id, create_date, last_update from customer where email like ?'
		data = (email,)
		self.cursor.execute(query, data)
		customer = self.cursor.fetchone()
		if customer != None:
			customer_object = Customer(customer[0],customer[1],customer[2],customer[3],customer[4],customer[5],customer[6],customer[7])
			return customer_object
		else:
			return None

	def get_all(self):
		query = 'select customer_id, email, first_name, last_name, store_id, address_id, create_date, last_update from customer'
		self.cursor.execute(query)
		customers = self.cursor.fetchall()
		customer_list = []
		for customer in customers:
			temp_object = Customer(customer[0],customer[1],customer[2],customer[3],customer[4],customer[5],customer[6],customer[7])
			customer_list.append(temp_object)

		return customer_list