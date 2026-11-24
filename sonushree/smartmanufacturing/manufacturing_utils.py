
def total_manufacturing_cost(production):
    total = 0
    for batch in production:
        total = total + (batch[2] * batch[4])
    return total


def defect_percentage(production):
    total_units = 0
    total_defects = 0

    for batch in production:
        total_units += batch[2]
        total_defects += batch[3]

    if total_units == 0:
        return 0

    return (total_defects / total_units) * 100
