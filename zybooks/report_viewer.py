import csv
with open("UNDCSCI160StokkeSpring2022_report_Kenneth_Jahnke_2022-02"
          "-08_1843_CST.csv") as f:
    reader = csv.DictReader(f)

    for info in reader:
        for key, value in info.items():
            if key in ["Last name", "First name", "Primary email"]:
                pass
            else:
                first_col_width = 0
                for i in info.keys():
                    if len(i) > first_col_width:
                        first_col_width = len(i) + 3
                print((key + " " * (first_col_width - len(key))), value)


# All work and no play makes Jack a dull boy.
