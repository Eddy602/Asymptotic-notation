#constant time - time does not chnge
# def display(n):
#     iterations=0
#     print("the number given is" ,n)   
#     iterations+=1
#     print("the number of iterations is",iterations) 

# display(10)    
# display(1000)
 #linear time
# print("LINEAR TIME COMPLEXITY")
# def linear(n):
#     iterations=0
#     for x in range(1,n+1):
#         iterations+=1
#     print("when n is",n,"the total number of itrations required is",iterations)
# linear(10) 
# linear(1000)       
 #quadratic time
print("QUADRATIC TIME")
def quad(n):
    iterations=0
    for i in range(0,n):
        for j in range(0,n):
            print('@',end='')
            iterations+=1
        print('')   
    print("when n is",n,"the total number of itrations is",iterations)  
quad(5)
quad(7)    