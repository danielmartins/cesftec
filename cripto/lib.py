# -*- coding: utf-8 -*-

from random import choice, randint
import string
from pprint import pprint

class TransposicaoEncrypt(object):
    
    def __init__(self):
        self.alfa = list(string.ascii_lowercase)
        
    def mount_keyOrder(self, key):
        order = []
        pos = []
        # Numera a ordem das letras do alfabeto
        for l in key:
            order.append(self.alfa.index(l))
            
        # Pega do mais próximo do inicio do alfabeto
        num_max = max(order)
        for i in range(num_max+1):
            if i in order:
                pos.append(order.index(i))
        
        return (order, pos)
    
    def encrypt(self, msg, key):
        msg = msg.replace(' ', '')
        msg = msg.lower()
        self.matrix = []
        line = []
        size = len(key)
        
        c = 0
        if not self.is_multiplo(msg, size):
            msg = self.fill(msg, size)
        msgList = list(msg)
        
        for l in msgList:
            if c < size - 1:
                line.append(l)
                c += 1
            else:
                line.append(l)
                self.matrix.append(line)
                c = 0
                line = []
        
        self.encrypted = []
        order, pos = self.mount_keyOrder(key)
        for p in pos:
            for row in self.matrix:
                self.encrypted.append(row[p])
        
        txtEncrypted = ""        
        for l in self.encrypted:
            txtEncrypted += l
        return txtEncrypted
        
    def decrypt(self, msg, key):
        sizeKey = len(key)
        sizeMsg = len(msg)
        r = sizeMsg / sizeKey
        
        # Cria uma matriz colunasXlinhas
        table = [ [0 for i in range(sizeKey)] for j in range(r) ]
        
        numLinhas = len(table)
        
        order, pos = self.mount_keyOrder(key)
        
        count_pos = r # numero de linhas é  
        for p in pos:
            # p numero da coluna 
            if count_pos > r:
                aux = count_pos - r
                partMsg = msg[aux:count_pos]
                count_pos = count_pos + r
            else:
                partMsg = msg[:count_pos]
                count_pos = count_pos + r
                
            
            for letra, linha in zip(partMsg, range(numLinhas)):
                table[linha][p] = letra
        
        
        txtDecrypted = ""
        for linha in table:
            for letra in linha:
                txtDecrypted += letra
        
        return txtDecrypted
    
    def is_multiplo(self, msg, size):
        """
        Se o resto da divizão for zero é multiplo 
        """
        return len(msg) % size == 0
    
    def fill(self, msg, size):
        """
        Verifica se é multiplo caso não seja, 
        adiciona uma letra aleatório ao fim da mensagem
        """
        while not self.is_multiplo(msg, size):
            msg += self.alfa[randint(0, len(self.alfa) - 1)]
        
        return msg
                 
                 
        
class CesarEncrypt(object):
    
    def __init__(self, key=3):
        self.alfa = list(string.ascii_lowercase)
        self.alfa.append(' ') # inserindo espaço na lista de caracteres
        self.key = key
        
    def separar(self, msg):
        # Guarda as chaves para as letras das mensagens
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

class RSAEncrypt(object):
    
    def __init__(self):
        self.alphabet = {
         'a':11,'b':12,'c':13,'d':14,'e':15,'f':16,'g':17,'h':18,'i':19,'j':20,
         'k':21,'l':22,'m':23,'n':24,'o':25,'p':26,'q':27,'r':28,'s':29,'t':30,
         'u':31,'v':32,'w':33,'x':34,'y':35,'z':36,' ':37 
         }
        
        self.translate = {
         11:'a',12:'b',13:'c',14:'d',15:'e',16:'f',17:'g',18:'h',19:'i',20:'j',
         21:'k',22:'l',23:'m',24:'n',25:'o',26:'p',27:'q',28:'r',29:'s',30:'t',
         31:'u',32:'v',33:'w',34:'x',35:'y',36:'z',37:' '}
        
    
    def gcd(self, a,b):
        """
        Retorna o divisor comum entre a e b pelo algoritmo euclidiano
        """
        while b:
            (a,b) = (b,a % b)
               
        return a
  
    def multiplicative_inverse(self, a, b):
        m = [0,1]               # determina d satisfazendo a condicao d*e=1 (mod n)
        while b:                
            q = a // b          
            (a,b) = (b,a % b)
            m.append(m[-2]-(q*m[-1]))
            m.remove(m[0])
        return m[-2]
  
  
    def iscoprime(self, a,b):
        """
        verifica se a e b sao coprimos
        """
        if self.gcd(a,b) == 1:
            return True
        else:
            return False  

  
    def generateRSAKeys(self, p, q):
        """
        Gera as chaves RSA publica e privada para os primos p e q
        """
    
        n = p*q                 # Calcula n = pq.
        self.n = n
                                
        Eu = (p-1) * (q-1)      # Calcula (pq) = (p - 1)(q - 1).
                                
        i = 3
        e = []
        while i < 25:
            if self.iscoprime(i,Eu): # Escolhe um inteiro tal que 1 < e < (pq),
                e.append(i)     # verificando se sao coprimos e adicionando os coprimos em uma lista
            i += 1              
     
        e = choice(e)           # Escolhe um valor aleatorio para e
     
        d = self.multiplicative_inverse(Eu,e)%Eu       # Calcula d 
        
        self.publicKey = (n,e)
        self.privateKey = (n,d)
                              
        return (n,e),(n,d)
    
    def getPublicKey(self):
        return self.publicKey
    
    def getPrivateKey(self):
        return self.privateKey
    
    def encrypt(self, input_text):
        """
        Encriptando letras com chave publica:
        """
        self.tuple_encrypted = []
        for x in input_text:
            # adiciona em uma lista cada valor de letra criptografada
            self.tuple_encrypted.append((long(self.alphabet[x]) ** self.publicKey[1]) % self.n) 
            
        encrypted = ''
        for y in  self.tuple_encrypted:
            encrypted = encrypted + str(y) + ' '
        
        return encrypted
    
    def decrypt(self):
        decrypted = ''
        for x in self.tuple_encrypted:
            decrypted = decrypted + self.translate[((long(x) ** self.privateKey[1]) % self.n)]
        return decrypted
        

if __name__ == "__main__":
    trans = TransposicaoEncrypt()
    cipher_msg = trans.encrypt("Vamos embora fomos descobertos, a casa caiu playboy... e nois na fita", "zera")
    print(cipher_msg)
    print(trans.decrypt(cipher_msg, "zera"))
    
#    print "Algoritmo de criptografia RSA"
#    p = long(raw_input("Valor de p (numero primo):"))
#    q = long(raw_input("Valor de q (numero primo):"))
#    
#    crypto = RSAEncrypt()
#    
#    print "gerando chave publica e privada...."
#    publickey, privatekey = crypto.generateRSAKeys(p, q)
#
#    print "Chave Publica (n, e) =", publickey
#    print "Chave Privada (n, d) =", privatekey
#    
#    n, e = publickey
#    n, d = privatekey
#    
#    input_text = raw_input("Entre com a palavra a ser criptografada:")
#    print(crypto.encrypt(input_text))
#    
#    print "Decriptando com chave privada:"
#    print(crypto.decrypt())
