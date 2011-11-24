#!/usr/bin/python
import random


def dcript(entrada, mapa):
	tmp = [" "] * len(entrada)
	for i in xrange(len(entrada)):
		if mapa.has_key(entrada[i]):
			tmp[i] = mapa[entrada[i]]
		else:
			tmp[i] = entrada[i]
	return tmp


def cript(entrada, mapa):
        rev_mapa = dict()
        for i in mapa:
                rev_mapa[mapa[i]] = i
	return dcript(entrada, rev_mapa)

def gerarMapa():
	letras = []
	for i in xrange(26):
		letras.append(chr(ord('A') + i))
	random.shuffle(letras)
	mapa = dict()
	for i in xrange(26):
		mapa[chr(ord('a') + i)] = letras[i]
	return mapa

mapa = {'a': 'G', 'c': 'R', 'b': 'A', 'e': 'U', 'd': 'T', 'g': 'N', 'f': 'F',\
 'i': 'K', 'h': 'I', 'k': 'Q', 'j': 'O', 'm': 'S', 'l': 'Z', 'o': 'W', 'n': 'H',\
 'q': 'B', 'p': 'C', 's': 'X', 'r': 'D', 'u': 'L', 't': 'J', 'w': 'V', 'v': 'E', 'y': 'M', 'x': 'P', 'z': 'Y'}

