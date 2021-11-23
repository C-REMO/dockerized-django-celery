from symbols.services.modelservice import SymbolModelService


class SymbolService:

    @staticmethod
    def get_all():
        return SymbolModelService.get_all()

    @staticmethod
    def get_by_title(title):
        return SymbolModelService.get_by_title(title)

    @staticmethod
    def get_by_description(description):
        return SymbolModelService.get_by_description(description)

    @staticmethod
    def get_by_permalink(permalink):
        return SymbolModelService.get_by_permalink(permalink)

    @staticmethod
    def get_by_url(url):
        return SymbolModelService.get_by_url(url)

    @staticmethod
    def get_all_by_type(symbol_type):
        return SymbolModelService.get_all_by_type(symbol_type)

    @staticmethod
    def create(description, permalink, title, url, symbol_type):
        return SymbolModelService.create(
            description, permalink, title, url, symbol_type
        )
