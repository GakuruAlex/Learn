def convert2range(v, f_min, f_max,t_min, t_max):
    return round(t_min + (t_max - t_min) * ((v - f_min) / (f_max - f_min)),2)