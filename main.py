
def read_file(path):
    file_contents = None
    with open(path) as f:
        file_contents = f.read()
    return file_contents
def count_words(string):
    return len(string.split())
def count_characters(string):
    lower_string = string.lower()
    result_dict = {}
    for i in lower_string:
        if i not in result_dict:
            result_dict[i] = 1
        else:
            result_dict[i] += 1
    return result_dict
def convert_to_list_of_dict(dict):
    dict_list = []
    for key, val in dict.items():
        if not key.isalpha():
            continue
        dict = {}
        dict["name"] = key
        dict["num"] = val
        dict_list.append(dict)
    return dict_list

def sort_on(dict):
    return dict["num"]
    
def main():
    path = "books/frankenstein.txt"
    contents = read_file(path)
    num_words = count_words(contents)
    num_char = count_characters(contents)
    dict_list = convert_to_list_of_dict(num_char)
    print(dict_list)
    dict_list.sort(reverse=True, key=sort_on)
    print(dict_list)
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    for dict in dict_list:
        key = dict["name"]
        val = dict["num"]
        print(f"The '{key}' character was found {val} times")
    print("--- End report ---")


main()