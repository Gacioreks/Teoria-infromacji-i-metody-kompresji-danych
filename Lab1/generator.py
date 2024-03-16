# -*- coding: utf-8 -*-
import sys
import random


def read_sample_file(file_name):
    f = open(file_name)
    data = f.read()
    return data

def draw_letter(probability_list):
    random_number = random.random()
    probability_sum = 0
    for element in probability_list:
        probability_sum += element['probability']
        if(probability_sum >= random_number):
            return element['letter']

def get_zero_level_text(text_length):
    ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    probability_list = []
    for letter in ALPHABET:
        probability_list.append({'letter': letter, 'probability': 1/len(ALPHABET)})
    generated_text = ""
    for i in range(text_length):
        generated_text += draw_letter(probability_list)
    return generated_text

def get_substring_frequency(data, level):
    substring_frequency = {}
    left = 0
    right = level
    for i in range(len(data)):
        substring = data[left:right]
        if(len(substring) < level):
            break
        left += 1
        right += 1
        if(not (substring in substring_frequency)):
            substring_frequency[substring] = 1
        else:
            substring_frequency[substring] += 1
    return substring_frequency.copy()

def get_probability_list(generated_text, substring_frequency_list, level):
    probability_list = []
    generated_text_length = len(generated_text)
    while(True):
        count = 0
        previous_string = generated_text[generated_text_length - level + 1:]
        for key, value in substring_frequency_list[0].items():
            if(previous_string+key in substring_frequency_list[level-1]):
                probability_list.append(
                    {
                        'letter': key,
                        'substring': previous_string+key,
                        'count': substring_frequency_list[level-1][previous_string+key]
                    }
                )
                count += substring_frequency_list[level-1][previous_string+key]
        if(len(probability_list) == 0):
            level -= 1
        else:
            for element in probability_list:
                element['probability'] = element['count'] / count
            return probability_list

def generate_text(data, level, text_length):
    substring_frequency_list = [get_substring_frequency(data, i+1) for i in range(level)]    
    generated_text = ""
    
    for i in range(text_length):
        probability_list = get_probability_list(generated_text, substring_frequency_list, level)
        generated_text += draw_letter(probability_list)
    
    return generated_text

def write_to_file(file_name, text):
    f = open(file_name, 'w')
    f.write(text)
    f.close()

def main():
    level = int(sys.argv[1])
    input_file_name = sys.argv[2]
    output_file_name = sys.argv[3]
    output_file_size = int(sys.argv[4])

    if(level == 0):
        generated_text = get_zero_level_text(output_file_size)
        print(generated_text)
        write_to_file(output_file_name, generated_text)
        return

    data = read_sample_file(input_file_name)
    generated_text = generate_text(data, level, output_file_size)

    print(generated_text)
    write_to_file(output_file_name, generated_text)

if __name__ == '__main__':
    main()