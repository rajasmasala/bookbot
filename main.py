from stats import get_num_words, get_char_nums, sorted_char_stats
import sys

def get_book_text(book_path):
	with open(book_path) as f:
		return f.read()



def main():
	if len (sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	book_string = get_book_text(sys.argv[1])
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}...")
	print("----------- Word Count ----------")
	print(f"Found {get_num_words(book_string)} total words")
	print("--------- Character Count -------")
	sorted_dict = sorted_char_stats(get_char_nums(book_string))
	for item in sorted_dict:
		print(f"{item["char"]}: {item["num"]}")
	
	print("============= END ===============")
	return

main()
