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
    path = "lexic_mistakes.csv"
    data = get_dictionary(path)
    corrected = messages
    for key in data:
        if key in corrected:
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
    path = "lexic_mistakes.csv"
    data = get_dictionary(path)

    messages = messages.lower()
    for key in data:
        if key in messages:
            res.append(f"❌ {key}\n✔️ {data[key]}")

    return res


# def write_together(sentence: str) -> list or None:
#     """Returns the list of error messages if there are the mistakes
#     with words that need to be written together."""
#     sentence = sentence.lower()
#     errors = []
#     together_prefixes = {'абро', 'авіа', 'авто', 'агро', 'аеро', 'аква', 'алко', 'анти',
#                          'арт', 'астро', 'аудіо', 'біо', 'боди', 'веб', 'віце', 'геліо', 'гео', 'гідро', 'гіпер',
#                          'дендро', 'екзо', 'еко', 'економ', 'екс', 'етно', 'євро', 'зоо', 'ізо', 'кібер', 'контр',
#                          'мета', 'метео', 'моно', 'мото', 'нарко', 'нео', 'онко', 'палео', 'пан', 'пара', 'поп',
#                          'прес', 'псевдо', 'соціо', 'теле', 'фіто', 'фолк', 'фольк', 'фоно', 'архі', 'архи', 'бліц',
#                          'гіпер', 'екстра', 'макро', 'максі', 'міді', 'мікро', 'міні', 'мульти', 'нано', 'полі',
#                          'преміум', 'супер', 'топ', 'ультра', 'флеш', 'напів', 'аби', 'ані', 'де'}
#     for prefix in together_prefixes:
#         pattern = rf'^(.* )*{prefix}[^\w].*'
#         if re.fullmatch(pattern, sentence):
#             errors.append(f'❗️ Слова з префіксом "{prefix}" пишуться разом.')
#     if errors:
#         return errors
#     return None


# def write_with_hyphen(sentence: str) -> list or None:
#     """Returns the list of error messages if there are the mistakes
#     with words that need to be written with a hyphen."""
#     sentence = sentence.lower()
#     errors = []
#     hyphen_prefixes = {'альфа', 'бета', 'дельта', 'казна', 'хтозна', 'бозна'}
#     hyphen_sufixes = {'таки', 'небудь'}
#     for prefix in hyphen_prefixes:
#         prefix_pattern = rf'^(.* )*{prefix}[^-].*'
#         if re.fullmatch(prefix_pattern, sentence):
#             errors.append(
#                 f'❗️ Слова з префіксом "{prefix}" пишуться через дефіс.')
#     for sufix in hyphen_sufixes:
#         sufix_pattern = rf'.*[^-]{sufix}( .*)?'
#         if re.fullmatch(sufix_pattern, sentence):
#             errors.append(
#                 f'❗️ Слова з суфіксом "{sufix}" пишуться через дефіс.')
#     if errors:
#         return errors
#     return None


# def main_check(sentence: str) -> list or None:
#     """Returns the list of error messages if there are the mistakes
#     with words that need to be written with a hyphen or together."""
#     together_errors = write_together(sentence)
#     hyphen_errors = write_with_hyphen(sentence)
#     if together_errors and hyphen_errors:
#         errors = together_errors + hyphen_errors
#     elif together_errors:
#         errors = together_errors
#     else:
#         errors = hyphen_errors
#     return errors
