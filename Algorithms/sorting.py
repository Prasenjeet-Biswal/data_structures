import os, sys, re
import random

def bubble_sort(arr):
	print("bubble sort")
	if arr==None or len(arr)<2:
		return
	changes=1
	for i in range(len(arr)):
		if changes==0:
			return
		changes=0
		for j in range(len(arr)-i-1):
			if arr[j] > arr[j+1]:
				t = arr[j]
				arr[j] = arr[j+1]
				arr[j+1]=t
				changes=1


def insertion_sort(arr):
	print("insertion sort")
	if arr==None or len(arr)<2:
		return
	for i in range(len(arr)):
		j=i-1
		t = arr[i]
		while j>=0 and t<arr[j]:
			arr[j+1]=arr[j]
			j-=1
		arr[j+1]=t
	return

## only when the array values are in a range.
def counting_sort(arr, arr_range, min):
	print("counting sort")
	count = [0]*arr_range
	for val in arr:
		count[val-min]+=1
	for i in range(1, len(count)):
		count[i] = count[i]+count[i-1]

	print(count)
	result = [0]*len(arr)

	for val in arr:
		result[count[val-min]-1]=val
		count[val-min]-=1
	return result

def get_min(arr, start, max_val):
	min_val = max_val
	min_index=-1
	for i, val in enumerate(arr[start:]):
		if val < min_val:
			min_val=val
			min_index=i+start
	return min_index

def selection_sort(arr, max_val):
	print("selection sort")
	for i in range(len(arr)-1):
		index = get_min(arr, i, max_val)
		t = arr[index]
		arr[index]=arr[i]
		arr[i]=t

def partition(arr, start, end, randomized=False):
	if randomized:
		k=random.randint(start, end)
		t1 = arr[k]
		arr[k]=arr[end]
		arr[end]=t1
	k=end
	t = arr[k]
	pointer = start-1
	for i in range(start, end):
		if arr[i]<t:
			pointer+=1
			t1=arr[pointer]
			arr[pointer]=arr[i]
			arr[i]=t1
	pointer+=1
	t1 = arr[pointer]
	arr[pointer]=t
	arr[k]=t1
	return pointer

def quick_sort(arr, start, end):
	if start>=end:
		return
	x = partition(arr, start, end)
	quick_sort(arr, start, x-1)
	quick_sort(arr, x+1, end)	

def randomized_quick_sort(arr, start, end):
	if start>=end:
		return
	x = partition(arr, start, end, True)
	randomized_quick_sort(arr, start, x-1)
	randomized_quick_sort(arr, x+1, end)

def heap_sort():
	pass

def radix_sort():
	pass

def bucket_sort():
	pass

def shell_sort():
	pass
	
def tim_sort():
	pass

def space_efficient_merge():
	pass

def merge(arr, first, second, end):
	mid=second-1
	pointer=first
	merged_array = []
	while first <=mid and second<=end:
		if arr[first]<=arr[second]:
			merged_array.append(arr[first])
			first+=1
		else:
			merged_array.append(arr[second])
			second+=1
	while first<=mid:
		merged_array.append(arr[first])
		first+=1
	while second<=end:
		merged_array.append(arr[second])
		second+=1
	for val in merged_array:
		arr[pointer]=val
		pointer+=1
	del(merged_array)

def merge_sort_indices(arr, start, end):
	if start==end:
		return
	mid = start + (end-start)//2
	merge_sort_indices(arr, start, mid)
	merge_sort_indices(arr, mid+1, end)
	merge(arr, start, mid+1, end) # O(n)
	

def merge_sort(arr):
	print("merge sort")
	merge_sort_indices(arr, 0, len(arr)-1)


arr = [2,4,6,1,7,9,4,4,2,1,3,5,7,7,7,7,7,7,8,8,8,8,2,3,4,3,2,5,6,3,8,9]
bubble_sort(arr)
print(arr)
# insertion_sort(arr)
# merge_sort(arr)
# result = counting_sort(arr, max(arr)-min(arr)+1, min(arr))
#selection_sort(arr, 100)
arr = [2,4,6,1,7,9,4,4,2,1,3,5,7,7,7,7,7,7,8,8,8,8,2,3,4,3,2,5,6,3,8,9]
quick_sort(arr, 0, len(arr)-1)
print(arr)
arr = [2,4,6,1,7,9,4,4,2,1,3,5,7,7,7,7,7,7,8,8,8,8,2,3,4,3,2,5,6,3,8,9]
randomized_quick_sort(arr, 0, len(arr)-1)
print(arr)


	


