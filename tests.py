area = [['X', '0', '0', '0'],
        ['X', 'X', 'X', '0'],
        ['0', 'X', '0', 'X'],
        ['X', '0', 'X', 'X']]
print(area[1].count('X'))
area_size = 4
win_length = 3
shifts = area_size - win_length
string = ''
for i in area:
    string = string + ''.join(i) + ' '
print(string, string.count('X' * win_length))
print()
string = ''
for j in range(area_size):
    for i in range(area_size):
        string += ''.join(area[i][j])
    string += ' '
print(string, string.count('X' * win_length))
print()
string = ''
for i in range(area_size):                          # 1-я диагональ (вправо-вниз)
    string += ''.join(area[i][i])
string += ' '
for i in range(area_size - 1, -1, -1):              # 2-я диагональ (влево-вниз)
    string += ''.join(area[area_size - 1 - i][i])
string += ' '
if shifts > 0:
    for j in range(1, shifts + 1):
        for i in range(area_size - j):              # верхние-левые диагонали вправо-вниз
            string += ''.join(area[i][i + j])
        string += ' '
        for i in range(area_size - j):              # нижние-левые диагонали вправо-вниз
            string += ''.join(area[i + j][i])
        string += ' '
    for j in range(1, shifts + 1):
        for i in range(area_size - 1, j - 1, -1):   # верхние-правые диагонали влево-вниз
            string += ''.join(area[area_size - 1 - i][i - j])
        string += ' '
        for i in range(area_size - 1, j - 1, -1):   # нижние-правые диагонали влево-вниз
            string += ''.join(area[area_size - i + j - 1][i])
        string += ' '
print(string, string.count('X' * win_length))

# j = list(filter(lambda v: v != 0, map(len, string.split('X'))))
# print(string.split('X'))
# print(j)