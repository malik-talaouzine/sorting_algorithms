from GUI import *
import copy

ORDER = None


def bubble_sort(lst, bar_width):
    red = [0]
    orange = [0]
    green = [0]

    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            orange[0] = lst[j + 1]
            print_res(lst, red, orange, green, bar_width=bar_width)
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        green[0] = lst[j + 1]


def selection_sort(lst, bar_width):
    red = [0]
    orange = [0]
    green = [0]
    n = len(lst)
    min = 0
    for j in range(n):
        red[0] = lst[j]
        min = j
        for i in range(j+1, n):
            green[0] = lst[min]
            orange[0] = lst[i]
            print_res(lst, red, orange, green, bar_width=bar_width)
            if lst[min] > lst[i]:
                min = i
        lst[j], lst[min] = lst[min], lst[j]
        #if is_sorted(lst):
                #break


def insertion_sort(lst, bar_width):
    red = [0]
    orange = [0]
    green = [0]

    for step in range(1, len(lst)):
        key = lst[step]
        if step < len(lst) - 1:
            red[0] = lst[step + 1]
        j = step - 1
            
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j = j - 1
            orange[0] = lst[j]
            print_res(lst, red, orange, green, bar_width=bar_width)
        green[0] = 0
        lst[j + 1] = key
        green[0] = lst[j + 1]
        print_res(lst, red, orange, green, bar_width=bar_width)
        #time.sleep(0.01)


def merge_sort(l, first=False, bar_width=0):
    global LST
    green = [0]
    orange = [0, 0]
    red = [0]
    if first:
        LST = copy.deepcopy(l)

    if len(l) > 1:
        mid = len(l)//2
        L = l[:mid]
        R = l[mid:]

        for i, val in enumerate(LST):
            if val == l[0]:
                left = i

        merge_sort(L, bar_width=bar_width)
        merge_sort(R, bar_width=bar_width)
 
        i = j = k = 0


        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                orange[0] = L[i]
                #green[0] = R[j]
                l[k] = L[i]
                #LST[left + k] = l[k]
                i += 1
            else:
                #orange[0] = L[i]
                orange[1] = R[j]
                l[k] = R[j]
                #LST[left + k] = l[k]
                j += 1
            k += 1
            #time.sleep(0.01)
            print_res(LST, red, orange, green, counter=True, bar_width=bar_width)
 
        while i < len(L):
            orange[0] = L[i]
            l[k] = L[i]
            #LST[left + k] = l[k]
            i += 1
            k += 1
            #time.sleep(0.01)
            print_res(LST, red, orange, green, counter=True, bar_width=bar_width)
 
        while j < len(R):
            orange[1] = R[j]
            l[k] = R[j]
            #LST[left + k] = l[k]
            j += 1
            k += 1
            #time.sleep(0.01)
            print_res(LST, red, orange, green, counter=True, bar_width=bar_width)

        for i,val in enumerate(l):
            LST[left + i] = val
            #LST[left:left+len(l)] = l
            green[0] = val
            print_res(LST, red, orange, green, counter=True, bar_width=bar_width)
            #time.sleep(0.01)


def quick_sort(lst, low=0, high=0, bar_width=1):
    if low < high:
        pi = partition(lst, low, high, bar_width=bar_width)
        quick_sort(lst, low, pi - 1, bar_width=bar_width)
        quick_sort(lst, pi + 1, high, bar_width=bar_width)


def partition(lst, low, high, bar_width=1): # for quick_sort
    green = [0]
    orange = [0, 0]
    red = [0]

    pivot = lst[high]
    green[0] = pivot
    i = low - 1
    orange[0] = lst[i]
    red[0] = lst[i]

    for j in range(low, high):
        if lst[j] <= pivot:
            i = i + 1
            orange[0] = lst[i]
            print_res(lst, red, orange, green, bar_width=bar_width)
            (lst[i], lst[j]) = (lst[j], lst[i])
    (lst[i + 1], lst[high]) = (lst[high], lst[i + 1])
    return i + 1


def bogo_sort(lst, bar_width):
    while not is_sorted(lst, bar_width=bar_width):
        random.shuffle(lst)
        time.sleep(0.1)
        #print_res(lst, bar_width=bar_width)


