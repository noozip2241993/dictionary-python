def mapping_two_lists(l1,l2):
    """Write a Python program to map two lists into a dictionary."""
    return dict(zip(l1,l2))
list1 = ['Khang','Trang','Me','Ba']
list2 = ['Jack','Kristy','Tho','Ninh']
print(mapping_two_lists(list1,list2))