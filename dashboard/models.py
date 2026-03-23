from django.db import models



class EXP(models.Model):
    level = models.IntegerField(null=False, verbose_name="Lv")
    character_name = models.CharField(max_length=10, default="未設定", verbose_name="キャラクター名")
    user_id = models.IntegerField(null=True,verbose_name="ユーザーID")
    
    
    
    
