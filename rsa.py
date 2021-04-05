import sys
import random as rand



class RSA:
    def __init__(self):
        # print("hel")
        print(self.rsaList())
        
        self.p,self.q = map(int,input().split())
        self.N=self.p*self.q
        self.N1=(self.p-1)*(self.q-1)
        print(self.genElist(self.N1))
        print("e")
        self.e=int(input())
        print(self.genDlist(self.e,self.N1))
        print("d")
        self.d=int(input())
        print("加密:")
        self.m=int(input())
        print(self.encrypt(self.m,self.e,self.N))
         
        print("解密:")
        self.c=int(input())
        print(self.decrypt(self.c,self.d,self.N))



    def encrypt(self,m,e,n):
        
       x=m**e
       x1=x%n
       return x1
    def decrypt(self,c,d,n):
        x=c**d
        x1=x%n
        return x1

    def rsaList(self):
        data = []
        while len(data)<5:
            y= rand.randint(2,1000)
            if self.isPrime(y):
                data.append(y)
            
        return data

    def isPrime(self,x):
        i=2
        flag=True
        while i<(x/2):
            if(x%i==0):
                flag=False
                break
            i=i+1
        
        return flag
        

    def iswho(self,n1,e):
        i=2
        flag=True
        while i<=n1:
            if(n1%i==0):
                if(e%i==0):
                    flag=False
                    break
            i=i+1
        return flag          


    def genElist(self,x):
        data =[]    
        while len(data)<5:
            y= rand.randint(2,1000)
            if self.iswho(y,x):
                data.append(y)
            
        return data

    def genDlist(self,e,n1):
        data =[]    
        i=2
        while len(data)<5:
            y= i
            d=y*e
            if d%n1==1:
                data.append(y)
            i=i+1    
            
        return data    



if __name__ == "__main__":
    rsa=RSA()
   
      
    
