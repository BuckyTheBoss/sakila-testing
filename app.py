from cust import Customer
from inventory import Inventory
from rental import Rental

def menu():
	menu_text = 'Welcome to the movie management platform!\n\n(a) Search for customer by email\n(b) Retrive all customers\n(c) Search for movie\n(d) Return movie\n(e) List all unreturned films\n(x) Exit: '
	while True:
		menu_ctrl = input(menu_text)
		customer = Customer()
		inventory = Inventory()
		rental = Rental()
		if menu_ctrl == 'a':
			searched_cust = customer.search_by_email(input("Please write the email you'd like to search for: "))
			if searched_cust == None:
				print('Sorry, we couldnt find that customer')
			else:
				print(f'Customer found!\n_______________\nFull Name: {searched_cust.first_name} {searched_cust.last_name}\nEmail: {searched_cust.email}\nStore ID: {searched_cust.store_id}\nAddress ID: {searched_cust.address_id}\nCreated: {searched_cust.create_date}\nUpdated: {searched_cust.last_update}')

		elif menu_ctrl == 'b':
			all_custs = customer.get_all()
			for cust in all_custs:
				print(f'_______________\nCustomer ID: {cust.customer_id}\nFull Name: {cust.first_name} {cust.last_name}\nEmail: {cust.email}')
		
		elif menu_ctrl == 'c':
			text = input('Please enter your search term: ')
			search_results = inventory.search_by_text(text, 1)
			for result in search_results:
				print(f'Movie details:\n______________\nInventory ID: {result.inventory_id}\nFilm ID: {result.film_id}\nFilm Title: {result.title}\nFilm Description: {result.description}\nRating: {result.rating}\nRental rate: {result.rental_rate}\n\n')


		elif menu_ctrl == 'd':
			return_film = int(input('Please enter the id for the film you are returning: '))
			rental.return_rental(return_film)
		
		elif menu_ctrl == 'e':
			film_list = rental.all_unreturned()
			for film in film_list:
				print(f"Unreturned rental details\n_________________________\nRental ID: {film.rental_id}\nRental Date: {film.rental_date}\nCustomer Name: {film.cust_name}\nCustomer Email: {film.email}\nPostal Address: {film.postal_code}\nTotal Due: ${film.compute_owed(film.rental_id)}")	
			sub_menu_ctrl = input('Please type in a rental ID to return or press (x) to return to main menu')
			if sub_menu_ctrl != 'x':
				#write better logic to validate input
				if input('Are you certain? Y/N: ') == 'Y':
					rental.return_rental(int(sub_menu_ctrl))
					print('Returned successfully\n\n')

		elif menu_ctrl == 'x':
			break

menu()