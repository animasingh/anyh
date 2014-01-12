# naive matrix multiplication 

A = [ [1,0,-2],[0,3,-1]];
B = [ [0,3],[-2,-1],[0,4]];

M = len(A);
N = len(A[0]); 
K = len(B[0]);

C=[]
 # C = M X K matrix
for i in range(0,M):
    C.append([0]*K);
    for j in range(0,K):     
        C[i][j]=0;
        for h in range(0,N):           
            C[i][j]= C[i][j] + A[i][h]*B[h][j];
        print i, j, C[i][j], C
        