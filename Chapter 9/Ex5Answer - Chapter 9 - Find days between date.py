
""" Excercise 5 - Find days between date

Input:
- ค่า a เป็นวันที่ที่กำหนด
- ลิสต์ x เก็บค่า วันที่ในรูปแบบของสตริง (format '%Y-%m-%d %H')

Process:
- คำนวณหาจำนวนวันที่ต่างกันของแต่ละ item กับ a
- คำนวณหาจำนวนชั่วโมงต่างกันของแต่ละ item กับ a

Output: 

a = 2022-01-01 10:00:00
days difference:152 days hours:23.0 h.     hours difference: 3671 h.
days difference:184 days hours:9.0 h.      hours difference: 4425 h.
days difference:214 days hours:0.0 h.      hours difference: 5136 h.
days difference:224 days hours:10.0 h.     hours difference: 5386 h.
days difference:0 days hours:8.0 h.        hours difference: 8 h.
days difference:-213 days hours:17.0 h.    hours difference: -5095 h.
days difference:-201 days hours:10.0 h.    hours difference: -4814 h.
days difference:-88 days hours:5.0 h.      hours difference: -2107 h.
days difference:-89 days hours:6.0 h.      hours difference: -2130 h.
days difference:-335 days hours:12.0 h.    hours difference: -8028 h.
days difference:1 days hours:6.0 h.        hours difference: 30 h.
"""

import datetime

a = datetime.datetime(2022, 1, 1, 10)

def find_days_sec(date_x):
    """คำนวณหาจำนวนวันที่ต่างกันของ ตัวแปรวันที่ date กับ a 
    และ return ค่าส่วนต่างของ days, hours

    คำนวณชั่วโมงที่ต่างกันนสามารถนำหน่วยวินาที มา หาร 3600 ได้
    เช่น 
        a = 1 Jan 2022 เวลา 10.00 am
        date x = 2 Jan 2022 เวลา 1.00 AM
        วันที่จะต่างกัน -1 วัน กับ 9 ชั่วโมง
    หรือ
        a = 1 Jan 2022 เวลา 10.00 am
        date x = 31 Dec 2021 เวลา 4.00 AM
        วันที่จะต่างกัน +1 วัน กับ 6 ชั่วโมง
    
    Args:
        date_x (datetime): วันที่ ที่ต้องการเปรียบเทียบกับ a

    Returns:
        int: จำนวนวัน ที่ต่างกันกับ a
        number: จำนวนชั่วโมง ที่ต่างกันกับ a

    """
    # 
    dt = a - date_x
    days = dt.days
    hours = dt.seconds/3600

    return days, hours

x = [
    "2021-08-01 11",
    "2021-07-01 01",
    "2021-06-01 10",
    "2021-05-22 00",
    "2022-01-01 02",
    "2022-08-01 17",
    "2022-07-21 00",
    "2022-03-30 05",
    "2022-03-31 04",
    "2022-12-01 22",
    "2021-12-31 04",
]

print(f"a = {a}")

for item in x:
    # Code here
    date1 = datetime.datetime.strptime(item, "%Y-%m-%d %H")

    days, hours = find_days_sec(date1)
    diff_h = int(days*24 + hours)
    
    # ให้ใส่ตัวแปรที่ .format()
    print("days difference:{} days hours:{} h.\t   hours difference: {} h.".format(days, hours, diff_h))



