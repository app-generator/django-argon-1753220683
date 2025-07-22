# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Note(models.Model):

    #__Note_FIELDS__
    note_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.CharField(max_length=255, null=True, blank=True)
    created_on = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Note_FIELDS__END

    class Meta:
        verbose_name        = _("Note")
        verbose_name_plural = _("Note")


class Sharednote(models.Model):

    #__Sharednote_FIELDS__
    note_id = models.ForeignKey(Note, on_delete=models.CASCADE)
    share_link = models.CharField(max_length=255, null=True, blank=True)
    public = models.BooleanField()
    shared_on = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Sharednote_FIELDS__END

    class Meta:
        verbose_name        = _("Sharednote")
        verbose_name_plural = _("Sharednote")


class Comment(models.Model):

    #__Comment_FIELDS__
    shared_note_id = models.ForeignKey(SharedNote, on_delete=models.CASCADE)
    created_on = models.DateTimeField(blank=True, null=True, default=timezone.now)
    content = models.TextField(max_length=255, null=True, blank=True)

    #__Comment_FIELDS__END

    class Meta:
        verbose_name        = _("Comment")
        verbose_name_plural = _("Comment")



#__MODELS__END
