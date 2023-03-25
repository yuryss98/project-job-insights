def verify_keys(job: dict):
    keys = job.keys()
    keys_valid = ["max_salary", "min_salary"]

    if len(keys) < 2:
        raise ValueError()

    for key in keys:
        if key not in keys_valid:
            raise ValueError()


def verify_values(values: list):
    for value in values:
        if type(int(value)) != int:
            raise ValueError()

    if int(values[0]) < int(values[1]):
        raise ValueError()
