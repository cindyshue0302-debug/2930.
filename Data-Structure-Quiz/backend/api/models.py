from django.db import models

class Question(models.Model):
  
    tag = models.CharField(max_length=50)
    
  
    question = models.CharField(max_length=500)
    
  
    options = models.JSONField()
    
  
    answer = models.CharField(max_length=200)

   
    def __str__(self):
        return self.question


class QuizRecord(models.Model):

    nickname = models.CharField(max_length=50)
    

    score = models.IntegerField()
 
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.nickname} - {self.score}分"