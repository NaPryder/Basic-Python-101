
""" Excercise 5 - Clean data

Input:
- อ่านข้อมูลจากไฟล์ "Raw_promotion_detail.txt" ที่อยู่ในโฟลเดอร์ "D:\Read_file"
    บรรทัดที่ 1 เก็บ header 'date_start|date_end|Product_ID|Price|discount_rate|Quantity'
    บรรทัดที่ 2 ถึง บรรทัดสุดท้าย เก็บข้อมูล date_start, date_end, Product_ID, Price, discount_rate, Quantity
    *** discount_rate เป็นหน่วย % เช่น 10 คือ 10%
    *** date_start, date_end เป็นสตริงในรูป format '%d %b %Y'
    *** หมวดหมู่ของสินค้า คิดจาก 2 ตัวแรกของ Product_ID เช่น 'AG10044' จะได้หมวดหมู่คือ 'AG' 

Process:
- คำนวณหาจำนวนวันที่ต่างกันระหว่าง date_start และ date_end แล้วแปลงเป็นหน่วยนาที
- คำนวณหาส่วนลด จากราคาของสินค้า * discount_rate / 100 และปัดเศษทั้งหมดขึ้น เช่น ได้ส่วนลด 100.01 ให้ปัดเป็น 101
- คำนวณหาว่า ในปี 2021 ถ้าขายสินค้าหมดในช่วงจัดโปรโมชัน จะมียอดขาย ต้นทุนสินค้า และกำไรเท่าไหร่ (รวมทุกหมวดหมู่)
- คำนวณหาว่า ถ้าขายสินค้าหมดในช่วงจัดโปรโมชัน ระหว่างวันที่ 1 Jan 2021 - 30 Jun 2021 (คิดจาก date_start)  แต่ละหมวดหมู่จะมียอดขาย ต้นทุนสินค้า และกำไรเท่าไหร่
    *** ให้ต้นทุนสินค้าอยู่ที่ 25% ของราคาสินค้าก่อนหักส่วนลด)

Output: 
- แสดงผล เวลาทั้งหมดที่จัดโปรโมชันทั้งปีของทุก product (หน่วยวัน และ นาที)
- แสดงผล ยอดขาย ต้นทุนสินค้า และกำไรของทั้งปีทุกหมวดหมู่
- แสดงผล ยอดขาย ต้นทุนสินค้า และกำไรที่ได้ในช่วงวันที่ 1 Jan 2021 - 30 Jun 2021 ของแต่ละหมวดหมู่

---Result---
เวลาทั้งหมดที่จัดโปรโมชันทั้งปี = 234 วัน หรือ 336960 นาที
ในปี 2021 มียอดขายรวม: 13652270.0 บาท
ในปี 2021 มีต้นทุนรวม: 5115500.0 บาท
ในปี 2021 มีกำไรรวม: 8536770.0 บาท

ในช่วงครึ่งปีแรก 1 Jan 2021 - 30 Jun 2021
AE มียอดขายรวม: 425450.0 บาท, มีต้นทุนรวม: 121875.0 บาท, มีกำไรรวม: 303575.0 บาท
AS มียอดขายรวม: 1141060.0 บาท, มีต้นทุนรวม: 402550.0 บาท, มีกำไรรวม: 738510.0 บาท
AQ มียอดขายรวม: 1267200.0 บาท, มีต้นทุนรวม: 485000.0 บาท, มีกำไรรวม: 782200.0 บาท
AT มียอดขายรวม: 4819500.0 บาท, มีต้นทุนรวม: 1721250.0 บาท, มีกำไรรวม: 3098250.0 บาท
AG มียอดขายรวม: 245000.0 บาท, มีต้นทุนรวม: 87500.0 บาท, มีกำไรรวม: 157500.0 บาท
"""

import datetime
import os
import math

