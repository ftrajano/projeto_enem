#!/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class Questao:
	def __init__(self, assunto,gabarito,dificuldade,imagem):
		self.assunto=assunto
		self.gabarito=gabarito
		self.dificuldade=dificuldade
		self.imagem=imagem


q1=Questao('regra de tres','b','facil','enem2018-136')
q2=Questao('regra de tres1sdfs','bgsdfgs','facilgsdfg','enem2018-136sdfgsdfg')
lista=[q1,q2]

@app.route('/')
def index():
	return render_template('index', titulo='Questoes', questoes=lista)

@app.route('/lista')
def index():
	return render_template('lista.html', titulo='Questoes', questoes=lista)


@app.route('/novo')
def novo():
	return render_template('novo.html', titulo='Adicionar Questao')


@app.route('/criar', methods=['POST',])
def criar():
	assunto=request.form['assunto']
	gabarito=request.form['gabarito']
	dificuldade=request.form['dificuldade']
	imagem=request.form['imagem']
	questao=Questao(assunto,gabarito,dificuldade,imagem)
	lista.append(questao)
	return render_template('questao.html', titulo='Questao Adicionada', questao=questao)
	#return redirect('/')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/autenticar')
def autenticar():
	if 'mestra' == request.form['senha']:
		return redirect('/', methods=['POST',])
	else:
		return redirect('/login')


if __name__ == '__main__':
	app.run(debug=True)