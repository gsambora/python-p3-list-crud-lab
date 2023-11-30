def create_an_empty_list():
    return []

def create_a_list():
    return ["meow", "woof", "neigh", "caw"]

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    new_list = [element]
    new_list.append(l)
    return new_list

def remove_element_from_end_of_list(l):
    return l[0:len(l)-1]

def remove_element_from_start_of_list(l):
    return l[1:len(l)]

def retrieve_first_element_from_list(l):
    return l[0]

def retrieve_element_from_index(l, index):
    return l[index]

def retrieve_last_element_from_list(l):
    return l[-1]
