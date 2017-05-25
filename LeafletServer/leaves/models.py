"""
Models for leaves
"""

from django.conf import settings
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())
    

class Leaf(models.Model):
    """
    Class for Leaves
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name=
                              'leaves', default='', on_delete=models.CASCADE)
    leaf_type = models.PositiveSmallIntegerField() 
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python',
                                max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly',
                             max_length=100)
    """
    tryna get array input for id numbers that have edit/comment/read access to leaf
    edit_access[] = models.IntegerField()
    comment_access[] = models.IntegerField()
    write_access[] = models.IntegerField()
    """
    
class Page(models.Model):
    """
    Class for Pages
    """
    
class Section(models.Model):
    """
    Class for Sections
    """

class Leaflet(models.Model):
    """
    Class for Leaflets
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='leaves', default='', on_delete=models.CASCADE)
    class Meta:
        """
        Meta class for django
        """
        ordering = ('created',)
        
