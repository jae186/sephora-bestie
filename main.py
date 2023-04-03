import asyncio
import os
import telegram
from bs4 import BeautifulSoup
import aiohttp

telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
chat_id = os.environ['CHAT_ID']

bot = telegram.Bot(token=telegram_bot_token)

# URL of the website to scrape
url = 'https://www.sephora-events.com/'

async def my_function():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.text()

    soup = BeautifulSoup(content, 'html.parser')
    zoom_links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href is not None and href.startswith('https://sephora.zoom'):
            zoom_links.append(href)

    # Send a notification if new links are available
    zoom_links = set(zoom_links)
    if len(zoom_links) > 2:
        message = "New links available: " + str(zoom_links)
        await bot.send_message(chat_id=chat_id, text=message)

loop = asyncio.get_event_loop()
loop.run_until_complete(my_function())
