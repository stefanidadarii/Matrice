M = [[2,44,21,13,24], 
    [34,5,-9,10,1], 
    [15,66,78,94,-6], 
    [77,4,11,19,87], 
    [33,56,444,80,32]]
print('Suma primului rand este', sum(M[0]))
print('Suma randului al doilea este', sum(M[1]))
print('Suma randului al treile este', sum(M[2]))
print('Suma randulului al patrulea este', sum(M[3]))
print('Suma randului al cincelea este', sum(M[4]))
coloana1=0
coloana2=0
coloana3=0
coloana4=0
coloana5=0
for i in M:
    coloana1+=i[0]
    coloana2+=i[1]
    coloana3+=i[2]
    coloana4+=i[3]
    coloana5+=i[4]
print('Suma primei coloane este', coloana1)
print('Suma coloanei a doua este', coloana2)
print('Suma coloanei a treia este', coloana3)
print('Suma coloanei a patra este', coloana4)
print('Suma coloanei a cincea este', coloana5)
dp = M[0][0]+M[1][1]+M[2][2]+M[3][3]+M[4][4]
ds = M[0][4]+M[1][3]+M[2][2]+M[3][1]+M[4][0]
print('Suma diagonalei principale este', dp, 'iar suma diagonalei secundare este', ds)