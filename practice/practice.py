numbers = [10,20,30,20,10,50,60,40,80,50,40]
unique = []
for e in numbers:
    if e not in unique:
        unique.append(e)


print(unique)
print(set(numbers))

words = ['aa', 'abc', 'xyz', 'aba', '1221']
count = 0
for w in words:
    if len(w) > 2 and w[0] == w[len(w) - 1]:
        count += 1
        
print(count)

students = [{'id': 1, 'mid': 80, 'name': 'Lary'}, 
            {'id': 2, 'mid': 78, 'name': 'Rabi'}, 
            {'id': 3, 'mid': 98, 'name': 'Ester'}, 
            {'id': 4, 'mid': 73, 'name': 'John'}, 
            {'id': 5, 'mid': 94, 'name': 'Berry'}, 
            {'id': 6, 'mid': 88, 'name': 'Bob'}, 
            {'id': 7, 'mid': 80, 'name': 'Alex'}, 
            {'id': 8, 'mid': 90, 'name': 'Andy'}, 
            {'id': 9, 'mid': 84, 'name': 'Beth'}, 
            {'id': 10, 'mid': 76, 'name': 'Cindy'}]

print(sum(s['mid'] >= 80 for s in students))