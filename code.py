def are_valid_groups(student_numbers, groups):
    for student in student_numbers:
        has_a_group=False
        for group in groups:
            if student in group:
                has_a_group=True
                break 
        if not has_a_group:
            return
    return True

    
