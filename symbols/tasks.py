from celery import shared_task
from celery.utils.log import get_task_logger
from datetime import datetime
import xml.etree.ElementTree as ET
import requests
from .models import FeedRecord
from core.services.symbols import SymbolService

logger = get_task_logger(__name__)


@shared_task
def task_save_yahoo_feeds(*args, **kwargs):
    """
    Saves latest feeds from yahoo
    """
    symbols = [('AAPL', 1), ('TWTR', 2), ('GOLD', 3), ('INTC', 4)]
    domain = 'https://feeds.finance.yahoo.com'

    for symbol, symbol_type in symbols:
        url = f'{domain}/rss/2.0/headline?s={symbol}&region=US&lang=en-US'
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en,bs;q=0.7,hr;q=0.3',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Host': 'feeds.finance.yahoo.com',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Linux x86_64; rv:94.0) Firefox/94.0'}

        resp = requests.get(url, headers=headers)
        root = ET.fromstring(resp.content)
        items = root.findall(".//item")

        for item in items:
            description = item.find('description').text
            title = item.find('title').text
            link = item.find('link').text
            guid = item.find('guid').text

            SymbolService.create(description, guid, title, link, symbol_type)

    logger.info(f"Feeds from Yahoo updated on {datetime.today()}")
