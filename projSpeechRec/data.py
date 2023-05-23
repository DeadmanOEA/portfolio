import numpy as np

def adapt(line):
    change_symb = [['a', 1],
                   ['b', 2],
                   ['с', 3],
                   ['c', 3],
                   ['d', 4],
                   ['e', 5],
                   ['f', 6],
                   ['g', 7],
                   ['h', 8],
                   ['i', 9],
                   ['j', 10],
                   ['k', 11],
                   ['l', 12],
                   ['m', 13],
                   ['n', 14],
                   ['o', 15],
                   ['p', 16],
                   ['q', 17],
                   ['r', 18],
                   ['s', 19],
                   ['t', 20],
                   ['u', 21],
                   ['v', 22],
                   ['w', 22],
                   ['x', 23],
                   ['y', 24],
                   ['z', 25],
                   [' ', 0],
                   ['-', 0]]
    line = list(line)
    for i, n in enumerate(line):
        for j in change_symb:
            if n == j[0]:
                line[i] = j[1]
    
    num = 30 - len(line)
    
    if num != 0:
        for i in range(num):
            line.append(0)
    result  = list(map(int, line))
    for i, n in enumerate(result):
        result[i] = n / 25
    
    return result
#adapt(''),
training_inputs = np.array([adapt('televizorni yoqing'), adapt('televizorning yoki'), adapt('televizorni yoqi'), adapt('televizorni yoki'), adapt('televizorning yoki'),
                            adapt('сhoynakning yoki'), adapt('сhoynakni yoqing'), adapt('сhoynakning yoqing'), adapt('сhoynakni yoki'),
                            adapt('brauzerni oching'), adapt('brauzerning uchun'), adapt('brauzerning oching'),
                            adapt('google saytini oching'), adapt('bugun saytining uchun'), adapt('bugun saytining oching'),
                            adapt('vk saytini oching'), adapt('waka saytining oching'), adapt('waka saytining uchun'), adapt('faqat saytining oching'),
                            adapt('ob-havo bashorati'),
                            adapt('ochiq hujjat'),
                            adapt('kalkulyatorni oching'), adapt('kalkulyator oching'),
                            adapt('ochiq bug'), adapt('ochiq baxt'), 
                            adapt('telegramni oching'), adapt('telegramning oching'), adapt('telegramni uchun') 
                            ])


#print(training_inputs)
training_otputs = np.array([[
    0.001, 0.001, 0.001, 0.001, 0.001,
    0.002, 0.002, 0.002, 0.002, 
    0.003, 0.003, 0.003,
    0.004, 0.004, 0.004,
    0.005, 0.005, 0.005, 0.005,
    0.006,
    0.007,
    0.008, 0.008,
    0.009, 0.009,
    0.010, 0.010, 0.010
                             ]]).T

