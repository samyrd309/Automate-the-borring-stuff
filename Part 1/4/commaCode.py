def comaCode(list):
    if len(list) == 0:
        return "" # Return empty string
    elif len(list) == 1:
        return list[0] # Return just the element
    elif len(list) == 2:
        return list[0] + ' and ' + list[1] # Return just two elements
    else:
        # Obtener la sublista para la coma
        item_with_comas = list[:-1]
        # Unir sublista con ", "
        main_string = ", ".join(item_with_comas)
        # Obtener ultimo elemnte
        last_item = list[-1]
        return main_string + ", and " + last_item

print(comaCode([]))
print(comaCode(["A"]))
print(comaCode(["A", "B"]))
print(comaCode(["A", "B", "C"]))