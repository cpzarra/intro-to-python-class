character = {
    'level': 'beginner',
    'health': 100,
}

def injure(character, damage):
    character['health'] = character['health'] - damage
    if character['health'] < 0:
        character['health'] = 0

def heal(character, amount):
    character['health'] = character['health'] + amount
    if character['health'] > 100:
        character['health'] = 100

print "Injure sustained..."
injure(character, 40)
print character['health']
print "Healing..."
heal(character, 50) # why not 110?
print character['health']