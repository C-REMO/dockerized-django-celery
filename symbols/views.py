from django.shortcuts import render
from django.core.paginator import Paginator
from core.services.symbols import SymbolService


def list_all(request):
    '''
    Show ALL news.
    '''

    feeds = SymbolService.get_all()
    pages = Paginator(feeds, 5).get_page(request.GET.get('page'))

    data = {
        'feeds': pages,
        'feed_type': None
    }
    return render(request, 'symbols/index.html', data)


def list_by_type(request, symbol_type):
    '''
    Show FEEDS by type.
    1 is AAPL symbol type
    2 is TWTR symbol type
    3 is GOLD symbol type
    4 is INTC symbol type
    '''

    feeds = SymbolService.get_all_by_type(symbol_type)
    pages = Paginator(feeds, 5).get_page(request.GET.get('page'))

    data = {
        'feeds': pages,
        'feed_type': feeds[0].get_feed_type() if feeds else None
    }
    return render(request, 'symbols/index.html', data)
