import json

def load_data():
    try:
        with open('budget.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"total": 0}

def save_data(total):
    with open('budget.json', 'w') as f:
        json.dump({"total": total}, f)

def main():
    data = load_data()
    total = data["total"]

    while True:
        print(f"Текущая сумма: {total} 💰")
        
        action = input("Введите 'добавить', 'убавить' или 'выход': ").strip().lower()
        
        if action == 'добавить':
            amount = float(input("Введите сумму для добавления: "))
            total += amount
        elif action == 'убавить':
            amount = float(input("Введите сумму для убавления: "))
            total -= amount
        elif action == 'выход':
            save_data(total)
            print("До свидания! 👋")
            break
        else:
            print("Некорректное действие. Попробуйте снова.")

if __name__ == "__main__":
    main()