def heapify(lst, N, i, bar_width):
    green = [0]
    orange = [0]
    red = [0]

    largest = i
    green[0] = lst[i]
    l = 2 * i + 1
    r = 2 * i + 2
 
    if l < N and lst[largest] < lst[l]:
        largest = l
        orange[0] = lst[largest]
        print_res(lst, red, orange, green, bar_width=bar_width)
 
    if r < N and lst[largest] < lst[r]:
        largest = r
        orange[0] = lst[largest]
        red[0] = lst[l]
        print_res(lst, red, orange, green, bar_width=bar_width)
 
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        red[0] = lst[i]
        orange[0] = lst[largest]
        print_res(lst, red, orange, green, bar_width=bar_width)
 
        heapify(lst, N, largest, bar_width)
 

def heap_sort(lst, bar_width):
    green = [0]
    orange = [0]
    red = [0]

    N = len(lst)
 
    for i in range(N//2 - 1, -1, -1):
        heapify(lst, N, i, bar_width)
 
    for i in range(N-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        green[0] = lst[i]
        red[0] = lst[0]
        print_res(lst, red, orange, green, bar_width=bar_width)
        heapify(lst, i, 0, bar_width)


def counting_sort(lst, bar_width):
    green = [0]
    orange = [0]
    red = [0]

    max_element = int(max(lst))
    orange[0] = max_element
    min_element = int(min(lst))
    red[0] = min_element
    range_of_elements = max_element - min_element + 1

    count_lst = [0 for _ in range(range_of_elements)]
    output_lst = [0 for _ in range(len(lst))]
  
    for i in range(0, len(lst)):
        count_lst[lst[i]-min_element] += 1
        red[0] = count_lst[lst[i]-min_element]
        print_res(lst, red, orange, green, bar_width=bar_width)
  
    for i in range(1, len(count_lst)):
        count_lst[i] += count_lst[i-1]
        orange[0] = count_lst[i]
        print_res(lst, red, orange, green, bar_width=bar_width)
  
    for i in range(len(lst)-1, -1, -1):
        output_lst[count_lst[lst[i] - min_element] - 1] = lst[i]
        count_lst[lst[i] - min_element] -= 1
        red[0] = output_lst[count_lst[lst[i] - min_element] - 1]
        orange[0] = count_lst[lst[i] - min_element]
        print_res(lst, red, orange, green, bar_width=bar_width)
  
    for i in range(0, len(lst)):
        lst[i] = output_lst[i]
        print_res(lst, red, orange, green, bar_width=bar_width)
  
    return lst


def countingSort(lst, exp1, bar_width):
    green = [0]
    orange = [0]
    red = [0]

 
    n = len(lst)
 
    # The output array elements that will have sorted arr
    output = [0] * (n)
 
    # initialize count array as 0
    count = [0] * (10)
 
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = lst[i] // exp1
        count[index % 10] += 1
 
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    # Build the output array
    i = n - 1
    while i >= 0:
        index = lst[i] // exp1
        output[count[index % 10] - 1] = lst[i]
        count[index % 10] -= 1
        i -= 1
 
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(lst)):
        lst[i] = output[i]
        green[0] = lst[i]
        print_res(lst, red, orange, green, bar_width=bar_width)
 
 
# Method to do Radix Sort
def radix_sort(lst, bar_width):
    green = [0]
    orange = [0]
    red = [0]

 
    # Find the maximum number to know number of digits
    max1 = max(lst)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp >= 1:
        countingSort(lst, exp, bar_width)
        exp *= 10


def shell_sort(lst, n, bar_width):
    green = [0]
    orange = [0]
    red = [0]

    gap=n//2
    while gap>0:
        j=gap
        while j<n:
            i=j-gap
              
            while i>=0:
                if lst[i+gap]>lst[i]:
                    green[0] = lst[i+gap]
                    red[0] = lst[i]
                    print_res(lst, red, orange, green, bar_width=bar_width)
                    break
                else:
                    lst[i+gap],lst[i]=lst[i],lst[i+gap]
                    green[0] = lst[i+gap]
                    red[0] = lst[i]
                    print_res(lst, red, orange, green, bar_width=bar_width)
  
                i=i-gap 
            j+=1
        gap=gap//2


def cocktail_sort(lst, bar_width):
    green = [0, 0]
    orange = [0]
    red = [0]

    n = len(lst)
    swapped = True
    start = 0
    end = n-1
    while (swapped == True):
        swapped = False
 
        for i in range(start, end):
            if (lst[i] > lst[i + 1]):
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                #orange[0] = lst[i + 1]
                red[0] = lst[i]
                print_res(lst, red, orange, green, bar_width=bar_width)
                swapped = True
 
        if (swapped == False):
            break
 
        swapped = False
        end = end-1
        green[0] = lst[end + 1]
 
        for i in range(end-1, start-1, -1):
            if (lst[i] > lst[i + 1]):
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                orange[0] = lst[i + 1]
                red[0] = lst[i]
                print_res(lst, red, orange, green, bar_width=bar_width)
                swapped = True
    
        green[0] = lst[end + 1]
        start = start + 1
        green[1] = lst[start - 1]


def compAndSwap(a, i, j, dire):
    if (dire==1 and a[i] > a[j]) or (dire==0 and a[i] < a[j]):
        a[i],a[j] = a[j],a[i]
 

def bitonicMerge(lst, low, cnt, dire, bar_width):
    green = [0, 0]
    orange = [0]
    red = [0]

    if cnt > 1:
        k = cnt//2
        for i in range(low , low+k):
            j = i+k
            if (dire==1 and lst[i] > lst[j]) or (dire==0 and lst[i] < lst[j]):
                lst[i],lst[j] = lst[j],lst[i]
                print_res(lst, red, orange, green, bar_width=bar_width)
        bitonicMerge(lst, low, k, dire, bar_width=bar_width)
        print_res(lst, red, orange, green, bar_width=bar_width)
        bitonicMerge(lst, low+k, k, dire, bar_width=bar_width)
        print_res(lst, red, orange, green, bar_width=bar_width)
 

def bitonic_sort(lst, low, cnt,dire, bar_width):
    green = [0, 0]
    orange = [0]
    red = [0]

    if cnt > 1:
          k = cnt//2
          bitonic_sort(lst, low, k, 1, bar_width=bar_width)
          print_res(lst, red, orange, green, bar_width=bar_width)
          bitonic_sort(lst, low+k, k, 0, bar_width=bar_width)
          print_res(lst, red, orange, green, bar_width=bar_width)
          bitonicMerge(lst, low, cnt, dire, bar_width=bar_width)
          print_res(lst, red, orange, green, bar_width=bar_width)
          print_res(lst, red, orange, green, bar_width=bar_width)


def start_bitonic_sort():
    lst, bar_width = initialize_list(250)
    bitonic_sort(lst, 0, len(lst), 1, bar_width)
    return lst


def cycle_sort(lst, bar_width):
    green = [0, 0]
    orange = [0]
    red = [0]

    writes = 0
    
    # Loop through the array to find cycles to rotate.
    for cycleStart in range(0, len(lst) - 1):
        item = lst[cycleStart]
        
        # Find where to put the item.
        pos = cycleStart
        for i in range(cycleStart + 1, len(lst)):
            if lst[i] < item:
                pos += 1
        
        # If the item is already there, this is not a cycle.
        if pos == cycleStart:
            continue
        
        # Otherwise, put the item there or right after any duplicates.
        while item == lst[pos]:
            pos += 1
        lst[pos], item = item, lst[pos]
        red[0] = lst[pos]
        orange[0] = item
        print_res(lst, red, orange, green, bar_width=bar_width)
        time.sleep(0.1)
        writes += 1
        
        # Rotate the rest of the cycle.
        while pos != cycleStart:
        
        # Find where to put the item.
            pos = cycleStart
            for i in range(cycleStart + 1, len(lst)):
                if lst[i] < item:
                    pos += 1
        
        # Put the item there or right after any duplicates.
            while item == lst[pos]:
                pos += 1
            lst[pos], item = item, lst[pos]
            red[0] = lst[pos]
            orange[0] = item
            print_res(lst, red, orange, green, bar_width=bar_width)
            time.sleep(0.1)
            writes += 1
    
    return writes


def is_sorted(lst, bar_width=0):
    #return all(lst[i] <= lst[i+1] for i in range(len(lst) - 1))
    green = []
    for i in range(len(lst) - 1):
        green.append(lst[i])
        print_res(lst, green=green, bar_width=bar_width)
        if lst[i] > lst[i + 1]: return False
    return True


def print_res(lst, red=[], orange=[], green=[], counter=False, bar_width=0):
    get_events()
    mouse, click = get_mouse_events()
    draw_window(mouse=mouse, click=click, lst=lst, red=red, orange=orange, green=green, counter=counter, bar_width=bar_width)
