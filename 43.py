def p43():
    nums = list(map(str, range(10)))
    prop_csum = 0
    x=1234567890
    while x<9876543210:  
        # for x in range(1234567890,9876543210):
        # if condition isn't satisfied, set number to
        # next eligible number for that condition
        d2_d4  = x//10**6 % 1000
        d3_d5  = x//10**5 % 1000
        d4_d6  = x//10**4 % 1000
        d5_d7  = x//10**3 % 1000 #get groups
        d6_d8  = x//10**2 % 1000
        d7_d9  = x//10    % 1000
        d8_d10 = x        % 1000 
        # check each condition
        if d2_d4 % 2 != 0:
            x = (x//10**9 * 10**9) + (d2_d4 + 1)*10**6
            continue
        if d3_d5%3 !=0:
            x = (x//10**8 * 10**8) + (d3_d5 + (3 - d3_d5%3))*10**5
            continue
        if d4_d6%5 != 0:
            x = (x//10**7 * 10**7) + (d4_d6 + (5 - d4_d6%5))*10**4
            continue
        if d5_d7%7 != 0: 
            x = (x//10**6 * 10**6) + (d5_d7 + (7 - d5_d7%7))*10**3           
            continue
        if d6_d8%11 != 0: 
            x = (x//10**5 * 10**5) + (d6_d8 + (11 - d6_d8%11))*10**2          
            continue
        if d7_d9%13 != 0: 
            x = (x//10**4 * 10**4) + (d7_d9 + (13 - d7_d9%13))*10          
            continue
        if d8_d10%17 != 0:
            x = (x//10**3 * 10**3) + (d8_d10 + (17 - d8_d10%17)) 
            continue

        need = list(nums)
        for d in str(x):
            if need.count(d): need.remove(d)
            else: break
        if len(need) == 0:
            prop_csum += x

        x += 1
    return prop_csum

if __name__ == '__main__':
    print(p43())
