from datetime import datetime
import cairosvg

# Get current time
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

# Create SVG content
svg_content = f'''
<svg width="400" height="100" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#000"/>
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" fill="#fff" font-family="Arial" font-size="20">{current_time}</text>
</svg>
'''

# Save SVG to file
with open("time.svg", "w") as f:
    f.write(svg_content)

# Convert SVG to PNG (optional)
cairosvg.svg2png(url="time.svg", write_to="time.png")