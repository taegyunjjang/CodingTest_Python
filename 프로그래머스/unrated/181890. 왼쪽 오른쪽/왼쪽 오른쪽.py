def solution(str_list):
    if 'l' in str_list:
        idxL = str_list.index('l')
        if 'r' in str_list:
            idxR = str_list.index('r')
            if idxL < idxR:
                return str_list[:idxL]
            else:
                return str_list[idxR + 1:]
        else:
            return str_list[:idxL]
    else:
        if 'r' in str_list:
            idxR = str_list.index('r')
            return str_list[idxR + 1:]
        else:
            return []