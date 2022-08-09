def seq_search(data, key):
    
    for i in range(len(data)):
        if data[i] == key :
            return i
        
    return -1 