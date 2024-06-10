from modelos.pessoa import Pessoa

Pessoa1 = Pessoa("Pedro", 22)

Pessoa1.receber_nota("Matematica", 10)
Pessoa1.receber_nota("Portugues", 5)
Pessoa1.receber_nota("Ciencias", 9)

Pessoa1.media_avaliacoes()
print(Pessoa1)