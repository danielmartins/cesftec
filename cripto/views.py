# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect, HttpResponse
from django.template.context import RequestContext
from forms import CesarForm
import string

class CesarEncrypt(object):
    
    def __init__(self, key=3):
        self.alfa = list(string.ascii_lowercase)
        self.alfa.append(' ') # inserindo espaço na lista de caracteres
        self.key = key
        
    def separar(self, msg):
        # Guarda as chaves para as letras das mensagems
        # Exemplo: A = 0, B = 1 e etc.
        chavesMsg = []
        for m in msg.lower():
            chavesMsg.append(self.alfa.index(m))
        return chavesMsg
            
    def encriptografar(self, msg):
        self.chavesMsg = self.separar(msg)
        self.msgCriptografada = ""
        for chave in self.chavesMsg:
            idx_novo_valor = chave + self.key
            if idx_novo_valor >= len(self.alfa):
                idx_novo_valor = idx_novo_valor % len(self.alfa)
            self.msgCriptografada += self.alfa[idx_novo_valor]
        return self.msgCriptografada
            
    
    def descriptografar(self, msgCriptografada):
        self.chavesMsgCriptografada = self.separar(msgCriptografada)
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
    viewData = {}
    formCesar = CesarForm()
    if request.method == 'POST':
        formCesar = CesarForm(request.POST)
        if formCesar.is_valid():
            crypto = CesarEncrypt(int(formCesar.cleaned_data['chave']))
            request.session['cesar_msg_criptografada'] = viewData['msg_criptografada'] = crypto.encriptografar(formCesar.cleaned_data['mensagem'])
            request.session['cesar_key'] = int(formCesar.cleaned_data['chave'])
            
    viewData['cesar_form'] = formCesar
    #return HttpResponse(crypto.encriptografar() + "<br/>" + crypto.descriptografar())
    return render_to_response('base.html', viewData,
                              context_instance=RequestContext(request))
    
def cesar_uncrypt(request):
    if request.method == 'GET':
        if request.session.get('cesar_msg_criptografada', '') <> '':
            crypto = CesarEncrypt(request.session['cesar_key'])
            msgDescript = crypto.descriptografar(request.session.get('cesar_msg_criptografada', ''))
            return HttpResponse(msgDescript)
    return HttpResponse('')
    
    