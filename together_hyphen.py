"""This module discovers the rules of adverbs writing and checks the sentences for it."""

import re


def write_together(sentence: str) -> list:
    """
    Returns the list of error messages if there are the mistakes
    with words that need to be written together.
    """
    errors = {}
    list_strings = []
    together_prefixes = {'абро', 'авіа', 'авто', 'агро', 'аеро', 'аква', 'алко', 'анти',
                         'арт', 'астро', 'аудіо', 'біо', 'боди', 'веб', 'віце', 'геліо', 'гео', 'гідро', 'гіпер',
                         'дендро', 'екзо', 'еко', 'економ', 'екс', 'етно', 'євро', 'зоо', 'ізо', 'кібер', 'контр',
                         'мета', 'метео', 'моно', 'мото', 'нарко', 'нео', 'онко', 'палео', 'пан', 'пара', 'поп',
                         'прес', 'псевдо', 'соціо', 'теле', 'фіто', 'фолк', 'фольк', 'фоно', 'архі', 'архи', 'бліц',
                         'гіпер', 'екстра', 'макро', 'максі', 'міді', 'мікро', 'міні', 'мульти', 'нано', 'полі',
                         'преміум', 'супер', 'топ', 'ультра', 'флеш', 'напів', 'аби', 'ані', 'де'}
    for prefix in together_prefixes:
        if prefix in sentence:
            pattern = re.findall(
                rf'(?<=[^\w-]){prefix}[-\s][\w]*(?=[^\w-])', sentence)
            pattern += re.findall(rf'^{prefix}[-\s][\w]*(?=[^\w-])', sentence)
            pattern += re.findall(rf'(?<=[^\w-]){prefix}[-\s][\w]*$', sentence)
            pattern += re.findall(rf'^{prefix}[-\s][\w]*$', sentence)
            for key in pattern:
                errors[key] = re.sub(rf'{prefix}.', prefix, key)
    for key in errors:
        string = f'❌ {key} \n ✔️ {errors[key]}'
        list_strings.append(string)
    return list_strings


def specific_hyphen(sentence: str) -> list:
    """
    Returns the list of error messages if there are the mistakes
    with words that need to be written with a hyphen due to specific rule.
    """
    list_strings = []
    errors = {}
    prefix = "по"
    sufixes = "ому"
    if 'по' in sentence and 'ому' in sentence:
        pattern = re.findall(
            rf'(?<=[^\w-]){prefix}[^-][\w]*{sufixes}(?=[^\w-])', sentence)
        pattern += re.findall(
            rf'^{prefix}[^-][\w]*{sufixes}(?=[^\w-])', sentence)
        pattern += re.findall(
            rf'(?<=[^\w-]){prefix}[^-][\w]*{sufixes}$', sentence)
        pattern += re.findall(rf'^{prefix}[^-][\w]*{sufixes}$', sentence)
        for key in pattern:
            if re.fullmatch(r'по [чт]ому', key):
                pass
            elif re.fullmatch(r'по[чт]ому', key):
                errors[key] = re.sub(r'по', 'по ', key)
            else:
                errors[key] = re.sub(r'по\s?', 'по-', key)
    for key in errors:
        string = f'❌ {key} \n ✔️ {errors[key]}'
        list_strings.append(string)
    return list_strings


def write_with_hyphen(sentence: str) -> list:
    """
    Returns the list of error messages if there are the mistakes
    with words that need to be written with a hyphen.
    """
    list_strings = []
    errors = {}
    hyphen_prefixes = {'альфа', 'бета', 'гамма',
                       'дельта', 'казна', 'хтозна', 'бозна'}
    hyphen_sufixes = {'таки', 'небудь'}
    for prefix in hyphen_prefixes:
        if prefix in sentence:
            pattern = re.findall(
                rf'(?<=[^\w-]){prefix}[^-][\w]*(?=[^\w-])', sentence)
            pattern += re.findall(rf'^{prefix}[^-][\w]*(?=[^\w-])', sentence)
            pattern += re.findall(rf'(?<=[^\w-]){prefix}[^-][\w]*$', sentence)
            pattern += re.findall(rf'^{prefix}[^-][\w]*$', sentence)
            for key in pattern:
                errors[key] = re.sub(r'{prefix}\s?', rf'{prefix}-', key)

    for sufix in hyphen_sufixes:
        if sufix in sentence:
            pattern = re.findall(rf'^\w*[^-]{sufix}(?=[^\w-])', sentence)
            pattern += re.findall(
                rf'(?<=[^\w-])\w*[^-]{sufix}(?=[^\w-])', sentence)
            pattern += re.findall(rf'(?<=[^\w-])\w*[^-]{sufix}$', sentence)
            pattern += re.findall(rf'^\w*[^-]{sufix}$', sentence)
            for key in pattern:
                errors[key] = re.sub(rf'\s?{sufix}', rf'-{sufix}', key)
    for key in errors:
        string = f'❌ {key} \n ✔️ {errors[key]}'
        list_strings.append(string)
    return list_strings


def main_check(sentence: str) -> list or None:
    """
    Returns the list of error messages if there are the mistakes
    with words that need to be written with a hyphen or together.
    """
    sentence = sentence.lower()
    together_errors = write_together(sentence)
    hyphen_errors = write_with_hyphen(sentence)
    specific_hyphen_errors = specific_hyphen(sentence)
    list_of_errors = together_errors + hyphen_errors + specific_hyphen_errors
    return list_of_errors if list_of_errors else None
print(main_check('почому по чому'))