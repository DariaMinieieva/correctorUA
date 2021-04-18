"""
This is main module with all the logic
for correctUA bot
"""

import re


def get_dictionary(path):
    """
    Get dictionary from csv
    """
    with open(path, mode='r') as infile:
        dict_wrong_right = {}
        for line in infile:
            line = line.split("\t")
            dict_wrong_right[line[0]] = line[1].strip()
    return dict_wrong_right


def correct_msg(messages):
    """
    Correct a message
    """
    path = "correctorUA/lexic_mistakes.csv"
    data = get_dictionary(path)
    corrected = messages
    for key in data:
        pattern = rf'[^а-яА-Яіїє]{key}[^а-яА-Яіїє]|[^а-яА-Яіїє]{key}$|^{key}[^а-яА-Яіїє]|^{key}$'

        if re.findall(pattern, corrected):
            ind_b = corrected.index(key)
            ind_e = ind_b + len(key)
            temp = corrected[:ind_b]
            temp += data[key]
            temp += corrected[ind_e:]
            corrected = temp

    return corrected


def check_conjunctions(sentence: str) -> list or None:
    """
    Returns the list of messages about a punctuation error
    with conjunctions if there is one.
    """
    sentence = sentence.lower()
    conjunctions = {'а', 'але', 'однак', 'проте', 'зате', 'хоч', 'хоча'}
    errors = []
    for word in conjunctions:
        pattern = rf'^.*[^,] {word}(([^\w].*)|$)'
        if re.fullmatch(pattern, sentence):
            errors.append(f'️❗ Перед "{word}" повинна стояти кома.')
    if errors:
        return errors
    return None


def check_for_mistake(messages):
    """
    Returns mistakes with corrections
    """
    res = []
    path = "correctorUA/lexic_mistakes.csv"
    data = get_dictionary(path)

    messages = messages.lower()
    for key in data:
        pattern = rf'[^а-яА-Яіїє]{key}[^а-яА-Яіїє]|[^а-яА-Яіїє]{key}$|^{key}[^а-яА-Яіїє]|^{key}$'
        if re.findall(pattern, messages):
            res.append(f"❌ {key}\n✔️ {data[key]}")

    return res

# def check_for_mistake(messages):
#     '''
#     Returns mistakes with corrections
#     '''
#     res = []
#     path = "correctorUA/lexic_mistakes.csv"
#     data = get_dictionary(path)
#     messages = messages.lower()
#     for key in data:
#         if (key in messages):
#             res.append(f"❌ {key}\n✔️ {data[key]}")
#     return res
