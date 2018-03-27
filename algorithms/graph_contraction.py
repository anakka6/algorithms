#!usr//bin/python2.6
import random

with open('/home/anakka/Desktop/Algorithms/kargerMinCut.txt','r') as file:
	A = file.readlines()

for i in range(len(A)):
	A[i] = str.split(A[i])
	for j in range(len(A[i])):
		A[i][j] = int(A[i][j])


def pick_random_edge(A):
	secure_random = random.SystemRandom()
	B = secure_random.choice(A)
	edge_head  = B[0]
	edge_tail = secure_random.choice(B[1:])
	return edge_head,edge_tail

def find_index_of_edge_tail(A,edge_tail):
	for index in range(len(A)):
		if A[index][0] == edge_tail:
			return index

def remove_duplicates(B):
	final_list = []
	for num in B:
		if num not in final_list:
			final_list.append(num)
	return final_list


def contraction(A,edge_head,edge_tail):
	index = find_index_of_edge_tail(A,edge_tail)
	B = A[index][1:]
	B = remove_duplicates(B)
	for element in B:
		element_index = find_index_of_edge_tail(A,element)
		for i in range(len(A[element_index])):
			if A[element_index][i] == edge_tail:
				A[element_index][i] = edge_head
		if element == edge_head:
			A[element_index] = A[element_index] + A[index]
			A[element_index].remove(edge_tail)
		m = 0
		for i in range(len(A[element_index])-1):
			m = m+1
			if A[element_index][m] == A[element_index][0]:
				A[element_index].pop(m)
				m = m-1
	A.pop(index)


while len(A)>2:
	edge_head,edge_tail = pick_random_edge(A)
	contraction(A,edge_head,edge_tail)

print "Size of the cut:",len(A[0])-1


























# def element_in_a_list_of_lists(A,m):
# 	for i in range(len(A)):
# 		for j in range(len(A[i])):
# 			if A[i][j] ==m:
# 				return True
# 	return False

# def get_the_position_of_element_in_a_list(A,m):
# 	for i in range(len(A)):
# 		for j in range(len(A[i])):
# 			if A[i][j] ==m:
# 				return i

# def merge_two_lists(inputList,edge_head,edge_tail):
# 	head_position = get_the_position_of_element_in_a_list(inputList,edge_head)
# 	tail_position = get_the_position_of_element_in_a_list(inputList,edge_tail)
# 	inputList[head_position] = inputList[head_position]+inputList[tail_position]
# 	inputList.pop(tail_position)
# 	return inputList

# def get_cut_list(A):
# 	cut_list=[]
# 	while len(A)>2:
# 		edge_head,edge_tail = pick_random_edge(A)
# 		#print "edge_head:",edge_head,"edge_tail:",edge_tail
# 		if element_in_a_list_of_lists(cut_list,edge_head) == False and element_in_a_list_of_lists(cut_list,edge_tail) == False:
# 			cut_list.append([])
# 			cut_list[-1].append(edge_head)
# 			cut_list[-1].append(edge_tail)
# 		elif element_in_a_list_of_lists(cut_list,edge_head) == True and element_in_a_list_of_lists(cut_list,edge_tail) == False:
# 			head_position = get_the_position_of_element_in_a_list(cut_list,edge_head)
# 			cut_list[head_position].append(edge_tail)
# 		elif element_in_a_list_of_lists(cut_list,edge_head) == True and element_in_a_list_of_lists(cut_list,edge_tail) == True:
# 			cut_list = merge_two_lists(cut_list,edge_head,edge_tail)
# 		#modify_graph_after_contraction(A,edge_tail)
# 		contraction(A,edge_head,edge_tail)
# 	return cut_list
# 	#print "A:",A
# 	#print "cut_list:",cut_list

