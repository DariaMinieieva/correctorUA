"""
Module contains function to check if adjectives are written correctly.
(without самий, сама, саме, самі)
but firstly you have to:
pip install pymorphy2
pip install -U pymorphy2-dicts-uk
"""
from pymorphy2 import MorphAnalyzer
morph = MorphAnalyzer(lang='uk')


def check_adj(message: str) -> list:
    """
    >>> check_adj('самий вищий')
    ['❌ самий вищий\n✔️ потрібно використовувати префікс най-']
    >>> check_adj('сама краща', 'самі веселі')
    ['❌ сама краща\n✔️ потрібно використовувати префікс най-', '❌ самі веселі\n✔️ потрібно використовувати префікс най-']
    >>> check_adj('саме довге')
    ['❌ самий довге\n✔️ потрібно використовувати префікс най-']
    """
    result = []
    sentence = message.lower().replace(',', '').split(' ')
    for i in range(len(sentence) - 1):
        if sentence[i] in {'самий', 'сама', 'самі'}:
            check_word = sentence[i + 1]
            check = morph.parse(check_word)[0]
            if check.tag.POS in {'ADJF', 'ADJS', 'COMP', 'PRTS', 'PRTN'}:
                result.append(
                    f"❌ {sentence[i]} {check_word}\n✔️ потрібно використовувати префікс най-")
        elif sentence[i] == 'саме':
            check_word = sentence[i + 1]
            check = morph.parse(check_word)[0]
            if check.tag.POS in {'ADJF', 'ADJS', 'COMP', 'PRTS', 'PRTN', 'ADVB'}:
                result.append(
                    f"❌ самий {check_word}\n✔️ потрібно використовувати префікс най-")
    return result if result else None
