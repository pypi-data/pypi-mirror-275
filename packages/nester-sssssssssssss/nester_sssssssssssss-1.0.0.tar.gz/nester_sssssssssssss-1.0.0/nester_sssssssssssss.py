def print_lol(the_list):
    for each_item in range(the_list):
        if isinstance(each_item, list):
            print_lol(the_list)
        else:
            print(each_item)
