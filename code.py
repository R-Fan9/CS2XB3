def are_valid_groups(student_numbers, groups):

    if(len(set(student_numbers)) != len(student_numbers)):
        return False
    
    for student in student_numbers:
        valid = False
        in_group = False
        
        if(type(student) is not type("")):
            return False

        for group in groups:
            if(len(group) > 3 or len(group) < 2):
                break

            if student in group and not in_group:
                valid = True
                in_group = True
            
            elif student in group and in_group:
                valid = False
                break

        if not valid:
            break

    return valid

    
