def title_case(title):
    t = title.split()
    cap_t = list(map(lambda x: x.capitalize(), t))
    capitalized = ' '.join(cap_t)
    return capitalized
