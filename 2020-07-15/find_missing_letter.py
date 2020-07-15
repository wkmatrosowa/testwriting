from string import ascii_lowercase, ascii_uppercase
def find_missing_letter(chars):
    lowercase = [char for char in ascii_lowercase]
    uppercase = [char for char in ascii_uppercase]
    lowercase_set = set(lowercase)
    uppercase_set = set(uppercase)
    indeces_l = [i for i, el in enumerate(lowercase) if el in chars and lowercase_set.issuperset(set(chars))]
    indeces_u = [i for i, el in enumerate(uppercase) if el in chars and uppercase_set.issuperset(set(chars))]
    if indeces_l != []:
        all_indeces = [x for x in range(indeces_l[0], indeces_l[-1]+1)]
        one_index = [num for num in all_indeces if num not in indeces_l]
        return lowercase[one_index[0]]
    else:
        all_indeces = [x for x in range(indeces_u[0], indeces_u[-1]+1)]
        one_index = [num for num in all_indeces if num not in indeces_u]
        return uppercase[one_index[0]]