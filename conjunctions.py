"""This module works with conjunctions and looks for punctuation errors
(if there is no comma before a conjunction)."""

import re


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
            errors.append(f'Перед "{word}" повинна стояти кома.')
    if errors:
        return errors
    return None
