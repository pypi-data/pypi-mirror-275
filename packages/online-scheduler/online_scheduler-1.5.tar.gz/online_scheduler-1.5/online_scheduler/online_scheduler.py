import os
import csv
import webbrowser

def main():
    if not os.path.exists("url.csv"):
        f = open("url.csv", "w", newline="")
        data1 = [["", "", "", "", "", ""],
                 ["", "", "", "", "", ""],
                 ["", "", "", "", "", ""],
                 ["", "", "", "", "", ""],
                 ["", "", "", "", "", ""],
                 ["", "", "", "", "", ""]]
        writer = csv.writer(f)
        writer.writerows(data1)
        f.close()
        print("url.csvを作成したので起動し直してください")
        quit()

    matrix = []
    f = open("url.csv", "r")
    while True:
        data = f.readline()
        if data == "":
            break
        data = data.rstrip("\n")
        line = data.split(",")
        matrix.append(line)
    f.close()

    Num = ["1限 |", "2限 |", "3限 |", "4限 |", "5限 |", "6限 |"]
    Mon = ["10", "11", "12", "13", "14", "15"]
    Tue = ["20", "21", "22", "23", "24", "25"]
    Wed = ["30", "31", "32", "33", "34", "35"]
    Thu = ["40", "41", "42", "43", "44", "45"]
    Fri = ["50", "51", "52", "53", "54", "55"]
    sch = [Num, Mon, Tue, Wed, Thu, Fri]

    row = len(sch)
    col = len(sch[0])

    print("時限\t月\t火\t水\t木\t金")
    print("-------------------------------------------------")
    for j in range(row):
        for i in range(col):
            if int(len(matrix[i][j])) >= 3:
                print("\033[34m" + sch[i][j], end="\t")
            else:
                print("\033[0m" + sch[i][j], end="\t")
        print("")
    print("編集⇨ a\t編集終了⇨ q\tマスを入力⇨ ブラウザを起動")

    a = input()
    if a == "a":
        f = open("url.csv", "w", newline="")
        while True:
            print("マスを選択 or q")
            a = input()
            if a == "q":
                writer = csv.writer(f)
                writer.writerows(matrix)
                f.close()
                break
                quit()
            else:
                b = a[0]
                c = a[1]
                print("URLを貼り付けor エンターキーで削除 ")
                d = input()
                matrix[int(b)][int(c)] = d
                print("時限\t月\t火\t水\t木\t金")
                print("-------------------------------------------------")
                for j in range(row):
                    for i in range(col):
                        if len(matrix[i][j]) <= 4:
                            print("\033[0m" + sch[i][j], end="\t")
                        else:
                            print("\033[34m" + sch[i][j], end="\t")
                    print("")
    elif a == "q":
        quit()
    else:
        b = a[0]
        c = a[1]
        webbrowser.open(matrix[int(b)][int(c)], 2)

if __name__ == "__main__":
    main()

