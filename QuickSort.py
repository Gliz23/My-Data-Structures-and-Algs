def quicksort(array):
    #Place your array in square brackets seperated by commas.
    #The pivot might just be the last item in the array.

    if len(array) < 2:
        return array
    else:
        pivot_index = len(array) - 1
        pivot = array[pivot_index]
        i = -1
        
        #We iterate j over the numbers (0 to n-1) where n = len of array. This will happen n times.
        for j in range(len(array) - 1): 
            # if the first element in the array < the pivot, we incremment i by 1. So at i = 0, j = 0.       
            if array[j] < pivot:
                i+=1
                #THen  we swap the array[i] element with the array[j] element.
                array[i],array[j] = array[j],array[i]
        # But if j is > the pivot, we swap array[i+1] with the pivot.
        array[i+1], array[pivot_index] = array[pivot_index], array[i+1]


        #Now the quicksort function will sort the array(from index 0 to i+1
        #which is the new position of the pivot) for values less than the pivot.
        less = quicksort(array[:i+1])


        #Now the quicksort function will sort the array(from index 0 to i+2 which is one step greater than 
        #the new position of the pivot) for values greater than the pivot.
        greater = quicksort(array[i+2:])

        
        return less + [pivot] + greater
    
         
 


 
eg = quicksort([5,7,2,9,1,7,4,9,1,0,2])
print(eg)
 
