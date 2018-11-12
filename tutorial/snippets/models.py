# snippets/models.py
from django.db import models
from pygments import highlight # new
from pygments.formatters.html import HtmlFormatter # new
from pygments.lexers import get_all_lexers, get_lexer_by_name # new
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE) # new
    highlighted = models.TextField() # new

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs): # new
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Category(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    cost = models.TextField()
    minPeople = models.TextField()
    maxPeople = models.TextField()
    isEnabled = models.BooleanField(default=True)
    owner = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE) # new

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs): # new
        options = {'title': self.title} if self.title else {}
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Tags(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    relatedname1 = models.CharField(max_length=100, blank=True, default='')
    relatedname2 = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.name


class Service(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    category = models.ForeignKey("snippets.Category", related_name="services",on_delete=models.CASCADE)
    differential = models.TextField() #adds or reduces cost 
    isEnabled = models.BooleanField(default=True)
    owner = models.ForeignKey('auth.User', related_name='services', on_delete=models.CASCADE) # new
    minPeople = models.TextField()
    maxPeople = models.TextField()
    imgsrc = models.TextField()
    isAvailable = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tags)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs): # new
        options = {'title': self.title} if self.title else {}
        super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


#Test Class to Be defined
class Carousel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    category = models.ForeignKey("snippets.Category", related_name="carousels",on_delete=models.CASCADE)
    imgSrc = models.TextField()
    isEnabled = models.BooleanField(default=True)
    owner = models.ForeignKey('auth.User', related_name='carousels', on_delete=models.CASCADE) # new

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs): # new
        options = {'title': self.title} if self.title else {}
        super(Carousel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Profile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, default='')
    email = models.CharField(max_length=100, blank=False, default='')
    phonenumber = models.CharField(max_length=100, blank=True, default='')
    phonenumber2 = models.CharField(max_length=100, blank=True, default='')
    owner = models.OneToOneField(
        'auth.User',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs): # new
        options = {'name': self.name} if self.name else {}
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Inquiry(models.Model):
    
    created = models.DateTimeField(auto_now_add=True)
    details = models.CharField(max_length=300, blank=False, default='')
    total = models.CharField(max_length=100, blank=False, default='0')
    owner = models.ForeignKey('auth.User',related_name="inquiries",on_delete=models.CASCADE,)
    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs): # new
        options = {'name': self.details} if self.details else {}
        super(Inquiry, self).save(*args, **kwargs)

    def __str__(self):
        return self.details


class Concept(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    quantity = models.CharField(max_length=100, blank=False, default='0')
    
    service = models.ForeignKey("snippets.Service", related_name="concepts",on_delete=models.CASCADE,primary_key=False)

    owner = models.ForeignKey("auth.User", related_name="concepts",on_delete=models.CASCADE,primary_key=False)
    
    inquiry = models.ForeignKey("snippets.Inquiry", related_name="concepts",on_delete=models.CASCADE,primary_key=True)
    
    subtotal = models.CharField(max_length=100, blank=False, default='0')
    
    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs): # new
        options = {'name': self.quantity} if self.quantity else {}
        super(Concept, self).save(*args, **kwargs)

    def __str__(self):
        return self.quantity

