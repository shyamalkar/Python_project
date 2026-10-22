import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import re


# Function to web page 

def fetch_webpage(url):
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.text


# Function to extract to details 

def extract_product_details(url):

    html = fetch_webpage(url)

    soup = BeautifulSoup(html, "html.parser")

    # Product title
    title_tag = soup.find("h1")

    if title_tag:
        title = title_tag.get_text(strip=True)
    else:
        title = "Title not found"

    # Product price
    price = None

    # Try common price elements
    price_selectors = [
        ".price",
        ".product-price",
        ".sale-price",
        "[itemprop='price']"
    ]

    for selector in price_selectors:

        price_tag = soup.select_one(selector)

        if price_tag:

            price_text = price_tag.get_text(" ", strip=True)

            # Extract numeric value
            match = re.search(r"[\d,]+(?:\.\d+)?", price_text)

            if match:
                price = float(match.group().replace(",", ""))
                break

    # Product image
    image_tag = soup.find("img")

    if image_tag and image_tag.get("src"):

        image_url = urljoin(url, image_tag["src"])

    else:

        image_url = None

    return {
        "title": title,
        "price": price,
        "image_url": image_url
    }


# Function to download product image 

def download_image(image_url, product_number):

    if not image_url:
        print("Image URL not found.")
        return None

    os.makedirs("product_images", exist_ok=True)

    image_path = f"product_images/product_{product_number}.jpg"

    response = requests.get(
        image_url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )

    response.raise_for_status()

    with open(image_path, "wb") as file:
        file.write(response.content)

    return image_path


# Function to compare price 

def compare_price(current_price, target_price):

    if current_price is None:
        return "Price not found"

    if current_price < target_price:

        return "Price is below target price"

    elif current_price == target_price:

        return "Target price reached"

    else:

        return "Price is above target price"



# Main programm

products = [

    {
        "url": "https://www.flipkart.com/item/p/product?pid=TABG6VNCJCNHYMPD&marketplace=FLIPKART&pageUID=1791429019135",
        "target_price": 1000
    },

    {
        "url": "https://www.apple.com/in/iphone/?cid=wwa-in-kwgo-iphone-noncore_iphonefamily-iphonefamily_compare-iphone_compare_avail_091826-iPhone_Compare-iPhone_Compare_Models&aosid=p240&ken_pid=go~cmp-14651195662~adg-201542590473~ad-826433222598_kwd-2183510789010~dev-c~ext-~prd-~mca-~nt-search&token=f8ed3188-10e0-4de1-9527-7c1db3c81d53",
        "target_price": 2000
    }

]


for product_number, product in enumerate(products, start=1):

    print("\n" + "=" * 60)

    print(f"PRODUCT {product_number}")

    print("=" * 60)

    try:

        details = extract_product_details(product["url"])

        print(f"Title       : {details['title']}")
        print(f"Price       : {details['price']}")
        print(f"Image URL   : {details['image_url']}")

        # Download image
        image_path = download_image(
            details["image_url"],
            product_number
        )

        print(f"Image saved : {image_path}")

        # Compare price
        result = compare_price(
            details["price"],
            product["target_price"]
        )

        print(f"Target Price: {product['target_price']}")
        print(f"Result      : {result}")

    except requests.exceptions.RequestException as error:

        print(f"Request error: {error}")

    except Exception as error:

        print(f"Error: {error}")





