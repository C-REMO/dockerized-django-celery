from ..models import FeedRecord


class SymbolModelService:
    """Symbol model service."""

    @staticmethod
    def get_all():
        return FeedRecord.objects.all()

    @staticmethod
    def get_by_title(title):
        try:
            return FeedRecord.objects.get(title=title)
        except FeedRecord.DoesNotExist:
            return None

    @staticmethod
    def get_by_description(description):
        try:
            return FeedRecord.objects.get(description=description)
        except FeedRecord.DoesNotExist:
            return None

    @staticmethod
    def get_by_url(url):
        try:
            return FeedRecord.objects.get(url=url)
        except FeedRecord.DoesNotExist:
            return None

    @staticmethod
    def get_by_permalink(permalink):
        try:
            return FeedRecord.objects.get(permalink=permalink)
        except FeedRecord.DoesNotExist:
            return None

    @staticmethod
    def get_all_by_type(symbol_type):
        return FeedRecord.objects.filter(symbol_type=symbol_type)

    @staticmethod
    def create(description, permalink, title, url, symbol_type):
        if not SymbolModelService.check_feed_exists(permalink):
            return FeedRecord.objects.create(
                description=description,
                permalink=permalink,
                title=title,
                url=url,
                symbol_type=symbol_type)

    @staticmethod
    def check_feed_exists(permalink):
        return FeedRecord.objects.filter(permalink=permalink)
