import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='ftrajano', passwd='Tra1ano', host='mysql.ftrajano.kinghost.net')


# inserindo usuarios
cursor = conn.cursor()
cursor.execute('INSERT INTO ftrajano.questoes (imagem, assunto, gabarito,dificuldade) VALUES (%s, %s, %s, %s)',('end1', 'Trigonometria', 'a','facil'))

#cursor.execute('select * from jogoteca.questoes')
#print(' -------------  Usuários:  -------------')
#for end in cursor.fetchall():
#    print(end[1])

# commitando senão nada tem efeito
conn.commit()
cursor.close()
