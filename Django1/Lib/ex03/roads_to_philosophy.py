import sys
import requests
from bs4 import BeautifulSoup

def get_wikipedia_page(title: str) -> str:
    url = "https://en.wikipedia.org/w/index.php"
    
    params = {
        "search": title,
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    try:
        response = requests.get(url, params=params, headers=headers, allow_redirects=True)

        if response.status_code == 404:
            print("It's a dead end !")
            sys.exit(0)

        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: A network or request error ocurred: {e}")
        sys.exit(1)


def recursive_search(title: str, roads: list) -> str:
    html = get_wikipedia_page(title=title)
    soup = BeautifulSoup(html, 'html.parser')

    h1_tag = soup.find(id="firstHeading")
    if not h1_tag:
        print("It's a dead end !")
        sys.exit(0)
    
    current_title = h1_tag.get_text()
    if current_title in roads:
        print("It leads to an infinite loop !")
        sys.exit(0)

    # 3. Print and record this step
    print(current_title)
    roads.append(current_title)

    # 4. Check if we reached the goal
    if current_title == "Philosophy":
        # The subject wants the count of articles visited
        print(f"{len(roads)} roads from {roads[0]} to philosophy !")
        sys.exit(0)

    # 5. Find the NEXT link
    content = soup.find(id="bodyContent")

    if content:
        paragraphs = content.find_all("p")
        for p in paragraphs:
            links = p.find_all("a")
            for link in links:
                href = link.get('href')
                if href and href.startswith("/wiki/") and ":" not in href:
                    # Extract the next title and recurse
                    next_title = href.split('/')[-1]
                    recursive_search(next_title, roads)
                    return

    # If the loop finishes without finding a link
    print("It's a dead end !")
    sys.exit(0)



def main():
    if len(sys.argv) != 2 or sys.argv == "":
        print("Usage: python roads_to_philosophy.py <word>")
        sys.exit(1)

    recursive_search(title=sys.argv[1], roads=[])


if __name__ == "__main__":
    main()