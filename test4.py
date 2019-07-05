import numpy as np 
# A = np.arange(24,12,-1).reshape((3,4))
# B = np.linspace(1,10,20)
# print(A)
# #print(B)

# '''print("{};{};{}".format(np.diff(A),np.cumsum(A),np.median(A)))
# j,k=np.nonzero(A)
# print((A.T).dot(A))
# print(A.T)


# x = np.array([[1,2,3],[4,5,6]])
# y = np.array([[1,2],[3,4],[5,6]])
# print('\n{}\n\n{}\n\n{}'.format(x,y,x.dot(y)))'''

# print(np.clip(A,20,9))
# print(np.mean(A,axis=0))
# for s in A.T:
#     print()
#     print(s)
# for s in A.flat:
#     print()
#     print(s)
A = np.array([1,1,1])[:,np.newaxis]
B = np.array([2,2,2])[:,np.newaxis]
print(np.vstack((A,B)))
print(A[np.newaxis,:].shape)
# print('\n{}\n\n\n{}\n\n\n{}\n\n\n{}\t'.format(A[np.newaxis,:],np.vstack(A),A[:,np.newaxis],np.hstack(A)))
print(np.concatenate((A,B),axis=1))