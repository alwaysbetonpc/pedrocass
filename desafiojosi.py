class Aluno():
    def __init__(self, matricula, nome, sexo, idade):
        self.matricula = matricula
        self.nome = nome
        self.sexo = sexo
        self.idade = idade

aluno1 = Aluno(12345, 'Pedro Canto', 'Masculino', 17 )
print('Matricula', aluno1.matricula)
print('Nome', aluno1.nome)
print('Sexo', aluno1.sexo)
print('Idade', aluno1.idade )