import itertools as it


def implies(x, y):
    return not x or y


def is_valid_free(domain, free_value):
    return any(x[1] == free_value for x in domain)


def f1(domain, _):
    return all(implies(x[0], x[1]) for x in domain)


def f2(domain, free):
    return implies(all(x[0] for x in domain), free)


def f3(domain, _):
    return any(implies(x[0], x[1]) for x in domain)


def f4(domain, free):
    return implies(any(x[0] for x in domain), free)


def create_domains(sz: int):
    valuations = list(it.product((False, True), repeat=2))
    domains = []
    for domain in it.product(valuations, repeat=sz):
        domains.append(list(domain))
    return domains


def logically_implies(f1, f2, domains):
    free_values = [True, False]
    
    ans = True
    for free_value in free_values:
        cur_ans = all(not is_valid_free(domain, free_value) or implies(f1(domain, free_value), f2(domain, free_value)) for domain in domains)
        ans = ans and cur_ans
    print(["No", "Yes"][ans])


def main():
    domains = create_domains(4)
    logically_implies(f1, f2, domains)
    logically_implies(f1, f3, domains)
    logically_implies(f1, f4, domains)
    logically_implies(f2, f1, domains)
    logically_implies(f2, f3, domains)
    logically_implies(f2, f4, domains)
    logically_implies(f3, f1, domains)
    logically_implies(f3, f2, domains)
    logically_implies(f3, f4, domains)
    logically_implies(f4, f1, domains)
    logically_implies(f4, f2, domains)
    logically_implies(f4, f3, domains)



main()