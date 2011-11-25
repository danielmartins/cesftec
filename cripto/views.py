# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect, HttpResponse
from django.template.context import RequestContext
from forms import CesarForm
import string

class CesarEncrypt(object):
    
    def __init__(self, msg, key=3):
        self.alfa = list(string.ascii_lowercase)
        self.msg = msg
        self.key = key
        
    def separar(self, msg):
        # Guarda as chaves para as letras das mensagems
        # Exemplo: A = 0, B = 1 e etc.
        chavesMsg = []
        for m in msg:
            chavesMsg.append(self.alfa.index(m))
        return chavesMsg
            
    def encriptografar(self):
        self.chavesMsg = self.separar(self.msg)
        self.msgCriptografada = ""
        for chave in self.chavesMsg:
            idx_novo_valor = chave + self.key
            if idx_novo_valor >= len(self.alfa):
                idx_novo_valor = idx_novo_valor % len(self.alfa)
            self.msgCriptografada += self.alfa[idx_novo_valor]
        return self.msgCriptografada
            
    
    def descriptografar(self):
        self.chavesMsgCriptografada = self.separar(self.msgCriptografada)
        self.msgDescriptografada = ""
        for chave in self.chavesMsgCriptografada:
            idx_valor = chave - self.key
            if idx_valor in range(len(self.alfa) - 1):
                self.msgDescriptografada += self.alfa[idx_valor]
            else:
                self.msgDescriptografada += self.alfa[idx_valor % len(self.alfa)]
        return self.msgDescriptografada

def cesar(request):
    """
    Implementação da cifra de cesar
    """
    msg2encrypt = "teste"
    crypto = CesarEncrypt(msg2encrypt, 3)
    form = CesarForm()
    #return HttpResponse(crypto.encriptografar() + "<br/>" + crypto.descriptografar())
    return render_to_response('base.html', {"cesar_form": form}, context_instance=RequestContext(request))



