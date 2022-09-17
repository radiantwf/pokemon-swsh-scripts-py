import os
import io
import time
import random

random.seed(time.time())
S_IFDIR = const(16384)
MACRO_BASE_PATH = "/resources/macros"
MACRO_EXT = ".m"


def get_marcos(base=MACRO_BASE_PATH):
    ret = []
    for p in os.listdir(base):
        path = "{}/{}".format(base, p)
        if p.startswith('.'):
            continue
        elif p.lower().endswith(MACRO_EXT):
            ret.append(path)
        elif (os.stat(path)[0] & S_IFDIR):
            ret.extend(get_marcos(path))
    return ret


def load_file(filename, dic=dict()) -> dict:
    try:
        f = open(filename, "rt")
    except:
        return dic

    file_tag = filename[len(MACRO_BASE_PATH) + 1:(
        len(filename) - len(MACRO_EXT))].replace("/", ".", -1) + "."
    rows = []
    while True:
        row = f.readline()
        if row == "":
            break
        row = row.strip()
        if row == "":
            continue
        elif row.startswith("--") or row.startswith("#"):
            continue
        row = row.replace(" ", "", -1).replace("\t", "", -1)
        if row.startswith("[") and row.count(".") == 0:
            row = "[" + file_tag + row[1:]
        rows.append(row)
    if len(rows) > 0:
        dic = read_segments(rows, dic=dic, file_tag=file_tag)
    f.close()
    return dic


def read_segments(src_rows, dic=dict(), file_tag: str = "", name: str = "") -> dict:
    rows = []
    sub_rows = []
    sub = False
    sub_floor = 0
    if name != "":
        debug = True
    for row in src_rows:
        if row.startswith("<") and row.endswith(">"):
            if len(rows) > 0:
                if name != "":
                    dic[name] = rows
                rows = []
            name = file_tag + row[1:len(row)-1]
            sub_rows = []
            sub = False
            continue
        elif sub:
            pass
        elif row.startswith("{"):
            sub = True
            row = row[1:]
        if sub:
            str_io = io.StringIO()
            for index in range(0, len(row)):
                if row[index] == "}" and sub_floor == 0:
                    sub_row = str_io.getvalue()
                    if len(sub_row) > 0:
                        sub_rows.append(sub_row)
                    if len(sub_rows) == 0:
                        sub = False
                        break
                    sub_name = hex(random.randint(1, time.time()))
                    if index < len(row) - 1:
                        ends = row[index + 1:]
                    line = "[{}]{}".format(sub_name, ends)
                    rows.append(line)
                    dic = read_segments(sub_rows, dic=dic,
                                        file_tag="", name=sub_name)
                    sub_rows = []
                    sub = False
                    break
                elif row[index] == "}" and sub_floor > 0:
                    sub_floor -= 1
                elif row[index] == "{":
                    sub_floor += 1
                str_io.write(row[index])
            if sub:
                sub_row = str_io.getvalue()
                if len(sub_row) > 0:
                    sub_rows.append(sub_row)
            str_io.close()
        else:
            rows.append(row)
    if len(rows) > 0 and name != "":
        dic[name] = rows
    return dic


macros = get_marcos()
dic = dict()
for macro in macros:
    dic = load_file(macro, dic)
# for key in dic.keys():
#     print(key)
#     print(dic[key])
