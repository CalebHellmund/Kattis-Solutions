# Problem: 4 thought
# Link: https://open.kattis.com/problems/4thought
# Difficulty: Medium 

operations = ['+', '-', '*', '//']
def test():
    goal = int(input())
    for x in operations:
        for y in operations:
            for z in operations:
                case = '4' + x + '4' + y + '4' + z + '4'
                if eval(case) == goal:
                    if x == '//':
                        x = '/'
                    if y == '//':
                        y = '/'
                    if z == '//':
                        z = '/'
                    print(f"4 {x} 4 {y} 4 {z} 4 = {goal}")
                    return False
    return True