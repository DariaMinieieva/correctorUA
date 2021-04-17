"""This module discovers the rules of adverbs writing and checks the sentences for it."""

import re

def write_together(sentence: str) -> list:
    """Returns the list of error messages if there are the mistakes 
    with words that need to be written together."""
    errors = []
    together_prefixes = {'абро', 'авіа', 'авто', 'агро', 'аеро', 'аква', 'алко', 'анти', \
    'арт', 'астро', 'аудіо', 'біо', 'боди', 'веб', 'віце', 'геліо', 'гео', 'гідро', 'гіпер', \
    'дендро', 'екзо', 'еко', 'економ', 'екс', 'етно', 'євро', 'зоо', 'ізо', 'кібер', 'контр', \
    'мета', 'метео', 'моно', 'мото', 'нарко', 'нео', 'онко', 'палео', 'пан', 'пара', 'поп', \
    'прес', 'псевдо', 'соціо', 'теле', 'фіто', 'фолк', 'фольк', 'фоно', 'архі', 'архи', 'бліц', \
    'гіпер', 'екстра', 'макро', 'максі', 'міді', 'мікро', 'міні', 'мульти', 'нано', 'полі', \
    'преміум', 'супер', 'топ', 'ультра', 'флеш', 'напів', 'аби', 'ані', 'де'}
    for prefix in together_prefixes:
        pattern = rf'^(.* )*{prefix}[^\w].*'
        if re.fullmatch(pattern, sentence):
            errors.append(f'Слова з префіксом "{prefix}" пишуться разом.')
    return errors


def specific_hyphen(sentence: str) -> list:
    """Returns the list of error messages if there are the mistakes 
    with words that need to be written with a hyphen due to specific rule."""
    errors = []
    prefix = "по"
    sufixes = ("ому", "и")
    pattern = rf'(.* )*{prefix}[^-]([^ ]+)?({sufixes[0]}|{sufixes[1]}).*'
    if re.fullmatch(pattern, sentence):
        errors.append(f'Слова з префіксом "{prefix}" й суфіксами "{sufixes[0]}" та \
"{sufixes[1]}" пишуться через дефіс.')
    return errors


def write_with_hyphen(sentence: str) -> list:
    """Returns the list of error messages if there are the mistakes 
    with words that need to be written with a hyphen."""
    errors = []
    hyphen_prefixes = {'альфа', 'бета', 'дельта', 'казна', 'хтозна', 'бозна'}
    hyphen_sufixes = {'таки', 'небудь'}
    for prefix in hyphen_prefixes:
        prefix_pattern = rf'^(.* )*{prefix}[^-].*'
        if re.fullmatch(prefix_pattern, sentence):
            errors.append(f'Слова з префіксом "{prefix}" пишуться через дефіс.')
    for sufix in hyphen_sufixes:
        sufix_pattern = rf'.*[^-]{sufix}( .*)?'
        if re.fullmatch(sufix_pattern, sentence):
            errors.append(f'Слова з суфіксом "{sufix}" пишуться через дефіс.')
    return errors


def main_check(sentence: str) -> list or None:
    """Returns the list of error messages if there are the mistakes 
    with words that need to be written with a hyphen or together."""
    sentence = sentence.lower()
    together_errors = write_together(sentence)
    hyphen_errors = write_with_hyphen(sentence)
    specific_hyphen_errors = specific_hyphen(sentence)
    errors = together_errors + hyphen_errors + specific_hyphen_errors
    return errors if errors else None
