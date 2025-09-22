# We import necessary packages 
#
import requests # requests is the package needed to handle web queries
import os # this package is necessary for OS actions management
from urllib.parse import urlparse
import hashlib

# We define a function that take url links as input parameters
def download_image(url, folder="Fetched_Images"):
    # Create folder to store images if not exists
    os.makedirs(folder, exist_ok=True)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check HTTP errors

        # Check Content-Type header to ensure it's an image
        content_type = response.headers.get('Content-Type', '')
        if not content_type.startswith('image/'):
            print(f"✗ URL does not point to an image. Content-Type: {content_type}")
            return False

        # Extract or generate filename
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:
            # Generate filename from hash of URL
            hashed_name = hashlib.md5(url.encode('utf-8')).hexdigest()
            filename = f"{hashed_name}.jpg"
        
        # Avoid duplicates by checking existing files (based on filename)
        filepath = os.path.join(folder, filename)
        if os.path.exists(filepath):
            print(f"✓ Image already downloaded: {filename}")
            return True

        # Save image in binary mode
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

        return True

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An unexpected error occurred: {e}")

    return False

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    urls = input("Please enter image URL(s), separated by commas if multiple: ")
    url_list = [url.strip() for url in urls.split(",")]

    for url in url_list:
        if url:
            download_image(url)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
