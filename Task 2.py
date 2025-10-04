list = [i for i in range(1,11)]
list2 = (list[:5])
list2.reverse()
print("Orginal list: {}".format(list))
print("Extracted first five elements: {}".format(list[:5]))
print("Reversed extracted elements: {}".format(list2))
