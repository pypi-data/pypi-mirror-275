import os
import csv
import webbrowser

class ScheduleManager:
    def __init__(self):
        if not os.path.exists("url.csv"):
            self.create_empty_schedule()
            print("url.csvを作成したので起動し直してください")
            quit()

        self.matrix = self.load_schedule_from_csv()
        self.sch = [
            ["1限 |", "2限 |", "3限 |", "4限 |", "5限 |", "6限 |"],
            ["10", "11", "12", "13", "14", "15"],
            ["20", "21", "22", "23", "24", "25"],
            ["30", "31", "32", "33", "34", "35"],
            ["40", "41", "42", "43", "44", "45"],
            ["50", "51", "52", "53", "54", "55"]
        ]
        self.row = len(self.sch)
        self.col = len(self.sch[0])

    def create_empty_schedule(self):
        with open("url.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows([[""] * 6] * 6)

    def load_schedule_from_csv(self):
        matrix = []
        with open("url.csv", "r") as f:
            for line in f:
                data = line.rstrip("\n").split(",")
                matrix.append(data)
        return matrix

    def display_schedule(self):
        print("時限\t月\t火\t水\t木\t金")
        print("-------------------------------------------------")
        for j in range(self.row):
            for i in range(self.col):
                if len(self.matrix[i][j]) >= 3:
                    self.sch[i][j] = "\033[34m" + self.sch[i][j] + "\033[0m"
                print(self.sch[i][j], end="\t")
            print("")

    def edit_schedule(self):
        while True:
            print("マスを選択 or w")
            a = input()
            if a == "w":
                self.save_schedule_to_csv()
                break
            else:
                b = int(a[0])
                c = int(a[1])
                print("URLを貼り付けor エンターキーで削除 ")
                d = input()
                self.matrix[b][c] = d
                if len(d) == 0:
                    self.sch[b][c] = "\033[0m" + self.sch[b][c] + "\033[0m"
                else:
                    self.sch[b][c] = "\033[34m" + self.sch[b][c] + "\033[0m"
                self.display_schedule()

    def save_schedule_to_csv(self):
        with open("url.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(self.matrix)

    def run(self):
        self.display_schedule()
        print("編集⇨ a\t編集終了⇨ w\tマスを入力⇨ ブラウザを起動")

        action = input()
        if action == "a":
            self.edit_schedule()
        else:
            b = int(action[0])
            c = int(action[1])
            webbrowser.open(self.matrix[b][c], 2)

if __name__ == "__main__":
    schedule_manager = ScheduleManager()
    schedule_manager.run()
