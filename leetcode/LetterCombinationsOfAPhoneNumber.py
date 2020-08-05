#!/usr/bin/env python
# coding=utf-8

def letterCombinations(digits):
    if '' == digits: return []
    kvmaps = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]],
                  digits, [''])


def letterCombinations2(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if not digits:
        return []
    dict = {"1": None, "2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
            "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

    def dfs(dict, string, index, path, res):
        if index == len(string):
            res.append(path)
            return
        for i in dict[string[index]]:
            dfs(dict, string, index + 1, path + i, res)

    res = []
    dfs(dict, digits, 0, "", res)
    return res


print letterCombinations2('23')