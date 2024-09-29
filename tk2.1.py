import requests
from bs4 import BeautifulSoup
import sqlite3
import sys


def extract_text_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: Failed to connect to the URL. Please check your internet connection or URL.")
        return None
    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again later.")
        return None
    except requests.exceptions.RequestException as req_err:
        print(f"Error: An error occurred while fetching the page: {req_err}")
        return None

    try:
        soup = BeautifulSoup(response.content, 'html.parser')
        page_text = soup.get_text(separator=' ', strip=True)
        return page_text
    except Exception as parse_err:
        print(f"Error while parsing the page: {parse_err}")
        return None



def save_text_to_database(url, text):
    try:
        conn = sqlite3.connect('web_texts.db')
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS web_content (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            content TEXT NOT NULL
        )
        ''')
        cursor.execute('''
        INSERT INTO web_content (url, content)
        VALUES (?, ?)
        ''', (url, text))        
        conn.commit()
        conn.close()
    except sqlite3.Error as db_err:
        print(f"Database error occurred: {db_err}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred while saving to the database: {e}")
        return False
    return True



def show_database_content():
    try:
        conn = sqlite3.connect('web_texts.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM web_content')
        rows = cursor.fetchall()
        if not rows:
            print("No data found in the database.")
            return
        for row in rows:
            print(f"ID: {row[0]}")
            print(f"URL: {row[1]}")
            print(f"Content:\n{row[2]}")
            print("\n" + "-"*80 + "\n")
        conn.close()
    except sqlite3.Error as db_err:
        print(f"Database error occurred while retrieving data: {db_err}")
    except Exception as e:
        print(f"An unexpected error occurred while showing the database content: {e}")



def main():
    try:
        url = input("Enter the URL of the webpage to scrape: ")        
        extracted_text = extract_text_from_url(url)
        if extracted_text:
            if save_text_to_database(url, extracted_text):
                print("Web page content saved successfully!")
                show_data = input("Would you like to see the content stored in the database? (y/n): ").strip().lower()
                if show_data == 'y':
                    show_database_content()
            else:
                print("Failed to save the content to the database.")
        else:
            print("Failed to extract or save the content.")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting.")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
