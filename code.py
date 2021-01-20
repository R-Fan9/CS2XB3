def are_valid_groups(students, groups):
    
    for student in students:
        valid = False
        in_group = False
        for i in range(len(groups)):
            if len(set(groups[i])) != len(groups[i]):
                break

            if student in groups[i] and not in_group:
                valid = True
                in_group = True

            elif student in groups[i] and in_group:
                valid = False
                break

        if not valid:
            break
    
    return valid
