import pymongo
from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Access the environment variables
MONGODB_URL = os.getenv("MONGODB_URL")

# Create function to connect to MongoDB Atlas and get a reference to the collection using pymongo lib.
def database_collection():
    client = pymongo.MongoClient(MONGODB_URL)
    db = client.tailnode  # Use your database name
    collection = db.books
    return collection
# Function to scrape and store data into MongoDB Atlas database.
def scrape_and_store_data():
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"
    collection = database_collection()
    
    for page in range(1, 51):  # Scrape all 50 pages
        url = base_url.format(page)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        print("Scraping page:", page)

        for book in soup.find_all('article', class_='product_pod'):
            img_url = book.find('img')['src']  # Extract image URL
            
            # Extract book name from different header tags
            name = None
            for header_tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                if book.find(header_tag) and book.find(header_tag).a:
                    name = book.find(header_tag).a['title']
                    break
            if not name:
                name = "Unknown"
            
            price = book.find('p', class_='price_color').text
            availability = book.find('p', class_='instock availability').text.strip()
            rating = book.find('p', class_='star-rating')['class'][1]

            # Print the scraped data attributes in the console
            print("Image URL:", img_url)
            print("Name:", name)
            print("Price:", price)
            print("Availability:", availability)
            print("Rating:", rating)
            
            # Insert data into MongoDB Atlas
            result = collection.insert_one({
                "image_url": img_url,  # Include image URL in MongoDB document
                "name": name,
                "price": price,
                "availability": availability,
                "rating": rating,
            })
            print("Inserted book:", result.inserted_id)

if __name__ == "__main__":
    scrape_and_store_data()
