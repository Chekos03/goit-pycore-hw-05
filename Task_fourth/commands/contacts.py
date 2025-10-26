from .decorator import input_error

@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        return "Помилка: команда 'add' очікує 2 аргументи: add <ім'я> <телефон>."
    name, phone = args[0], args[1]
    key = name.lower()
    contacts[key] = {"name": name, "phone": phone}
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        return "Помилка: команда 'change' очікує 2 аргументи: change <ім'я> <новий_телефон>."
    name, new_phone = args[0], args[1]
    key = name.lower()
    if key not in contacts:
        return f"Помилка: контакт '{name}' не знайдено."
    contacts[key]["phone"] = new_phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    if len(args) < 1:
        return "Помилка: команда 'phone' очікує 1 аргумент: phone <ім'я>."
    name = args[0]
    key = name.lower()
    if key not in contacts:
        return f"Помилка: контакт '{name}' не знайдено."
    return contacts[key]["phone"]

@input_error
def show_all(contacts):
    if not contacts:
        return "Немає збережених контактів."
    lines = []
    for key in sorted(contacts.keys()):
        entry = contacts[key]
        lines.append(f"{entry['name']}: {entry['phone']}")
    return "\n".join(lines)