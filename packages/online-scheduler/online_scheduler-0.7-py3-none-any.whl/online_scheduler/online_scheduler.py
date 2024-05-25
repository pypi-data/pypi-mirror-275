import os
import csv
import webbrowser

def main():
    if not os.path.exists("url.csv"):
        create_empty_csv()

    matrix = load_schedule_from_csv()

    Num = ["1限 |", "2限 |", "3限 |", "4限 |", "5限 |", "6限 |"]
    Mon = ["10", "11", "12", "13", "14", "15"]
    Tue = ["20", "21", "22", "23", "24", "25"]
    Wed = ["30", "31", "32", "33", "34", "35"]
    Thu = ["40", "41", "42", "43", "44", "45"]
    Fri = ["50", "51", "52", "53", "54", "55"]
    sch = [Num, Mon, Tue, Wed, Thu, Fri]

    row = len(sch)
    col = len(sch[0])

    print_schedule(matrix, sch)

    print("編集⇨ a\t編集終了⇨ w\tマスを入力⇨ ブラウザを起動")
    a = input()

    if a == "a":
        edit_schedule(matrix, sch)
    else:
        open_browser(matrix, a)

def create_empty_csv():
    with open("url.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows([[""] * 6] * 6)
    print("url.csvを作成したので起動し直してください")

def load_schedule_from_csv():
    matrix = []
    with open("url.csv", "r") as f:
        for line in f:
            data = line.rstrip("\n").split(",")
            matrix.append(data)
    return matrix

def print_schedule(matrix, sch):
    print("時限\t月\t火\t水\t木\t金")
    print("-------------------------------------------------")
    for j in range(len(sch)):
        for i in range(len(sch[0])):
            if len(matrix[i][j]) >= 3:
                sch[i][j] = "\033[34m" + sch[i][j] + "\033[0m"
            print(sch[i][j], end="\t")
        print("")

def edit_schedule(matrix, sch):
    while True:
        print("マスを選択 or w")
        a = input()
        if a == "w":
            save_schedule_to_csv(matrix)
            break
        else:
            b = int(a[0])
            c = int(a[1])
            print("URLを貼り付けor エンターキーで削除 ")
            d = input()
            matrix[b][c] = d
            if len(d) == 0:
                sch[b][c] = "\033[0m" + sch[b][c] + "\033[0m"
            else:
                sch[b][c] = "\033[34m" + sch[b][c] + "\033[0m"
            print_schedule(matrix, sch)

def save_schedule_to_csv(matrix):
    with open("url.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(matrix)

def open_browser(matrix, a):
    b = int(a[0])
    c = int(a[1])
    webbrowser.open(matrix[b][c], 2)

if __name__ == "__main__":
    main()
