import sys

from searchers.base_searcher import Searcher

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Run: python script.py <query>\n'
              '\twhere <query> is a search query\n'
              '\ti.q. python script.py Meal for')
        sys.exit(0)
    query = ' '.join(sys.argv[1:])
    books = Searcher.search(query)
    for book in books:
        print('{}\t{}'.format(book.id, book.title))
