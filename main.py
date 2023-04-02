import asyncio
import requests
import telegram
from bs4 import BeautifulSoup


bot = telegram.Bot(token='6238012639:AAGrE_gmnMr1DoygZ2iD-Zw-OUvNUvJeX7Q')
chat_id = '6023747101'

# URL of the website to scrape
url = 'https://www.sephora-events.com/'

async def my_function():
    # Perform the web scraping and link checking
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    zoom_links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href is not None and href.startswith('https://sephora.zoom'):
            zoom_links.append(href)

    # Send a notification if new links are available
    zoom_links = set(zoom_links)
    if len(zoom_links) > 1:
        message = "New links available: " + str(zoom_links)
        await bot.send_message(chat_id=chat_id, text=message)

loop = asyncio.get_event_loop()
loop.run_until_complete(my_function())

    

