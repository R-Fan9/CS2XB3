def are_valid_groups(student_numbers, groups):
    
    if(len(set(student_numbers)) != len(student_numbers)):
        return False

    for student in student_numbers:
        already_in_a_group = False
        valid = False
        if(type(student) is not type("")):
            return False
        for group in groups:
            if(len(group) > 3 or len(group) < 2):
                break
            if student in group and not already_in_a_group:
                valid = True
                already_in_a_group = True 
            elif student in group and already_in_a_group:
                valid = False
                break
        if not valid:
            break
        
    return valid