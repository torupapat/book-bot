def words_count(content):
    words_list = content.split()
    count = len(words_list)
    return count

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)
        print(words_count(file_contents))

main()