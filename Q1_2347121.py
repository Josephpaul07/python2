# Write a PYTHON script with List comprehension for the following
# • Is the given list divisible by 3 or NOT?
# • Square of even numbers in a list
# • Sum of digits of all EVEN numbers in a list
# • Remove duplicate numbers in a list

list1= [1,2,3,8,6,5,12]
for x in list1:
    if x%3==0:
        print("divisible by 3:",x)
 
# • Square of even numbers in a list
list2= [1,2,3,8,6,5,12]
print("square of even number:")
for x in list2:
    if x%2==0:
         print(x**2)
        
 # • Sum of digits of all EVEN numbers in a list
list= [1,2,3,8,6,5,12]
print("sum of even number:")
sum=0
for x in list:
    if x%2==0:
        sum+=x
    print(sum)
# • Remove duplicate numbers in a list
list=[1,2,3,8,6,5,12,5,2,3,8]  
print("duplicate number",list)
result=[*set(list)] 
print("list after duplicating",result) 

#Create a dictionary to store the details of your company employees (name as key and
# birthdate as value).
staff={ 
       "ryan":"may 7",
       "sree":"april 3",
       "kurin":"jun 5"   
}

def birthdate(name):
    print(staff[name])

birthdate('ryan')
    
        

    
            
 
     
    
    
