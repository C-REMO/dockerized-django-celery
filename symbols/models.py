import uuid
from django.db import models


AAPL = 1
TWTR = 2
GOLD = 3
INTC = 4
NOT_VALID = 999
SYMBOL_CHOICES = (
    (AAPL, "AAPL Symbol Type"),
    (TWTR, "TWTR Symbol Type"),
    (GOLD, "GOLD Symbol Type"),
    (INTC, "INTC Symbol Type"),
    (NOT_VALID, "Invalid Type"),
)


class BaseRecord(models.Model):

    class Meta:
        abstract = True


class FeedRecord(BaseRecord):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    permalink = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    url = models.URLField(max_length=2048, blank=True, null=True)
    symbol_type = models.PositiveSmallIntegerField(
        choices=SYMBOL_CHOICES, default=999)

    class Meta:
        ordering = ['-time_created']

    def get_feed_type(self):
        """Return readable feed value."""
        return dict(SYMBOL_CHOICES)[self.symbol_type]
