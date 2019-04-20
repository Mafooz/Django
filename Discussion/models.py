from django.db import models
from django.contrib.auth.models import User

#class Tag(models.Model):
#	title=models.CharField(max_length=255,unique=True)
#	def __str__(self):
#		return self.title
postags=[('','-----'),('1','Guitar'),('2','Blockchain'),('3','Flute')]
class Post(models.Model):
	title=models.CharField(max_length=255)
	Author=models.ForeignKey('auth.User',on_delete=models.CASCADE, null=True)
	body=models.TextField()
	posted=models.DateField(db_index=True, auto_now_add=True)
	tags=models.CharField(max_length=255,choices=postags,null=True)
	def __str__(self):
		return self.title

class Comment(models.Model):
	ctor=models.ForeignKey('auth.User',on_delete=models.CASCADE, null=True)
	cdate=models.DateField(db_index=True, auto_now_add=True)
	cbody=models.TextField()
	cpost=models.ForeignKey('Post',on_delete=models.CASCADE, null=True)

	def __str__(self):
		return str(self.ctor)+str(self.cpost)+str(self.cbody)
	

