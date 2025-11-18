

def prime_checker(n)->bool:
    if n==2: return True
    if n<2 or n%2==0: return False
    for i in range(3,int(n/2),2):
        if n%i==0:
            return False
    return True