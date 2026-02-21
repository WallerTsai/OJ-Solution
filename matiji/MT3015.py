def construction(number):
    #暴力构造哈希表(注意顺序就好)
    map = {
        '1s':2,
        '2s':2,'2p':6,
        '3s':2,'3p':6,
        '4s':2,'3d':10,'4p':6,
        '5s':2,'4d':10,'5p':6,
        '6s':2,'4f':14,'5d':10,'6p':6,
        '7s':2,'5f':14,'6d':10,'7p':6,'8s':2,
    }
    position = {
        's':0,
        'p':1,
        'd':2,
        'f':3,
    }


    res = [[] for _ in range(8)]

    for level,num in map.items():
        if number > 0:
            level_number = int(level[0])
            pos_number = position[level[1]]
            electrons_number = min(number,num)
            res[level_number-1].insert(pos_number,f"{level}{electrons_number}")
            number -= num
    for i in range(len(res)):
        if res[i]:
            print(' '.join(res[i]))

n = int(input())
construction(n)

def electron_configuration(n):
    # 定义能级及其最大电子数
    levels = {
        '1s': 2, '2s': 2, '2p': 6, '3s': 2, '3p': 6, '4s': 2, '3d': 10,
        '4p': 6, '5s': 2, '4d': 10, '5p': 6, '6s': 2, '4f': 14, '5d': 10,
        '6p': 6, '7s': 2, '5f': 14, '6d': 10, '7p': 6, '8s': 2
    }
    configuration = []

    for level, max_e in levels.items():
        if n > 0:
            electrons = min(n, max_e)
            configuration.append(f"{level}{electrons}")
            n -= electrons

    # 输出格式
    output = {}
    for entry in configuration:
        level_number = int(entry[0])  # 获取能层数
        if level_number not in output:
            output[level_number] = []
        output[level_number].append(entry)

    # 打印结果
    for i in sorted(output.keys()):
        print(' '.join(output[i]))

# 输入电子数
n = int(input())
electron_configuration(n)