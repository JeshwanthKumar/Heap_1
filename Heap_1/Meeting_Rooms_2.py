def minMeetingRoom(intervals):
    start = sorted([i[0] for i in intervals])   #Sort all the first index in the intervals
    end = sorted([i[1] for i in intervals]) #Sort all the secind index in the intervals
    
    res = 0 #Initialize res as 0
    count = 0   #Initialize count as 0
    
    s, e = 0, 0 #Initialize s and e as two pointers starting from first index
    while s < len(intervals):   #Continue till the length of the intervals
        if start[s] < end[e]:   #If the start[s] < end[e] increment the s pointer by 1 and count by 1
            s += 1
            count += 1
        else:   #Else increment the e counter by 1 and decrement the count by 1
            e += 1
            count -= 1
            
        res = max(res, count)   #Compare the maximum between res and count and store it in res
    return res  #Return res which will give the minimum number of rooms

print(minMeetingRoom([(0,30),(5,10),(15,20)]))