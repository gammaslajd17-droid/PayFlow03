def choose_payment():
    payments = ["Visa", "MasterCard", "PayPal"]

    print("Төлем түрін таңда:")
    for i, p in enumerate(payments, 1):
        print(f"{i}. {p}")

    choice = int(input("Санды енгіз: "))
    print(f"{payments[choice-1]} таңдалды ✅")
