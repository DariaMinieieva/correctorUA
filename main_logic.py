"""
This is main module with all the logic
for correctua bot
"""


def get_dictionary(path):
    with open(path, mode='r') as infile:
        dict_wrong_right = {}
        for line in infile:
            line = line.split("\t")
            dict_wrong_right[line[0]] = line[1].strip()
    return dict_wrong_right


# def check_for_mistake(messages):
#     path = "correctorUA/lexic1.csv"
#     data = get_dictionary(path)
#     corrected = messages
#     for key in data:
#         if key in messages:
#             ind_b = corrected.index(key)
#             ind_e = ind_b + len(key)
#             temp = corrected[:ind_b]
#             temp += data[key]
#             temp += corrected[ind_e:]
#             corrected = temp

#     return corrected

def check_for_mistake(messages):
    res = []
    path = "correctorUA/lexic_mistakes.csv"
    data = get_dictionary(path)

    messages = messages.lower()
    for key in data:
        if key in messages:
            res.append(f"❌ {key}\n✔️ {data[key]}")

    return res


if __name__ == "__main__":
    print(check_for_mistake(
        get_dictionary("correctorUA/lexic1.csv"), "Ми бурхливі овації за свою чудову головний лейтмотив."))
