import re

input_file = open('input/input.txt', 'r')

elves = input_file.read().split('\n\n')

bigger_callory_count = 0

def order_by_callories(elf):
    return elf['callories']

for index, elf in enumerate(elves):
    callories = 0
    for food in elf.splitlines():
        callories += int(food)
    elves[index] = { 'callories': callories, 'index': index }

elves.sort(reverse=True, key=order_by_callories)

for index, elf in enumerate(elves):
    bigger_callory_count += elf['callories']
    if index == 0:
        print(f'Maior quantidade de calorias: {bigger_callory_count}')
    if index == 2:
        print(f'Soma de maiores 3 quantidade de calorias: {bigger_callory_count}')
        break