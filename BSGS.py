from math import floor, sqrt
def pow_mod(x, y, z):
    p = 1     # puterea este, initial, 1
    while y:      #dupa pasul k, y=2^(n-k)*a_n+...+a_k, p=x^(2^(k-1)*a_{k-1}+...+a_0), iar x devine x^(2^k)
      if y & 1:    #daca a_k=1, x^(2^k) participa la inmultire
        p = (p * x) % z      #p=x^(2^(k-1)*a_{k-1}+...+a_0)*x^(2^k)=x^(2^k+2^(k-1)*a_{k-1}+...+a_0)
      y >>= 1     #indiferent daca x^(2^k) participa sau nu la inmultire, y devine 2^(n-k-1)*a_n+...+a_{k+1}
      x = x * x % z        #x devine  x^(2^(k+1))
    return p
    
def babystepgiantstep(g, y, p):
  t = floor(sqrt(p - 1))    
  hashtable = {(pow_mod(g, i, p)*y)%p: i for i in range(t+1)}
  print(hashtable.keys())
  print(hashtable.values())
  h = pow_mod(g, t, p)
  q = floor((p-1)/t)
  for j in range(q+1):
        k = pow_mod(h, j, p)
        if k in hashtable:
          print(j*t-hashtable[k])
          return (j*t-hashtable[k])
