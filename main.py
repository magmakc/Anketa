from validators import parse_line
from report import print_table, print_bad, print_stat
from storage import IN_FILE, OK_FILE, ERR_FILE, read_lines, save_files

def main():
    lines = read_lines(IN_FILE)
    if lines is None:
        print("Файл " + IN_FILE + " не найден")
        return

    good = []
    bad = []
    empty = 0
    for num, line in enumerate(lines, 1):
        line = line.strip()
        if line == "":
            empty += 1
            continue
        anketa, reason = parse_line(line)
        if reason:
            bad.append((num, line, reason))
        else:
            good.append(anketa)

    good.sort(key=lambda a: a["fio"])

    print_table(good)
    print()
    print_bad(bad)
    print()
    print("Всего строк в файле:", len(lines), "(пустых строк:", str(empty) + ")")
    print("Принято:", len(good), "| Отклонено:", len(bad))
    print()
    print_stat(good)
    print()
    save_files(good, bad)
    print("Сохранено: " + OK_FILE + " и " + ERR_FILE)

if __name__ == "__main__":
    main()