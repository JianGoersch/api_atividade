from models import Pessoas, db_session, Usuarios

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

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_usuarios():
    usuario = Usuarios.query.all()
    print(usuario)

if __name__=='__main__':
    #insere_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    #consulta_pessoas()
    insere_usuario('jian', '1234')
    insere_usuario('goersch', '1234')
    consulta_usuarios()
