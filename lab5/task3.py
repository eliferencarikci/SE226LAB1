total=0 #global variable

def S(n):
    """
    Computing the altenating series:
     S_n = 1 - 1/2 + 1/3 - 1/4 + ... + (-1)^(n+1)/n

    Recursive logic:
    - Function calls itself with n-1 until n reaches 0 (base case).
    - At each step, it adds the current term to the global variable 'total'.

    Sign handling:
    - If n is odd → term is positive
    - If n is even → term is negative
    - This is achieved using (-1)^(n+1)
    
    Note:
    - The function does NOT return anything.
    - Result is stored in global variable 'total'.
    """
    global total

    if n==0:
        return
    
    total += ((-1)**(n+1))/n
    S(n-1)

  
  #main
    n=int(input("Enter n: "))
    S(n)
    print("Result:",total)