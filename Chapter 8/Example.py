
def is_leap_year(year):
    # print('---start function---')
    if ((year%4 == 0) and (year%100 != 0)) or (year%400 ==0):
        days = 366
    else:
        days = 365
    
    print(f'Total days of year {year} = {days}')
    # print('---end function---')

is_leap_year(year=2020)
is_leap_year(year=2021)
is_leap_year(year=2022)
is_leap_year(year=2023)
is_leap_year(year=2024)
is_leap_year(year=2025)
is_leap_year(year=2026)
is_leap_year(year=2005)
