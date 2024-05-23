import numpy as np
from ..utils import ToLeft
import matplotlib.pyplot as plt
# import bisect
def Create_DT_incremental(P):
	return Create_DT_incremental_Sorted(P[np.lexsort((P[:, 1], P[:, 0]))])
	
def Create_DT_incremental_Sorted(P):
	l=len(P)
	if l<3 or P[-1][0]==P[0][0]:
		print("Insufficient points to construct Delaunay diagram.")
		return None,None
		
	i=2
	if P[0][0]==P[1][0]:
		while P[0][0]==P[i][0]:
			i+=1
			
		L_ch_i=[0,i-1,i]
		i_xmax=2
	
	else:
		while i<l:
			LogFlag=ToLeft(P[0],P[1],P[i])
			if LogFlag==0:
				i+=1
				continue
			elif LogFlag<0:
				L_ch_i=[0,i,i-1]
				i_xmax=1
				break
			else:
				L_ch_i=[0,i-1,i]
				i_xmax=2
				break
			
		else:
			print("Insufficient points to construct Delaunay diagram.")
			return None,None
		
	#返回线段的Delaunay对应点
	#某一线段，用点索引对来表示
	D_tri={(0,i):[1],(i,0):[1],(0,1):[i],(1,0):[i],(i-1,i):[i-2],(i,i-1):[i-2]}
	# D_tri[i,i-1]=[i1]
	for i1 in range(1,i-1):
		D_tri[i1,i1+1]=[i]
		D_tri[i1+1,i1]=[i]
		D_tri[i1,i]=[i1-1,i1+1]
		D_tri[i,i1]=[i1-1,i1+1]
		
	i+=1
	while i<l:
		L_ch_i,i_xmax=add_point_i(P,L_ch_i,D_tri,i_xmax,i)
		
		i+=1
		
	return L_ch_i,D_tri

"""
用集合来实现记录点
"""
	
def add_point_i(P,A,D,a1,i_p):
	p=P[i_p]
	if ToLeft(p,P[A[a1-1]],P[A[a1]])>=0:
		a2=a1-len(A)+1
	else:
		a2=a1-len(A)
		while ToLeft(p,P[A[a1-1]],P[A[a1]])<0:
			a1-=1
			
	while ToLeft(p,P[A[a2]],P[A[a2+1]])<0:
		a2+=1
			
	b1=a1-len(A)
	b2=a2
	L_i=[A[a1]]
	N=[]
	# print("b1",b1)
	# print("b2",b2)
	while b2>b1:
		N.append(A[b2])
		b2-=1
		
	# find_border(P,S,D,N,L_i,i_b,i_p)
	find_border_while(P,D,N,L_i,A[a1],i_p)
	add_edge(D,L_i,i_p)
	if a2==0:
		return A[:a1+1]+[i_p],a1+1
	return A[:a1+1]+[i_p]+A[a2:],a1+1

#N是一个列表，实际使用类似栈，记录着每个要进行in_circle操作的点的P中索引
#L_i返回，原始集合P[:i_p]应该与p相连的点的P中索引
def find_border_rec(P,D,N,L_i,i_b,i_p):
	if not N or (i_b,N[-1]) not in D:
		return
	i_d=D[i_b,N[-1]][0]
	if in_circle_bcd(P,i_p,i_b,N[-1],i_d):
		del D[i_b,N[-1]]
		del D[N[-1],i_b]
		N.append(i_d)
		find_border(P,S,D,N,L_i,i_b,i_p)
		
	else:
		L_i.append(i_b)
		find_border(P,D,N,L_i,N.pop(),i_p)
	
def find_border_while(P,D,N,L_i,i_b,i_p):
	while N:
		if (i_b,N[-1]) in D and D[i_b,N[-1]]:
			i_d=D[i_b,N[-1]][0]
			if in_circle_bcd(P,i_p,i_b,N[-1],i_d):
				del D[i_b,N[-1]]
				del D[N[-1],i_b]
				D[i_d,i_b].remove(N[-1])
				D[i_b,i_d].remove(N[-1])
				D[i_d,N[-1]].remove(i_b)
				D[N[-1],i_d].remove(i_b)
				N.append(i_d)
				continue
			
		i_b=N.pop()
		L_i.append(i_b)
	

def add_edge(D,L,i_p):
	l=len(L)
	D[L[0],L[1]].append(i_p)
	D[L[1],L[0]].append(i_p)
	D[L[0],i_p]=[L[1]]
	D[i_p,L[0]]=[L[1]]
	for i in range(1,l-1):
		D[L[i],L[i+1]].append(i_p)
		D[L[i+1],L[i]].append(i_p)
		D[L[i],i_p]=[L[i-1],L[i+1]]
		D[i_p,L[i]]=[L[i-1],L[i+1]]
		
	#i==l-2
	D[L[l-1],i_p]=[L[l-2]]
	D[i_p,L[l-1]]=[L[l-2]]
	
	
def Sorted_Increment_w_d(A,p,a1):
	if ToLeft(p,A[a1-1],A[a1])>0:
		a2=a1-len(A)+1
		
	else:
		a2=a1-len(A)
		while ToLeft(p,A[a1-1],A[a1])<=0:
			a1-=1
			
	while ToLeft(p,A[a2],A[a2+1])<=0:
		a2+=1
			
	if a2==0:
		return A[:a1+1]+[p],a1+1
	return A[:a1+1]+[p]+A[a2:],a1+1
	
def in_circle_bcd(P,i_a,i_b,i_c,i_d):
	ab=P[i_b]-P[i_a]
	ac=P[i_c]-P[i_a]
	db=P[i_b]-P[i_d]
	dc=P[i_c]-P[i_d]
	
	return np.dot(ab,ac)*np.linalg.norm(db)*np.linalg.norm(dc)+np.dot(db,dc)*np.linalg.norm(ab)*np.linalg.norm(ac)<0
	