from .models import FeedRecord
from django.test import TestCase
from core.services.symbols import SymbolService


class CreatingFeedObjectTest(TestCase):
    def __init__(self, *args, **kwargs):
        super(CreatingFeedObjectTest, self).__init__(*args, **kwargs)
        self.title = "Test title"
        self.wrong_title = "This si wrong title"
        self.description = "Test description"
        self.wrong_description = "This is wrong description"
        self.url = "https://www.example.com"
        self.wrong_url = "https://www.wrongexample.com"
        self.permalink = "abcd"
        self.wrong_permalink = "dcba"

    def setUp(self):
        self.feed = SymbolService.create(
            self.description, self.permalink, self.title, self.url, 1
        )
        self.feed.save()

    def tearDown(self):
        self.feed.delete()

    def test_feed_by_title(self):
        feed = SymbolService.get_by_title(self.title)
        self.assertNotEqual(feed, None)
        if feed:
            self.assertEqual(feed.title, self.title)

    def test_feed_by_title_negative(self):
        feed = SymbolService.get_by_title(self.wrong_title)
        self.assertEqual(feed, None)

    def test_feed_by_description(self):
        feed = SymbolService.get_by_description(self.description)
        self.assertNotEqual(feed, None)
        if feed:
            self.assertEqual(feed.description, self.description)

    def test_feed_by_description_negative(self):
        feed = SymbolService.get_by_description(self.wrong_description)
        self.assertEqual(feed, None)

    def test_feed_by_url(self):
        feed = SymbolService.get_by_url(self.url)
        self.assertNotEqual(feed, None)
        if feed:
            self.assertEqual(feed.url, self.url)

    def test_feed_by_url_negative(self):
        feed = SymbolService.get_by_url(self.wrong_url)
        self.assertEqual(feed, None)

    def test_feed_by_permalink(self):
        feed = SymbolService.get_by_permalink(self.permalink)
        self.assertNotEqual(feed, None)
        if feed:
            self.assertEqual(feed.permalink, self.permalink)

    def test_feed_by_permalink_negative(self):
        feed = SymbolService.get_by_permalink(self.wrong_permalink)
        self.assertEqual(feed, None)
