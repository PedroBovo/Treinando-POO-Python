from modelos.avaliacao import Avaliacao

class Pessoa:

    pessoas =[]

    def __init__(self, nome, idade) -> None:
        self._nome = nome
        self._idade = idade
        self._avaliacoes = []
        Pessoa.pessoas.append(self)

    
    def __str__(self) -> str:
        return f"{self._nome.ljust(25)} | {str(self._idade).ljust(25)} | {self.media_avaliacoes()}"
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return "18+" if self._idade >18 else "-18"    
    
    def receber_nota(self, prova, nota):
        avaliacao = Avaliacao(prova, nota)
        self._avaliacoes.append(avaliacao)

    def media_avaliacoes(self):
        if not self._avaliacoes:
            return 0
        
        soma = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        quantidade_notas = len(self._avaliacoes)
        media = round(soma / quantidade_notas, 1)

        return media
            


    @classmethod
    def listar_pessoas(cls):
        print(f"{"nome".ljust(25)} | {"idade".ljust(25)} | {"Media de notas"}\n")
        for pessoa in cls.pessoas:
            print(f"{pessoa._nome.ljust(25)} | {str(pessoa.idade).ljust(23)} | {pessoa.media_avaliacoes}")





