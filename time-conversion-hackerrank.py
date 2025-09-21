#Solution Time comlexity: O(1).
#With function .index can be used linear seach
#Detect type format and make sentence for search in another array and return the position 

def timeConversion(s):
    # Write your code here
    
    am_hours = ["00", "01", "02" ,"03", "04", "05","06", "07", "08", "09", "10", "11"]
    pm_hours = ["12", "13", "14", "15",  "16", "17", "18", "19","20", "21", "22", "23"]
    
    hour_string =  s.split(':')
    format_time =  hour_string[2][2:4]
    new_hour = None
    
    # si se busca am por ejemplo 1
    if format_time == "PM":
        hour  = "00" if hour_string[0] == "12" else hour_string[0]
        
        picked_position = am_hours.index(hour)
        new_hour =  pm_hours[picked_position]
        
    else:
        hour  = "00" if hour_string[0] == "12" else hour_string[0]
        picked_position = am_hours.index(hour)
        new_hour =  am_hours[picked_position]
        
    new_time =  str(new_hour)+':'+hour_string[1]+':'+hour_string[2][:2]
        
    return new_time
