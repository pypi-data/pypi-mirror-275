def parse_bool(bool_value: str|int|bool|None) -> bool | None:
    '''Description
    Parse and convert str, int to bool or return nothing if they are not

    :param bool_value:str|int|None  : Parameters considered boolean: true/false, on/off, 1/0, and others
    :return bool|None               : Returns the boolean value of the entered parameter or None if it is not
    '''

    true_values = {"yes", "true", "1", "on", "correct", "valid", "right"}
    false_values = {"no", "false", "0", "off", "incorrect", "invalid", "wrong"}

    if isinstance(bool_value,bool):
        return bool_value
    
    if isinstance(bool_value,int):
        if bool_value == 1:
            bool_value = "1"
        elif bool_value== 0:
            bool_value = "0"
        else:
            return None

    if isinstance(bool_value,str):
        bool_value = str(bool_value).lower()
        if bool_value in true_values:
            return True
        elif bool_value in false_values:
            return False
        else:
            return None

    return None