year = int(input())

year_sign = {2000: "Дракон", 2001: "Змея", 2002: "Лошадь", 2003: "Коза", 2004: "Обезьяна", 2005: "Петух",
             2006: "Собака", 2007: "Свинья", 2008: "Крыса", 2009: "Бык", 2010: "Тигр", 2011: "Кролик"}

if year in year_sign:
    print(year_sign[year])
else:
    while year not in year_sign:
        year -= 12
    print(year_sign[year])
