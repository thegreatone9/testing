#watch navinreddy's python bubble sort video
#bubble sort works by swapping constantly, beg to end of list. 
#the swapping pushes the biggest element to the end in the first iter.
#in the 2nd swap, the 2nd biggest element is pushed to the 2nd last. 

def swap(li_st, a, b):
    temp = li_st[a]
    li_st[a] = li_st[b]
    li_st[b] = temp
    return li_st

def bub_sort_dec_order(li_st): 
    for i in range(len(li_st)):    
        for i in range(len(li_st)-1):
            if li_st[i] < li_st[i+1]:
                li_st = swap(li_st, i, i+1)
    return li_st


def bub_sort(li_st): 
    for i in range(len(li_st)):    
        for j in range(len(li_st)-1-i): #the i here was added at the end...after noticing that the largest value in the list gets pushed to the rightend after every i iteration, so no need to to check it. 
            if li_st[j] > li_st[j+1]:
                li_st = swap(li_st, j, j+1)
    return li_st

print("in asc order: {}".format(bub_sort([5,3,8,6,7,-6, 2, 0, 100])))
print("in dec order: {}".format(bub_sort_dec_order([5,3,8,6,7,-6, 2, 0, 100])))
