import requests
import bs4

# URL without page number
base_url = "http://books.toscrape.com/catalogue/page-{}.html"

# 4 - 5 rating books list
high_r_books = []

# Page iteration
for page in range(1, 51):

    # Create soup for every page
    page_url = base_url.format(page)
    result = requests.get(page_url)
    soup = bs4.BeautifulSoup(result.text, "lxml")

    # Select book data
    books = soup.select(".product_pod")

    # Book iteration
    for book in books:

        # Check 4-5 Star rating
        if len(book.select(".star-rating.Four")) != 0 or len(book.select(".star-rating.Five")) != 0:

            # Save title
            book_title = book.select("a")[1]["title"]

            # Append book to list
            high_r_books.append(book_title)

# Show 4-5 star rating books
for b in high_r_books:
    print(b)
