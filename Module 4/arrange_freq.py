A=(list(input().strip().split()))
A=A.sort()
A=set(A)
"""B={}
for i in A:
    B[i]=A.count(i)
for i in range(1,len(A)):
    for j in range(0,i):
        if B[A[i]]>B[A[j]]:
            A[i],A[j]=A[j],A[i]
        elif B[A[i]]==B[A[j]]:
            if A[i]>=A[j]:
                A[i],A[j]=A[j],A[i]"""
print(A)
