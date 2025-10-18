# My First Web Crawler: Book Title Scraper

This is my first web crawler project, built as a guided lesson. The script fetches the main page of `books.toscrape.com` and extracts the title of every book listed.

## What it does

The crawler performs three main tasks:

1.  Fetches the HTML content from `https://books.toscrape.com/`.
2.  Parses the HTML to find the title of every book on the front page.
3.  Saves these titles into a clean `.csv` file named `book_titles.csv`.

## Technologies Used

* **Python 3**
* **Requests** (for making HTTP requests to get the webpage)
* **BeautifulSoup4** (for parsing the HTML and finding elements)

## How to Run This Project

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
    cd YOUR_REPOSITORY_NAME
    ```

2.  **Install the required libraries:**
    ```bash
    pip install requests beautifulsoup4
    ```

3.  **Run the script:**
    ```bash
    python your_script_name.py
    ```

4.  **Check the output:**
    A file named `book_titles.csv` will be created in the same folder, containing all the book titles.