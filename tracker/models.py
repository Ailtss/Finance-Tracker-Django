from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import TransactionQuerySet

class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'Categorias'
    def __str__(self):
        return self.name

# Uma transação pode ser Receita ou Despesa
# Tem um valor
# Possui uma Categoria (Chave Estrangeira)
# É vinculada a um usuário (Chave Estrangeira)
# Possui uma data
class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = (
        ("receita", "Receita"),
        ("despesa", "Despesa"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE) #Se deletar o usuário, deleta as transações
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.CharField(max_length=7, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    objects = TransactionQuerySet.as_manager()
    

    def __str__(self):
        return f"{self.type} de {self.amount} na {self.date} pelo {self.user}"
    
    class Meta:
        ordering = ['-date']