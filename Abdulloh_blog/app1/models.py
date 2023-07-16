from django.db import models


class Category(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Tags(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Author(models.Model):
    full_name=models.CharField(max_length=100,default='Unknown')
    birth_year=models.DateField()
    your_status=models.CharField(max_length=200,default='Nothing is impossible in life.')
    img=models.FileField(upload_to='blog-img',default=None, blank=True, null=True)

    def __str__(self):
        return self.full_name


class Blog(models.Model):
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,null=True,blank=True)
    img=models.FileField(upload_to='blog-img')
    title=models.CharField(max_length=250)
    text=models.TextField()
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL,null=True,blank=True)
    tag=models.ForeignKey(Tags,on_delete=models.SET_NULL, null=True,blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    name=models.CharField(max_length=50)
    text=models.CharField(max_length=250)
    date=models.DateField(auto_now=True)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,default=None)
    picture=models.FileField(upload_to='comment',null=True,blank=True,default=None)

    def __str__(self):
        return self.name
