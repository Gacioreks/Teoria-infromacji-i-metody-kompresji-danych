import sys
import random



def get_file_string(file_name):
    f = open(file_name)
    data = f.read()
    return data

def get_letters_probability(text, level=1):
    substring = ""
    substrings_count = 0
    substrings_dict = {}
    left_bound = 0
    right_bound = level
    text_length = len(text)
    for i in range(text_length):
        substring = text[left_bound:right_bound]
        if(len(substring) < level):
            break
        left_bound += 1
        right_bound += 1
        if(not (substring in substrings_dict)):
            substrings_dict[substring] = 1
        else:
            substrings_dict[substring] += 1
        substrings_count += 1
    for key, value in substrings_dict.items():
        substrings_dict[key] = value/substrings_count
    return substrings_dict.copy()

def get_probability_arr(substrings_dictionary):
    probability_arr = []
    for key, value in substrings_dictionary.items():
        probability_arr.append({'substring': key, 'prob': value})
    probability_arr.sort(key=lambda substring: -substring['prob'])
    return probability_arr.copy()

def generate_text(probability_arr, text_length, substring_length=1):
    generated_text = ""
    for i in range(text_length):
        random_number = random.random()
        probability_sum = 0
        drawn_substring = ""
        for substring in probability_arr:
            probability_sum += substring['prob']
            if(probability_sum >= random_number):
                drawn_substring = substring['substring']
                break
        generated_text += drawn_substring
    return generated_text

file_name = "data.txt"
level = 1
text_length = 10

if(len(sys.argv) > 1):
    file_name = sys.argv[1]
    if(sys.argv[2]):
        level = int(sys.argv[2])
    if(sys.argv[3]):
        text_length = int(sys.argv[3])
    

data = get_file_string(file_name)
substrings_probability = get_letters_probability(data, level)


substrings_probability_arr = get_probability_arr(substrings_probability)
print(substrings_probability_arr)

generated_text = generate_text(substrings_probability_arr, text_length, level)
print('Generated text:\n' + generated_text)
