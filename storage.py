IN_FILE = "anketa.txt"
OK_FILE = "ok.txt"
ERR_FILE = "errors.txt"

def read_lines(name):
    try:
        f = open(name, "r", encoding="utf-8")
    except FileNotFoundError:
        return None
    lines = f.read().split("\n")
    f.close()
    return lines

def save_files(good, bad):
    f = open(OK_FILE, "w", encoding="utf-8")
    for a in good:
        f.write(a["fio"] + ";" + a["mail"] + ";" + a["phone"] + ";" + a["group"] + "\n")
    f.close()

    f = open(ERR_FILE, "w", encoding="utf-8")
    for num, line, reason in bad:
        f.write("строка " + str(num) + ": " + reason + " | " + line + "\n")
    f.close()

if __name__ == "__main__":
    print(read_lines(IN_FILE))