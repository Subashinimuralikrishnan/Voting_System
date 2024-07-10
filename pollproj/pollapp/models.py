from django.db import models
#que-class
class Question(models.Model):
    text=models.CharField(max_length=300)
    pub_date=models.DateTimeField('date published')

    def __str__(self):
        return self.text
class Choice(models.Model):
    que=models.ForeignKey(Question,on_delete=models.CASCADE)
    ch_txt=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.ch_txt
    
