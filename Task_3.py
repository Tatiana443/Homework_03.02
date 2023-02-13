# В настольной игре Scrabble каждая буква имеет определенную ценность.
# очки распределяются так: A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка;K – 5 очков;
# J, X – 8 очков;Q, Z – 10 очков. Напишите программу, которая вычисляет 
# стоимость введенного пользователем слова.
# Пример: ноутбук 12
points_en = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
        8:'JZ',
      	10:'QZ'}
points_ru = {1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
        4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}
dict = abs(int(input('Введите 1, если английский алфавит, либо 2, если русский: ')))
word = input('Введите слово: ').upper()
if dict == 1:
	print(sum([k for i in word for k, v in points_en.items()  if i in v]))
else:
	print(sum([k for i in word for k, v in points_ru.items() if i in v]))

