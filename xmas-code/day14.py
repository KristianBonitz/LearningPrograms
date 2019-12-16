import math

f = open("input.txt")
puzzle_input = [j.strip().split('=>') for i, j in enumerate(f)]
reactions = []
r_inputs = []
r_outputs = []
for i, o in puzzle_input:
    r_inputs.append([{"unit":int(elements.strip(', ').split(' ')[0]), "name":elements.strip(', ').split(' ')[1]} for elements in i.strip().split(',')])
    r_outputs.append([{"unit":int(elements.strip(', ').split(' ')[0]), "name":elements.strip(', ').split(' ')[1]} for elements in o.strip().split(',')])
for a in range(len(r_inputs)):
    reactions.append( {"input": r_inputs[a], "output": r_outputs[a]})

def find_components(reaction_list, name):
  for i in reaction_list:
    if i['output'][0]['name'] == name:
        return i['input']

def find_reaction(reaction_list, name):
  for i in reaction_list:
    if i['output'][0]['name'] == name:
        return i

def break_down(reaction_list, name, amount):
  e_list = []
  r = find_reaction(reaction_list, name)
  for i in r["input"]:
        units = math.ceil(amount / r['output'][0]['unit'])
        e_list.append({"unit": i['unit'] * units, "name": i['name']})

  return e_list

def search_tree(reaction_list, search_name, match_name):
    components = find_components(reaction_list, search_name)
    for i in components:
        if i['name'] == "ORE":
            return False
        elif i['name'] == match_name:
            return True

    if True in [search_tree(reaction_list, j["name"], match_name) for j in components]:
        return True
    else:
        return False

def break_down_elements(reaction_list, starting_element):
    break_down_list = [starting_element]
    while len(break_down_list) > 1 or break_down_list[0]["name"] != 'ORE':
        for prime in break_down_list:
            found = False
            for other in break_down_list:
                if other["name"] != "ORE":
                    found = search_tree(reaction_list, other["name"], prime["name"])

                if found == True:
                    break
            if found == False and prime["name"] != "ORE":
                break_down_list += break_down(reaction_list, prime["name"], prime["unit"])
                break_down_list.remove(prime)
                break_down_list = merge_elements(break_down_list)
                break
    return break_down_list

def merge_elements(element_list):
    new_list = []
    for element in element_list:
        found = False
        for i in range(len(new_list)):
            if new_list[i]["name"] == element["name"]:
                new_list[i]["unit"] += element["unit"]
                found = True
                break
        if found == False: new_list.append(element)
    
    return new_list
#print(break_down(reactions, "FUEL", 2))
ore_limit = 1000000000000
ore_needed = 975981768855
fuel_amount = 1639350

while ore_needed < ore_limit:
    fuel_amount += 1 
    ore_needed = break_down_elements(reactions, {"unit": fuel_amount, "name":"FUEL"})[0]["unit"]
    print("fuel amount:",fuel_amount,"\nOre needed:", ore_needed)

fuel_amount -= 1
print(fuel_amount)
#print(merge_elements([{"unit": 10, "name": "A"}, {"unit": 10, "name": "A"}, {"unit": 10, "name": "X"}]))
