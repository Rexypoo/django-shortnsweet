from django.db import models
from django.core.validators import URLValidator, validate_slug
from django.utils.translation import gettext_lazy as _

class ShortURL(models.Model):

    # For TextField max_length only affects display
    url = models.TextField(
        max_length=70,
        validators=[URLValidator()],
    )

    alias = models.SlugField(
        db_index=True,
        max_length=200,
        help_text=_('Short name for the given URL'),
        unique=True,
        # This needs a randomized default
        validators=[validate_slug],
    )

    def __str__(self):
        return self.alias