def get_discount(discount_rate, price):
    """คำนวณหา discount พร้อมปัดเศษทั้งหมดขึ้น 
    เช่น discount_rate = 15
        price = 150
        ส่วนลดก่อนปัดเศษ = 22.5
        ส่วนลดหลังปัดเศษขึ้น = 23

    Args:
        discount_rate (int): ส่วนลด (เปอร?เซ็นต์)
        price (float): ราคาสินค้า

    Returns:
        int: ส่วนลดหลังปัดเศษขึ้น
    """
    return math.ceil(price*discount_rate/100)

def find_differrence_days(date_start, date_end):
    """คำนวณหาจำนวนวันที่ต่างกันของ ตัวแปรวันที่ date_start กับ date_end 
    และ return ค่าส่วนต่างของ days 
    
    Args:
        date_start (datetime): วันที่ 
        date_end (datetime): วันที่ 

    Returns:
        int: จำนวนวัน ที่ต่างของ date_start กับ date_end 
    """
    dt = date_end - date_start
    return dt.days

def check_half_year(date_start):
    """ตรวจสอบว่า date_start อยู่ในช่วงวันที่ 1 Jan 2021 - 30 Jun 2021 หรือไม่

    Args:
        date_start (datetime): วันที่
    
    Returns:
        bool: True ถ้า date_start อยู่ในช่วงวันที่ 1 Jan 2021 - 30 Jun 2021 
    """
    return datetime.datetime(2021, 1, 1) <= date_start <= datetime.datetime(2021, 6, 30)

# add function
def convert_str_to_dt(string_date):
    return datetime.datetime.strptime(string_date, "%d %b %Y")

def convert_day_to_minute(days):
    return days*24*60

def get_half_year_sales(group, sales, profit, cost):
    if group not in d_half_year_sales:
        d_half_year_sales[group] = [sales, profit, cost]
    else:
        d_half_year_sales[group][0] += sales
        d_half_year_sales[group][1] += profit
        d_half_year_sales[group][2] += cost

def show_half_year():
    for group, value in d_half_year_sales.items():
        print(f"{group} มียอดขายรวม: {value[0]} บาท, มีต้นทุนรวม: {value[2]} บาท, มีกำไรรวม: {value[1]} บาท")
total_discount = 0  # ส่วนลดรวมทั้งปี
total_sales = 0     # ยอดขายรวมทั้งปี
total_cost = 0      # ต้นทุนรวมทั้งปี
total_profit = 0    # กำไรรวมทั้ง
total_minute = 0    # จำนวนนาทีที่จัดโปรโมชันทั้งปี
total_day = 0       # จำนวนวันที่จัดโปรโมชันทั้งปี

# Code here
file = os.path.join("D:\Read_file", "Raw_promotion_detail.txt")
d_half_year_sales = {}

with open(file, 'r') as txt_file:
    for i, line in enumerate(txt_file):
        if i < 1:
            continue

        date_start, date_end, product_ID, price, discount_rate, quantity = [e.strip() for e in line.strip().split('|')]

        group = product_ID[:2]
        price = float(price)
        dt_start = convert_str_to_dt(date_start)
        dt_end = convert_str_to_dt(date_end)
        days = find_differrence_days(dt_start, dt_end)
        minutes = convert_day_to_minute(days)
        discount = get_discount(int(discount_rate), price)

        cost = 0.25 * price * int(quantity)
        sales = (price - discount) * int(quantity)
        profit = sales - cost

        total_day += days
        total_minute += minutes
        total_discount += discount
        total_sales += sales
        total_cost += cost
        total_profit += profit

        if check_half_year(date_start=dt_start):
            get_half_year_sales(group, sales, profit, cost)

print('---Result---')
print("เวลาทั้งหมดที่จัดโปรโมชันทั้งปี = {} วัน หรือ {} นาที".format(total_day, total_minute))
print("ในปี 2021 มียอดขายรวม: {} บาท".format(total_sales))
print("ในปี 2021 มีต้นทุนรวม: {} บาท".format(total_cost))
print("ในปี 2021 มีกำไรรวม: {} บาท".format(total_profit))
print()
print("ในช่วงครึ่งปีแรก 1 Jan 2021 - 30 Jun 2021")
# show result here
show_half_year()
    

