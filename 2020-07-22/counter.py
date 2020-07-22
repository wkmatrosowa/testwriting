def count(string):
    string_list = [char for char in string]
    return {char:string_list.count(char) for char in string_list}