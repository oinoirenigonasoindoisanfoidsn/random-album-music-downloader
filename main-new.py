import requests
import re
import sys
import os

def get_random_album_url():
    """Fetches a random album URL from random-album.com by extracting window.currentAlbum.url"""
    url = "https://random-album.com/"
    response = requests.get(url)

    if response.status_code == 200:
        match = re.search(r'window\.currentAlbum\s*=\s*{[^}]*"url"\s*:\s*"([^"]+)"', response.text)
        if match:
            return match.group(1)  # Extract the album URL

    return None

def main():
    if len(sys.argv) >= 2:
        try:
            amount = int(sys.argv[1])
        except ValueError:
            sys.exit("That was an invalid input! Program will now close.")
    else:
        try:
            amount = int(input("How many albums do you want to download?: "))
        except ValueError:
            sys.exit("That was an invalid input! Program will now close.")

    for x in range(amount):
        album_link = get_random_album_url()
        if album_link:
            print(f"{x + 1}: {album_link}")
            dir_path = os.path.dirname(os.path.realpath(__file__))
            os.system(f'bandcamp-dl --base-dir="{dir_path}/music" --full-album --embed-art --template="%{{album}}/%{{track}} - %{{title}}" {album_link}')
        else:
            print("Failed to retrieve a random album URL.")

if __name__ == "__main__":
    main()
