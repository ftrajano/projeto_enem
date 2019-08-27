#!/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)

class Questao:
	def __init__(self, assunto,gabarito,dificuldade,imagem):
		self.assunto=assunto
		self.gabarito=gabarito
		self.dificuldade=dificuldade
		self.imagem=imagem


q1=Questao('regra de tres','b','facil','enem2018-136')
lista=[q1]

@app.route('/')

def index():
	return render_template('lista.html', titulo='Questoes', questoes=lista)


@app.route('/novo')
def novo():
	return render_template('novo.html', titulo='Adicionar Questao')


@app.route('/criar', methods=['POST',])
def create():
	assunto=request.form['assunto']
	gabarito=request.form['gabarito']
	dificuldade=request.form['dificuldade']
	imagem=request.form['imagem']
	questao=Questao(assunto,gabarito,dificuldade,imagem)
	lista.append(questao)
	return render_template('questao.html', titulo='Teu cu', questao=questao)

if __name__ == '__main__':
        app.run()