# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect, HttpResponse
from django.template.context import RequestContext
from forms import CesarForm, RsaForm
from lib import CesarEncrypt, RSAEncrypt


def home(request, tipo=None):
    """
    Implementação da cifra de cesar
    """
    viewData = {}
    formCesar = CesarForm()
    formRSA = RsaForm()
    
    if tipo is not None:
        if tipo == 'rsa':
            if request.method == 'POST':
                formCesar = CesarForm(request.POST)
                if formCesar.is_valid():
                    crypto = CesarEncrypt(int(formCesar.cleaned_data['chave']))
                    request.session['cesar_msg_criptografada'] = viewData['msg_criptografada'] = crypto.encriptografar(formCesar.cleaned_data['mensagem'])
                    request.session['cesar_key'] = int(formCesar.cleaned_data['chave'])
            
    viewData['cesar_form'] = formCesar
    return render_to_response('base.html', viewData,
                              context_instance=RequestContext(request))
    
def home_uncrypt(request, tipo):
    if request.method == 'GET':
        if request.session.get('cesar_msg_criptografada', '') <> '':
            crypto = CesarEncrypt(request.session['cesar_key'])
            msgDescript = crypto.descriptografar(request.session.get('cesar_msg_criptografada', ''))
            return HttpResponse(msgDescript)
    return HttpResponse('')


def rsa(request):
    viewData = {}
    if request.method == 'POST':
        formCesar = CesarForm(request.POST)
        if formCesar.is_valid():
            pass
    
    
