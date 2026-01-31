import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fetch and parse the homepage
res = requests.get("https://www.python.org")
soup = BeautifulSoup(res.content, "html.parser")

# Extract article titles from widgets
titles = [a.get_text(strip=True)
          for cls in ['event-widget', 'blog-widget']
          for a in soup.select(f".medium-widget.{cls} a")]

# Create DataFrame (without saving to file)
df = pd.DataFrame(titles, columns=["Article Title"])

# Print DataFrame
print(df)
