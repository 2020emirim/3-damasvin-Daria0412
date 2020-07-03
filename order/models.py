from django.db import models

class Order(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, related_name = 'order')
    stock = models.PositiveIntegerField(default=1)
    cup = models.IntegerField() # 0 레귤러, 1 점보
    ice = models.IntegerField(default=100) #0 50 100 150
    sugar = models.IntegerField(default=100) # 0 50 100 150
    price = models.IntegerField()

    def __str__(self):
        return f'음료 : {sekf.drink}, 개수 : {sekf.stock}, 컵사이즈 : {sekf.cup}, 얼음량 : {sekf.ice}, 당도 : {sekf.sugar}, 가격 : {sekf.price}'

