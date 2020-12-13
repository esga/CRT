def productlist(l): #ritorna produttoria di una lista
    N=1
    for i in l:
        N*=i
    return N


def CRT(b,n,s=False): #teorema cinese del resto
    '''solution of a system: x=b[i] (mod n[1])
       s print variable, if ==True, the function prints the system and the solution '''
    N=productlist(n)
    Ni=[]
    for i in range(len(n)):
        temp_list=n[:]
        temp_list[i]=1
        Ni.append(productlist(temp_list))
    y=[0]*len(b)
    for i in range(len(b)):
        searchingy=True
        temp_y=0
        while searchingy and temp_y<=n[i]:
            if (temp_y*Ni[i])%n[i]==1:
                searchingy=False
                y[i]=temp_y
            else:
                temp_y+=1
    x0=sum([b[i]*Ni[i]*y[i] for i in range(len(n))])
    x=x0%N
    if s:
        for i in range(len(b)):
            print("x = %d (mod %d)"%(b[i],n[i]))
        print("\nSolution:\nx = %d + %dk"%(x,N))
    return [x, N]

def example():
    b=[2,0,4]
    n=[5,4,7]
    solution= CRT(b,n,True)
