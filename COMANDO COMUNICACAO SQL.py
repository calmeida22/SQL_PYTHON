import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="aulapython"
)

cursor = conexao.cursor()
# COMANDOS PARA CRIAR, ALTERAR, INSERIR DADOS EM UMA TABELA
# cursor.execute("CREATE TABLE deparmanto(iddepto integer, nomedep varchar(50));")
# cursor.execute("ALTER TABLE deparmanto RENAME TO departamento;")
# cursor.execute"""("INSERT INTO usuario(idUsuario,dataNascimento,nome)
#          VALUES(4,20200708,'Vera'),(3,19990214,'Maria')")"""
# cursor.execute("ALTER TABLE usuario MODUFY COLUMN idUsuario integer AUTO_INCREMENT;")
# cursor.execute"""("INSERT INTO usuario(dataNascimento,nome)
#           VALUES(19990525,'Jose'),(19970612,'Rosa');")"""

# COMANDO PARA MOSTRAR NA TELA AS INFORMAÇÕES DE UMA TABELA
# cursor.execute("SELECT * FROM usuario;")
# resultado = cursor.fetchall()
# print('')
# for linha in resultado:
#    print(linha)

# COMANDO PARA DELETAR UM DADO DO BANCO DE DADOS
# comando="DELETE FROM usuario WHERE idUsuario=7"
# cursor.execute(comando)

# COMANDO PARA DELETAR UM DADO DO BANCO DE DADOS
# comando="UPDATE usuario SET nome='Joaquim' WHERE idUsuario=8"
# cursor.execute(comando)

# COMANDO INSERIR INFORMAÇÕES BANCO DE DADOS NA TABELA USUARIO
# nome = input('Digite um nome para usuário: ')
# dataNascimento = input('Digite a data de nascimento do usuário (ex.:AAAAMMDD: ')
# print('O nome é:', nome, ' e data de nascimento é:', dataNascimento)
# comando = f"""INSERT INTO usuario(nome,dataNascimento)
#            VALUES('{nome}',{dataNascimento})"""
# cursor.execute(comando)

# COMANDO INSERIR INFORMAÇÕES BANCO DE DADOS NA TABELA DEPARTAMENTO
# nomedep = input('Digite departamento para cadastrar: ')
# print('O departamento inserido é:', nomedep, )
# comando = f"""INSERT INTO departamento(nomedep)
#            VALUES('{nomedep}')"""
# cursor.execute(comando)

conexao.commit()

cursor.close()
conexao.close()
