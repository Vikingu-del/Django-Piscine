import sys
import dewiki
import json
import requests

def req_wiki(query: str):
    url = "https://fr.wikipedia.org/w/api.php"

    headers = {
        "User-Agent": "MyWikiTool/1.0 (contact: eseferi@student.42vienna.com)"
    }

    params = {
        "action": "parse",
        "format": "json",
        "page": query,
        "prop": "wikitext",
        "redirects": 1
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status() # Check for HTTP errors
        # data = response.json() # build in request.json()
        data = json.loads(response.text)
        # dumped_Data = json.dumps(data, indent=4) 
        # print(f"{dumped_Data}")

        # Check if Wikipedia returned an error (e.g., page not found)
        if "error" in data:
            print(f"Error: {data['error'].get('info', 'Page not found')}")
            sys.exit(1)

        # Extract raw wikitext
        wikitext = data["parse"]["wikitext"]["*"]

        if "\n\n" in wikitext:
            # We split the text by double newlines and keep 
            # everything from the first "real" paragraph onwards.
            parts = wikitext.split("\n\n")
            # We filter out parts that start with '{{' (templates)
            clean_parts = [p for p in parts if not p.strip().startswith("{{")]
            wikitext = "\n\n".join(clean_parts)

        # Use dewiki to remove Wiki Markup (links, bolding, etc.)
        # We strip trailing whitespace to keep it clean
        clean_text = dewiki.from_string(wikitext).strip()

        return clean_text

    except requests.exceptions.RequestException as e:
        print(f"Server error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)  
    print(r.status_code)

def main():
    if len(sys.argv) != 2 or sys.argv == "":
        print("Usage: python request_wikipedia.py <word>")
        sys.exit(1)
    
    # Format filename
    query = sys.argv[1]
    content = req_wiki(query)
    filename = query.replace(" ", "_") + ".wiki"

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        print(f"Error writing to file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()