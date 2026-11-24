
from manufacturing_utils import total_manufacturing_cost, defect_percentage
production = [
    (501, "circuit board", 100, 5, 250),
    (502, "power supply", 80, 12, 400),
    (503, "sensor", 150, 8, 180),
    (504, "controller", 60, 3, 650),
    (505, "connector", 200, 15, 50)
]

print("PRODUCTION RECORDS")

for batch in production:
    print(batch)


try:
    batch_id = int(input("Enter Batch ID: "))
    name = input("Enter product name: ")
    units = int(input("Enter units produced: "))
    defects = int(input("Enter defective units: "))
    cost = float(input("Enter cost per unit: "))

    if units < 0 or defects < 0 or cost < 0:
        raise ValueError("Negative values are not allowed!")

    if defects > units:
        raise ValueError("Defective units cannot exceed total units!")

except ValueError as e:
    print("Invalid input:", e)

else:
    new_batch = (batch_id, name, units, defects, cost)
    production.append(new_batch)
    print("New batch added successfully!")

finally:
    print("Batch entry process completed.")

print("\nTOTAL MANUFACTURING COST:")
print(total_manufacturing_cost(production))

print("\nOVERALL DEFECT PERCENTAGE:")
print(defect_percentage(production))

print("\nBATCHES WITH MORE THAN 10 DEFECTS:")

high_defects = list(filter(lambda batch: batch[3] > 10, production))

for batch in high_defects:
    print(batch)

print("\nACCEPTED PRODUCTION QUANTITIES:")

accepted = list(map(lambda batch: batch[2] - batch[3], production))

print(accepted)

print("\nCOST OF EACH BATCH:")

batch_cost = list(map(lambda batch: batch[2] * batch[4], production))

print(batch_cost)

