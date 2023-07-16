from django.db import models


class Home(models.Model):
    title_unusual_events=models.CharField(max_length=50)
    description=models.TextField()
    img=models.FileField(upload_to="event")

    def __str__(self):
        return self.title_unusual_events

class About_me(models.Model):
    who_am_I=models.CharField(max_length=100)
    short_story=models.TextField()
    video=models.FileField(upload_to='video')

    def __str__(self):
        return self.who_am_I

class My_life(models.Model):
    img=models.FileField(upload_to='my_life')
    my_story_title=models.CharField(max_length=50)
    my_story=models.TextField()
    second_img=models.FileField(upload_to='my_life')
    my_second_story_title=models.CharField(max_length=50)
    my_second_story=models.TextField()

    def __str__(self):
        return self.my_story_title

class My_achchivements(models.Model):
    img=models.FileField(upload_to='my_achchivments')
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)

    def __str__(self):
        return self.title

class My_status_for_future(models.Model):
    title=models.CharField(max_length=50)
    text=models.TextField()
    img=models.FileField(upload_to='mission')

    def __str__(self):
        return self.title

class Surprising_situations(models.Model):
    img=models.FileField(upload_to='surprising_situation')
    title=models.CharField(max_length=30)
    interesting_emotion=models.CharField(max_length=50)
    description=models.CharField(max_length=250)

    def __str__(self):
        return self.title

class My_portfolio(models.Model):
    portfoli_descriptions=models.CharField(max_length=250)
    img1=models.FileField(upload_to='portfolio')
    img2=models.FileField(upload_to='portfolio')
    img3=models.FileField(upload_to='portfolio',null=True,blank=True)
    name=models.CharField(max_length=50)
    description=models.TextField()
    client=models.CharField(max_length=30)
    project_finishing_date=models.DateField()
    project_url=models.CharField(max_length=100, null=True, blank=True,default=None)

    def __str__(self):
        return self.name


class My_images(models.Model):
    img1=models.FileField(upload_to="my_pictures", default=None, null=True)
    # img2=models.FileField(upload_to="my_pictures", default=None, null=True, blank=True)
    # img3=models.FileField(upload_to="my_pictures", default=None, null=True, blank=True)
    # img4=models.FileField(upload_to="my_pictures", default=None, null=True, blank=True)
    # img5=models.FileField(upload_to="my_pictures", default=None, null=True, blank=True)











