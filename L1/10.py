# найти год, исходя из unix-времени

def year(unix_time):
    
    s_year = 1970 + ((((unix_time // 60) / 60) / 24) // 365)

    return s_year


unix_time = int(input())
print(year(unix_time))