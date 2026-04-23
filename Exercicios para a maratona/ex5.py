def inverter_string(s):
    if len(s) <= 1:
        return s
    return s[-1] + inverter_string(s[:-1])