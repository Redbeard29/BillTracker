def is_valid_input(cost):
    try:
        float(cost)
    except ValueError:
        return False
    else:
        return True

def valid_num_times(times):
    try:
        int(times)
    except ValueError:
        return False
    else:
        return True