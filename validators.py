def check_fio(text):
    """Возвращает (фио, None) или (None, причина)."""
    parts = text.split()
    if len(parts) < 2:
        return None, "в ФИО меньше двух слов"
    return " ".join(parts).title(), None

def check_mail(text):
    """Возвращает (почта, None) или (None, причина)."""
    mail = text.strip().lower()
    error = "почта неверная: " + mail
    if mail.count("@") != 1:
        return None, error
    name, domain = mail.split("@")
    if name == "" or domain == "":
        return None, error
    if "." not in domain:
        return None, error
    if domain.startswith(".") or domain.endswith("."):
        return None, error
    return mail, None

def check_phone(text):
    """Возвращает (телефон, None) или (None, причина)."""
    digits = ""
    for ch in text:
        if ch.isdigit():
            digits += ch
    if len(digits) != 11:
        return None, "в телефоне " + str(len(digits)) + " цифр вместо 11"
    if digits[0] != "7" and digits[0] != "8":
        return None, "телефон должен начинаться с 7 или 8"
    phone = "+7 (" + digits[1:4] + ") " + digits[4:7] + "-" + digits[7:9] + "-" + digits[9:]
    return phone, None

def check_group(text):
    """Возвращает (группа, None) или (None, причина)."""
    group = text.replace(" ", "").lower()
    if group == "":
        return None, "группа не указана"
    return group, None

def parse_line(line):
    """Возвращает (анкета, None) или (None, причина отказа)."""
    fields = line.split(";")
    if len(fields) != 4:
        return None, "полей " + str(len(fields)) + " вместо 4"

    fio, err = check_fio(fields[0])
    if err:
        return None, err
    mail, err = check_mail(fields[1])
    if err:
        return None, err
    phone, err = check_phone(fields[2])
    if err:
        return None, err
    group, err = check_group(fields[3])
    if err:
        return None, err

    return {"fio": fio, "mail": mail, "phone": phone, "group": group}, None

if __name__ == "__main__":
    print(parse_line("иван иванов;ivan@mail.ru;+79211112233;09с33"))