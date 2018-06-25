card_a = {
    'suit': 'spades',
    'number': 4,
}

card_b = {
    'suit': 'hearts',
    'number': 8,
}

hand = [card_a, card_b]

print 'The hand contains:'
for card in hand:
    print 'A', card['number'], 'of', card['suit']