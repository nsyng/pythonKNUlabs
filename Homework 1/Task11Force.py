"""

    1.1. Обчислити силу притягання F між двома тілами, що мають маси
    m1,m2 , на відстані r

"""

m1 = float(input('m1: ')); 
m2 = float(input('m2: '));
r = float(input('r: '));

y = 6.673*10**-11;
result = y*m1*m2/(r**2); 

print('Result: ', result)
