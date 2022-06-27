
# code ตาม flowchart โดยการประยุกต์ใช้นอเสธ

level = 1
exp = 0
counter = 0

while True:  

    # detail
    print('level :',level)
    print('exp :',exp)
    print('counter :',counter)

    if (level != 10) or (exp < 60):
        #ล่ามอนสเตอร์
        print('ล่ามอนสเตอร์')
        exp += 40
        counter += 1

        if exp >= 100:
            exp = 0       
            level += 1
            print('level up to', level)

    else:
        # ล่าบอส
        print('ล่าบอส')

        if (counter >= 35) :
            print('ผ่านด่าน')
            break   

        else:
            level = 9
            print('try again')
    
    print('-------------------')

print('End')