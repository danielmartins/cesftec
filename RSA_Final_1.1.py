def gcd(a,b):
    "Retorna o divisor comum entre a e b pelo algoritmo euclidiano"
    while b:
        (a,b) = (b,a % b)   
    return a
  
def multiplicative_inverse(a, b):
    m = [0,1]               # determina d satisfazendo a condicao d*e=1 (mod n)
    while b:                
        q = a // b          
        (a,b) = (b,a % b)
        m.append(m[-2]-(q*m[-1]))
        m.remove(m[0])
    return m[-2]
  
  
def iscoprime(a,b):
    "verifica se a e b sao coprimos"
    if gcd(a,b) == 1:
        return True
    else:
        return False  

  
def generateRSAKeys(p, q):
    "Gera as chaves RSA publica e privada para os primos p e q"

    n = p*q                 # Calcula n = pq.
                            
    Eu = (p-1) * (q-1)      # Calcula (pq) = (p - 1)(q - 1).
                            
    i = 3
    e = []
    while i < 25:
        if iscoprime(i,Eu): # Escolhe um inteiro tal que 1 < e < (pq),
            e.append(i)     # verificando se sao coprimos e adicionando os coprimos em uma lista
        i += 1              
 
    e = choice(e)           # Escolhe um valor aleatorio para e
 
    d = multiplicative_inverse(Eu,e)%Eu       # Calcula d 
                          
    return (n,e),(n,d)    

if __name__ == "__main__":

  alphabet = {
         'a':11,'b':12,'c':13,'d':14,'e':15,'f':16,'g':17,'h':18,'i':19,'j':20,
         'k':21,'l':22,'m':23,'n':24,'o':25,'p':26,'q':27,'r':28,'s':29,'t':30,
         'u':31,'v':32,'w':33,'x':34,'y':35,'z':36,' ':37 
         }

  translate = {
         11:'a',12:'b',13:'c',14:'d',15:'e',16:'f',17:'g',18:'h',19:'i',20:'j',
         21:'k',22:'l',23:'m',24:'n',25:'o',26:'p',27:'q',28:'r',29:'s',30:'t',
         31:'u',32:'v',33:'w',34:'x',35:'y',36:'z',37:' '}  

  print "Algoritmo de criptografia RSA"
  p = long(raw_input("Valor de p (numero primo):"))
  q = long(raw_input("Valor de q (numero primo):"))

  print "gerando chave publica e privada...."
  (publickey, privatekey) = generateRSAKeys(p, q)

  print "Chave Publica (n, e) =", publickey
  print "Chave Privada (n, d) =", privatekey

  n, e = publickey
  n, d = privatekey

  input_text = raw_input("Entre com a palavra a ser criptografada:")
  tuple_encrypted = []

  print "Encriptando letras com chave publica:"  
  for x in input_text:   
      tuple_encrypted.append((long(alphabet[x]) ** e) % n) # adiciona em uma lista cada valor de letra criptografada

  encrypted = ''
  for y in tuple_encrypted:
      encrypted = encrypted + str(y) + ' '

  print encrypted

  print "Decriptando com chave privada:"
  
  decrypted = ''
  for x in tuple_encrypted:
      decrypted = decrypted + translate[((long(x) ** d) % n)]
     
  print decrypted        


