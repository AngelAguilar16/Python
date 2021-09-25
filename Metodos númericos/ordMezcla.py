def merge(left, right):
    result=[]
    
    while(len(left) > 0 and len(right) > 0):
        if (left[0] <= right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
            
    if(len(left) > 0):
        result = result + left
    if(len(right) > 0):
        result = result + right

    return result

def sort(arra):
    left=[]
    right=[]
    
    if(len(arra) <= 1):
        return arra
        
    else:
        middle=len(arra)/2
        middle-=1
        
        for x in range(middle+1):
            left.append(arra[x])
            
             
        for x in range(middle+1, len(arra)):
            right.append(arra[x])
            
        left = sort(left)
        right = sort(right)
        result = merge(left, right)
        
        return result
        
    
v = [5,55,555,5555]
sort(v)