class Book:
	id = 1
	book_list = []

	def __init__(self, title, author):
		self.title = author
		self.author = author
		self.id = Model.id
		Book.book_list.append(self)
		
		Book.id += 1