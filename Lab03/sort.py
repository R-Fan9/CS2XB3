
# inplace quicksort
def quicksort_inplace(L):
    my_quicksort_inplace(L,0,len(L)-1)
    
def my_quicksort_inplace(L,low,high):
    if low<high:
        p_idx = partition(L,low,high)
        my_quicksort_inplace(L,low,p_idx-1)
        my_quicksort_inplace(L,p_idx+1,high)

def partition(L,low,high):
    index = low
    pivot = L[high]
    for i in range(low,high):
        if L[i] <=  pivot:
            L[index], L[i] = L[i], L[index]
            index +=1
    L[index], L[high] = L[high], L[index]
    return index

# two-pivot quicksort
def dual_quicksort(L):
    # return dual_pivot_quicksort(L)
    copy = dual_pivot_quicksort(L)
    for i in range(len(L)):
        L[i] = copy[i]

def dual_pivot_quicksort(L):
    if len(L) < 2:
        return L

    pivot1=min(L[0],L[1])
    pivot2=max(L[0],L[1])

    fst, scd, thd = [], [], []

    for num in L[2:]:
        if(num < pivot1):
            fst.append(num)
        elif(num < pivot2):
            scd.append(num)
        else:
            thd.append(num)
    return dual_pivot_quicksort(fst) + [pivot1] + dual_pivot_quicksort(scd) + [pivot2] + dual_pivot_quicksort(thd)

# three-pivot quicksort
def tri_quicksort(L):
    # return tri_pivot_quicksort(L)
    copy = tri_pivot_quicksort(L)
    for i in range(len(L)):
        L[i] = copy[i]
        
def tri_pivot_quicksort(L):
    if len(L) < 2:
        return L
    elif len(L) < 3:
        return [min(L), max(L)]
    else:
        ft = [L[0],L[1],L[2]]
        ft.sort()
        pivot1=ft[0]
        pivot2=ft[1]
        pivot3=ft[2]
        fst, scd, thd, fth = [], [], [], []

        for num in L[3:]:
            if(num < pivot1):
                fst.append(num)
            elif(num < pivot2):
                scd.append(num)
            elif(num < pivot3):
                thd.append(num)
            else:
                fth.append(num)

        return (tri_pivot_quicksort(fst) + [pivot1] + 
        tri_pivot_quicksort(scd) + [pivot2] + 
        tri_pivot_quicksort(thd) + [pivot3] +
        tri_pivot_quicksort(fth))

# auxiliary function for four-pivot quicksort
def middleOfThree(a, b, c) : 
    # Compare each three number to find  
    # middle number. Enter only if a > b 
    if a > b :  
        if (b > c): 
            return b 
        elif (a > c) : 
            return c 
        else : 
            return a  
    else: 
        # Decided a is not greater than b. 
        if (a > c) : 
            return a 
        elif (b > c) : 
            return c 
        else : 
            return b

# four-pivot quicksort
def quad_quicksort(L):
    # return quad_pivot_quicksort(L)
    copy = quad_pivot_quicksort(L)
    for i in range(len(L)):
        L[i] = copy[i]

def quad_pivot_quicksort(L):
    if len(L) < 2:
        return L
    elif len(L) < 3:
        return [min(L), max(L)]
    elif len(L) < 4:
        return [min(L), middleOfThree(L[0], L[1], L[2]), max(L)]
    else:
        ft = [L[0],L[1],L[2],L[3]]
        ft.sort()
        p1 = ft[0]
        p2 = ft[1]
        p3 = ft[2]
        p4 = ft[3]

        fst, scd, thd, fth, fiv = [], [], [], [], []

        for num in L[4:]:
            if(num < p1):
                fst.append(num)
            elif(num < p2):
                scd.append(num)
            elif(num < p3):
                thd.append(num)
            elif(num < p4):
                fth.append(num)
            else:
                fiv.append(num)
        
        return (quad_pivot_quicksort(fst) + [p1] + 
        quad_pivot_quicksort(scd) + [p2] + 
        quad_pivot_quicksort(thd) + [p3] +
        quad_pivot_quicksort(fth) + [p4] +
        quad_pivot_quicksort(fiv))

def final_sort(L):
    # return final_sort_hybrid(L)
    copy = final_sort_hybrid(L)
    for i in range(len(L)):
        L[i] = copy[i]

# hybrid of four-pivot quicksort and insertion sort
def final_sort_hybrid(L):
    if len(L) < 2:
        return L
    elif len(L) < 3:
        return [min(L), max(L)]
    elif len(L) < 4:
        return [min(L), middleOfThree(L[0], L[1], L[2]), max(L)]
    elif len(L) < 6:
        insertion_sort(L)
    else:
        ft = [L[0],L[1],L[2],L[3]]
        ft.sort()
        p1 = ft[0]
        p2 = ft[1]
        p3 = ft[2]
        p4 = ft[3]

        fst, scd, thd, fth, fiv = [], [], [], [], []

        for num in L[4:]:
            if(num < p1):
                fst.append(num)
            elif(num < p2):
                scd.append(num)
            elif(num < p3):
                thd.append(num)
            elif(num < p4):
                fth.append(num)
            else:
                fiv.append(num)
        return (quad_pivot_quicksort(fst) + [p1] + 
        quad_pivot_quicksort(scd) + [p2] + 
        quad_pivot_quicksort(thd) + [p3] +
        quad_pivot_quicksort(fth) + [p4] +
        quad_pivot_quicksort(fiv))