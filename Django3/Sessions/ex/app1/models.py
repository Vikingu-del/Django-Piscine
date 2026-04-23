from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return f"{self.username} (Reputation: {self.calculate_reputation()})"
    
    def calculate_reputation(self):
        user_tips = self.tips.all()
        total_upvotes = sum(tip.upvotes.count() for tip in user_tips)
        total_downvotes = sum(tip.downvotes.count() for tip in user_tips)
        return (total_upvotes * 5) - (total_downvotes * 2)
    
    def has_perm(self, perm, obj=None):
        current_rep = self.calculate_reputation()
        if perm == "app1.can_downvote_tips":
            return current_rep >= 15
        if perm == "app1.delete_tip":
            return current_rep >= 30
        return super().has_perm(perm, obj)


class Tip(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tips')
    date = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(User, related_name='upvoted_tips', blank=True)
    downvotes = models.ManyToManyField(User, related_name='downvoted_tips', blank=True)
    # hide = models.ManyToManyField(User, related_name='hidden_tips', blank=True)

    class Meta:
        permissions = [
            ("can_downvote_tips", "Can downvote any tip"),
        ]

    def __str__(self):
        return f"{self.author.username}: {self.content}, {self.date}"
