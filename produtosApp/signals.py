import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import ProdutosCad

@receiver(post_delete, sender=ProdutosCad)
def deletar_arquivo_imagem(sender, instance, **kwargs):
    if instance.imagem and os.path.isfile(instance.imagem.path):
        os.remove(instance.imagem.path)