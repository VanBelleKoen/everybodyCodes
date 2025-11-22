A = [155,53]
R = [0,0]


def sum_array(arr1, arr2):
    R = [arr1[0] + arr2[0], arr1[1] + arr2[1]]
    return R

def multiply_array(arr1, arr2):
    R = [arr1[0] * arr2[0] - arr1[1] * arr2[1], arr1[0] * arr2[1] + arr1[1] * arr2[0]]
    return R

def divide_array(arr1, arr2):
    R = [int(arr1[0] / arr2[0]), int(arr1[1] / arr2[1])]
    return R

def cycle(R, A):
    R = multiply_array(R, R)
    R = divide_array(R, [10,10])
    R = sum_array(R, A)
    return R

def engraving_cycles(R, B):
    R = multiply_array(R, R)
    R = divide_array(R, [100000,100000])
    R = sum_array(R, B)
    return R

def part_one():
    for _ in range(2):
        R = cycle(R, A)
        result_cycle_one = cycle(R, A)
    print("Result after one cycle:", result_cycle_one)


def part_two():
    A=[-21733,67997]
    limit = 1000000
    
    grid = []
    for i in range(1001):
        for j in range(1001):
            x = A[0] + i * 1
            y = A[1] + j * 1
            grid.append([x, y])
    
    count = 0
    for point in grid:
        R = [0, 0]
        should_engrave = True
        
        for cycle in range(100):
            R = multiply_array(R, R)
            R = divide_array(R, [100000, 100000])
            R = sum_array(R, point)
            
            if abs(R[0]) > limit or abs(R[1]) > limit:
                should_engrave = False
                break
        
        if should_engrave:
            count += 1
    
    print(f"Part 2 - Number of engraved points: {count}")
    return count

part_two()