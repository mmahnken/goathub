# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices


class Goat(TimeStampedModel, StatusModel, models.Model):
    """A goat. """

    STATUS = Choices('private', 'published')

    user = models.ForeignKey(
        User,
        null=False,
    )

    name = models.CharField(
        max_length=40,
    )

    photo = models.ImageField(
        upload_to="goats",
        blank=True,
    )

    description = models.TextField(
        blank=True,
        help_text="Additional information about this goat."
    )

    notes = models.TextField(
        blank=True,
        help_text="Internal notes about this goat."
    )

class Comment(TimeStampedModel, models.Model):
    """A comment about a goat."""

    user = models.ForeignKey(
        User,
        null=False,
    )

    goat = models.ForeignKey(
        Goat,
        null=False,
    )

    comment = models.TextField(
        null=False,
    )
