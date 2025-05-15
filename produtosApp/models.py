from django.db import models


class ProdutosCad(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    preco_cartao = models.DecimalField(max_digits=10, decimal_places=2)
    preco_pix = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)

    def __str__(self):
        return self.nome

