from models import Pessoas, db_session

def insere_pessoas():
    pessoa = Pessoas(nome='Jian2', idade=32)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Jian').first()
    print(pessoa.idade)
    #for p in pessoa:
        #print(p)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Jian').first()
    pessoa.idade = 21
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Jian2').first()
    pessoa.delete()


if __name__=='__main__':
    #insere_pessoas()
    #altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
