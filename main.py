def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
		return file_contents

def word_count(book_to_use):
	return len(book_to_use.split())

def main():
	#print(get_book_text("books/frankenstein.txt"))
	num_words = word_count(get_book_text("books/frankenstein.txt"))
	print(f"Found {num_words} total words")

main()