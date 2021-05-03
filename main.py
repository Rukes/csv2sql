def remove_quotes(str):
    if str.startswith('"') and str.endswith('"'):
        str = str[1:]
        str = str[:-1]
    return str


file_path = input("input file name (in current folder): ")
delim = input("input csv delimiter: ")
first_line_header = input("first line header? [y/n]: ")
table_name = input("sql table name: ")
col_names = {}

while True:
    col_name = input("input column name (empty = end): ")
    if col_name != "":
        col_index = input(f"input column index for {col_name}: ")
        if col_index != "":
            col_names[col_name] = col_index
        else:
            continue
    else:
        break

print_or_save = input("print or save result? [p/s]: ")

print("\n\nProccessing...\n\n")

table_val = "("
for col in col_names:
    table_val += "`" + col + "`, "
table_val = table_val[:-2]
table_val += ")"

file = open(file_path, "r")
writer = None
if print_or_save == "s":
    writer = open("output_file.txt", "w")
first = True
i = 0
for fline in file:
    if first and first_line_header == "y":
        first = False
        continue
    csv = fline.split(delim)
    value = "("
    for col in col_names:
        index = int(col_names[col])
        value += "'" + csv[index].rstrip() + "', "
    value = value[:-2]
    value += ")"
    text = "INSERT INTO `"+table_name+"` " + table_val + " VALUES " + value + ";"
    if writer is None:
        print(text)
    else:
        writer.write(text + "\n")
    i += 1

print("[!] Proccess done [!]")
print(f"[.] Rows: {i}")
