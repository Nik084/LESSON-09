first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) >= 5]
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
third_result = {x: len(x) for x in first_strings + second_strings if len(x) % 2 == False}
fourth = [(first_strings[i], second_strings[i])
          for i in range(min(len(first_strings), len(second_strings)))
          if len(first_strings[i]) == len(second_strings[i])]
print(first_result)
print(second_result)
print(third_result)
print(fourth)