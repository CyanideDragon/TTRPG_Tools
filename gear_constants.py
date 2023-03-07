import json

def unpacker(data):

    print("\n \n \n \n")

    weapon_data = {}
    armor_data = {}
    adventuring_gear_data = {}
    #Since the json file is a dict in a list in a dict, we need to cut out the list part.
    #We can create 3 variables, one for each gear type. Then we make the keys of the first dict the name of the weapon, and then the values are a dict of the remaining values.

    weapon_list = []
    armor_list = []
    adventuring_gear_list = []

    for i in data['weapons']:
        weapon_list.append(i)

    for i in data['armors']:
        armor_list.append(i)
    
    for i in data['adventuring_gear']:
        adventuring_gear_list.append(i)

    #prints for testing outside of main environment
    # print(weapon_list)
    # print(armor_list)
    # print(adventuring_gear_list)

    # print("\n \n \n \n")


    for j in weapon_list:
        new_key = j.pop('name')
        weapon_data.update({new_key: j})
        #key will be weapon name, values will be another dict with key values related to weapon properties

    for j in armor_list:
        new_key = j.pop('name')
        armor_data.update({new_key: j})
        #key will be armor name, values will be another dict with key values related to armor properties

    for j in adventuring_gear_list:
        new_key = j.pop('name')
        adventuring_gear_data.update({new_key: j})
        #key will be adventuring_gear name, values will be another dict with key values related to adventuring_gear properties

    #prints for testing outside of main environment
    # print(f"Arming sword     =     {weapon_data['Arming Sword']}")
    # print(f"Scimitar         =     {weapon_data['Scimitar']}")
    # print(f"Longbow          =     {weapon_data['Longbow']}")

    return weapon_data, armor_data, adventuring_gear_data


with open('data/items.json', 'r') as item_file:
        data = json.load(item_file)


weapon_data, armor_data, adventuring_gear_data = unpacker(data)

