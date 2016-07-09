from itertools import permutations

def get_num_from_string(s, mapping):
    return int(''.join([mapping.get(i, i) for i in s]))

def print_mapping(mapping):
    for k, v in mapping.iteritems():
        print k + ' = ' + v + ',  ',
    print

def cryptogram_sum(arr_s, res):
    # cryptogram_sum(['SEND', 'MORE'], 'MONEY')
    numbers = {str(i) for i in xrange(10)}
    letters = list(set(i for i in ''.join(arr_s + [res]) if i not in numbers))

    no_zero_letters = [i[0] for i in arr_s + [res] if i[0] in letters]
    for letters_attempt in permutations('0123456789', len(letters)):
        mapping = {letter: letters_attempt[i] for i, letter in enumerate(letters)}
        tmp1 = sum(get_num_from_string(el, mapping) for el in arr_s)
        if tmp1 == get_num_from_string(res, mapping) and not any(mapping[i] == '0' for i in no_zero_letters):
            print_mapping(mapping)

def cryptogram_mul(arr_s, res):
    # cryptogram_mul(['ABCD', 'E'], 'FGHI')
    numbers = {str(i) for i in xrange(10)}
    letters = list(set(i for i in ''.join(arr_s + [res]) if i not in numbers))

    no_zero_letters = [i[0] for i in arr_s + [res] if i[0] in letters]
    for letters_attempt in permutations('0123456789', len(letters)):
        mapping = {letter: letters_attempt[i] for i, letter in enumerate(letters)}
        tmp1 = reduce(lambda x, y: x*y, [get_num_from_string(el, mapping) for el in arr_s])
        if tmp1 == get_num_from_string(res, mapping) and not any(mapping[i] == '0' for i in no_zero_letters):
            print_mapping(mapping)

cryptogram_sum(['XYZ', 'XYZ', 'XYZ'], 'ZZZ')
cryptogram_mul(['ABC', '8'], 'ACCC')