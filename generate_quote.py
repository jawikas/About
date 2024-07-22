import requests
import cairosvg

# Fetch quote of the day
response = requests.get("https://quotes.rest/qod")
if response.status_code == 200:
    data = response.json()
    if "contents" in data and "quotes" in data["contents"]:
        quote = data["contents"]["quotes"][0]["quote"]
        author = data["contents"]["quotes"][0]["author"]

        # Create SVG content
        svg_content = f'''
        <svg width="400" height="200" xmlns="http://www.w3.org/2000/svg">
          <rect width="100%" height="100%" fill="#000"/>
          <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" fill="#fff" font-family="Arial" font-size="20">{quote} - {author}</text>
        </svg>
        '''

        # Save SVG to file
        with open("quote.svg", "w") as f:
            f.write(svg_content)

        # Convert SVG to PNG (optional)
        cairosvg.svg2png(url="quote.svg", write_to="quote.png")
    else:
        print("Quote data not found in API response.")
else:
    print("Failed to fetch quote of the day.")
