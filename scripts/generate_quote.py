import requests
import cairosvg

# Fetch quote of the day
response = requests.get("https://api.quotable.io/random")
if response.status_code == 200:
    data = response.json()
    quote = data['content']
    author = data['author']

    # Create SVG content with a nicer design
    svg_content = f'''
    <svg width="600" height="200" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#282c34"/>
      <text x="50%" y="40%" text-anchor="middle" fill="#ffffff" font-family="Arial" font-size="20" font-weight="bold">{quote}</text>
      <text x="50%" y="70%" text-anchor="middle" fill="#ffffff" font-family="Arial" font-size="16" font-style="italic">- {author}</text>
    </svg>
    '''

    # Save SVG to file
    with open("quote.svg", "w") as f:
        f.write(svg_content)

    # Convert SVG to PNG (optional)
    cairosvg.svg2png(url="quote.svg", write_to="quote.png")
else:
    print("Failed to fetch quote of the day.")
