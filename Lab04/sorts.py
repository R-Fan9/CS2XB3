import random

def mergesort_three_way(L):
    
    if len(L) <= 1:
        return
    
    if len(L) == 2:
        if L[0] > L[1]:
            L[0], L[1] = L[1], L[0]
        return L

    third_1 = len(L)//3
    third_2 = len(L)//3 * 2
    left, middle, right = L[:third_1], L[third_1:third_2],L[third_2:]

    #Mergesort core
    mergesort_three_way(left)
    mergesort_three_way(middle)
    mergesort_three_way(right)
    temp = merge_three_way(left, middle, right)

    #Copy the sorted list to L
    for i in range(len(temp)):
        L[i] = temp[i]


def merge_three_way(left, middle, right):
    L = []
    i = j = k = 0
    while i < len(left) or k < len(middle) or j < len(right):
        if i >= len(left):
            if k >= len(middle):
                L.append(right[j])
                j += 1
            elif j >= len(right):
                L.append(middle[k])
                k += 1
            else:
                if middle[k] <= right[j]:
                    L.append(middle[k])
                    k += 1
                else:
                    L.append(right[j])
                    j+=1           
        elif j >= len(right):
            if k >= len(middle):
                L.append(left[i])
                i += 1
            else:
                if middle[k] <= left[i]:
                    L.append(middle[k])
                    k += 1
                else:
                    L.append(left[i])
                    i+=1   
        elif k >= len(middle):
            if right[j] <= left[i]:
                L.append(right[j])
                j += 1
            else:
                L.append(left[i])
                i+=1      
        else:
            if left[i] <= right[j] and left[i] <= middle[k]:
                L.append(left[i])
                i += 1
            elif right[j] <= left[i] and right[j] <= middle[k]:
                L.append(right[j])
                j+=1
            else:
                L.append(middle[k])
                k+=1
    return L
