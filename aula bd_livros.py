import mysql.connector

con = mysql.connector.connect(host='localhost', database='db_livros', user='root', password='')

if con.is_connected():
    info = con.get_server_info()
    print('Conectado ao servidor mysql versão', info)
    cursor = con.cursor()
    cursor.execute('select date base();')
    linha = cursor.fetchone()
    print('Conectado ao banco de dados', linha)
if con.is_connected():
    cursor.close()
    con.close()
    print("conexão ao mysql foi encerrada")
# Não deu certo olhar depois os erros
