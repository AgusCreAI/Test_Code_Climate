def apilarP(n): 
    ''' 
    Este predicado determina si es posible apilar n latas de forma exacta 
    sin que sobre ninguna. 
    Parameters 
    ---------- 
    n: int 
        Número de latas a apilar. 
  
    Returns 
    ------- 
    decision: Bool 
        True: se pueden apilar. 
        False: no se pueden apilar. 
        
    ''' 
    k= 1
    total_latas= 0
    if n== 0 :
        print('0 latas no se pueden apilar')
    
    while n>total_latas:
        total_latas= total_latas+k
        if total_latas==n :
            print(f'{n} latas se pueden apilar en {k} pisos')
            return True
            
        k= k+ 1

        if total_latas>n:
            sobran= total_latas-n
            print(f'{n} latas no se pueden apilar, habría {k-1} pisos '
                  f'y sobrarían {sobran} latas')
            return False


def apilarP(n): 
    ''' 
    Este predicado determina si es posible apilar n latas de forma exacta 
    sin que sobre ninguna. 
    Parameters 
    ---------- 
    n: int 
        Número de latas a apilar. 
  
    Returns 
    ------- 
    decision: Bool 
        True: se pueden apilar. 
        False: no se pueden apilar. 
        
    ''' 
    suma = 0
    i = 1
    
    while suma < n:
        suma += i
        i += 1
    
    return suma == n