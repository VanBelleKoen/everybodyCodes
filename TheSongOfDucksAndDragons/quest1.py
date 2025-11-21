name_list = ['Calketh','Zraaltaril','Kyoris','Zyrketh','Eltoth','Nyssluth','Zraalonar','Ascaldaros','Thalkyris','Urisis']
instruction_list = ['L9','R9','L6','R1','L1','R9','L2','R1','L8','R9','L2']


def find_quest_giver(names, instructions):
    index = 0
    for instr in instructions:
        direction = instr[0]
        steps = int(instr[1:])
        if direction.upper() == 'L':
            index = (index - steps) % len(names)
        elif direction.upper() == 'R':
            index = (index + steps) % len(names)
    print(names[index])


parent_first_name_list = ['Rythlon','Valcalyx','Brivsin','Thaloris','Shaelardith','Havzryn','Grimketh','Azaxis','Krynnsar','Gorathbryn','Tharnindor','Myndvash','Brythsar','Azlyr','Adalhal','Jalris','Goratheldrin','Aelalar','Ferdrith','Vaelrovan']
instructions_parents = ['L18','R18','L6','R18','L14','R9','L14','R18','L14','R17','L5','R17','L5','R6','L5','R12','L5','R18','L5','R13','L13','R9','L15','R18','L16','R8','L9','R14','L7']


def find_first_parent(names, instructions):
  index = 0
  for instr in instructions:
    direction = instr[0]
    steps = int(instr[1:])
    if direction.upper() == 'L':
        index = (index - steps) % len(names)
    elif direction.upper() == 'R':
        index = (index + steps) % len(names)
  print(names[index])

parent_second_name_list = ['Ylaronar','Eldengryph','Ilmaragrath','Tarlindor','Jarthyris','Paldgoril','Sarthel','Falkris','Kynelor','Rynisis','Erasselor','Paldsaral','Calral','Ulkfarin','Glaurpyr','Eltthyris','Olarjorath','Morquor','Vorncarth','Ardencalyx','Tharilaxis','Quorluth','Xyrzyph','Gaeririn','Eaddravor','Balzral','Lordaros','Brivgnaris','Syltaril','Seljor']
instructions_second_parents = ['L15','R14','L46','R39','L17','R47','L26','R9','L22','R14','L7','R40','L10','R17','L37','R39','L14','R48','L36','R28','L5','R43','L5','R31','L5','R34','L5','R22','L5','R40','L5','R35','L5','R9','L5','R30','L5','R38','L5','R16','L34','R39','L18','R8','L27','R31','L49','R11','L38','R20','L41','R16','L33','R15','L8','R14','L26','R9','L46']

def find_second_parent(names, instructions):
    names = names.copy()
    for instr in instructions:
        index = 0
        direction = instr[0]
        steps = int(instr[1:])
        if direction.upper() == 'L':
            new_index = (index - steps) % len(names)
        elif direction.upper() == 'R':
            new_index = (index + steps) % len(names)
        names[0], names[new_index] = names[new_index], names[0]
    print(names[0])

find_quest_giver(name_list, instruction_list)
find_first_parent(parent_first_name_list, instructions_parents)
find_second_parent(parent_second_name_list, instructions_second_parents)