def mask_phone(phone):
    # +7 (921) 111-22-33  ->  +7 (921) ***-**-33
    return phone[:9] + "***-**-" + phone[-2:]

def print_table(good):
    line = "-" * 83
    print(f"{'№':>3}  {'ФИО':<28}{'Почта':<22}{'Телефон':<20}{'Группа'}")
    print(line)
    for i, a in enumerate(good, 1):
        print(f"{i:>3}  {a['fio'][:27]:<28}{a['mail'][:21]:<22}"
              f"{mask_phone(a['phone']):<20}{a['group']}")
    print(line)

def print_bad(bad):
    print("Отклонено строк:", len(bad))
    for num, line, reason in bad:
        print("  строка " + str(num) + ": " + reason)
        print("      " + line)

def print_stat(good):
    stat = {}
    for a in good:
        stat[a["group"]] = stat.get(a["group"], 0) + 1
    print("По группам:")
    for group in sorted(stat):
        print(f"  {group:<8}{stat[group]}")

if __name__ == "__main__":
    print(mask_phone("+7 (921) 111-22-33"))