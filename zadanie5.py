i = float(input("enter a profit  "))
z = float(input("enter the costs "))
if i > z:Введите издержки фирмы
    print(f"Firm work with cost. rentable is {i / z:.2f}")
    w = int(input("enter number of employees"))
    print(f"profit for one employ is {i / z:.2f}")
elif i == z:
    print("Firm work to zero")
else:
    print("firm work to lesion")