def get_num_words(book_to_use):
	return len(book_to_use.split())

def get_char_count(string_to_count):
	char_dict = {}
	for char in string_to_count.lower():
		