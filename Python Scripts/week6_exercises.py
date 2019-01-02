def histogram(s):
    c_counts = dict()
    for c in s:
        if not (c in c_counts):
            #letter does not exist in the dictionary
            #add to the dictionary
            c_counts[c]=1
        else:
            c_counts[c]+=1
    return c_counts


def histogram_2(s):
    c_counts = dict()
    for c in s:
        c_counts[c]=c_counts.get(c,0)+1
    return c_counts

def reverse_lookup(d,v):
    keys = []
    for k in d:
        if d[k]==v:
            keys.append(k)
        if len(keys)==0:
            raise LookupError("Not found in dictionary")
        else:
            return keys

def invert_dict(d):
    # create an empty dictionary
    newd = dict()
    # process d and add to newd
    for key in d:
        v = d[key]
        if not v in newd:
            newd[v] = [key]
        else:
            newd[v].append(key)
        return newd
            




    
    # find out value range
    largest_number = 0
    for key in d:
        if d[key]>largest_number:
            largest_number=d[key]
    # find all the keys that map to each number in range
    for i in range(largest_number):
        reverse_lookup
        
