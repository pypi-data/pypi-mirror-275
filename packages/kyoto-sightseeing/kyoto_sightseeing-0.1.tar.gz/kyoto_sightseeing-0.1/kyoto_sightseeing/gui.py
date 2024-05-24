import tkinter as tk
from tkinter import messagebox, Scrollbar
from tkinter.ttk import Frame
from kyoto_sightseeing.route_planner import plan_route, calculate_distance
from kyoto_sightseeing.coordinates import get_coordinates, coordinates

class KyotoSightseeingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("京都旅行最短ルート")
        
        self.num_days = 0
        self.sightseeing_entries = []
        self.accommodations_entries = []

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="京都旅行最短ルート", font=("Arial", 18))
        title.pack()

        note = tk.Label(self.root, text="※入力は漢字で答えてください")
        note.pack()

        self.num_days_label = tk.Label(self.root, text="宿泊日数：n泊n+1日")
        self.num_days_label.pack()
        self.num_days_entry = tk.Entry(self.root)
        self.num_days_entry.pack()

        self.num_days_entry.bind('<FocusOut>', self.update_accommodation_entries)

        self.start_label = tk.Label(self.root, text="開始地点：")
        self.start_label.pack()
        self.start_entry = tk.Entry(self.root)
        self.start_entry.pack()

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(fill=tk.BOTH, expand=True)

        self.accommodations_frame = tk.Frame(self.input_frame)
        self.accommodations_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.sightseeing_frame = tk.Frame(self.input_frame)
        self.sightseeing_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.add_sightseeing_entry()

        self.end_label = tk.Label(self.root, text="最終地点：")
        self.end_label.pack()
        self.end_entry = tk.Entry(self.root)
        self.end_entry.pack()

        self.calculate_button = tk.Button(self.root, text="最短ルートを計算", command=self.calculate_route)
        self.calculate_button.pack()

        self.result_frame = tk.Frame(self.root)
        self.result_frame.pack(fill=tk.BOTH, expand=True)
        
        self.result_text = tk.Text(self.result_frame, height=10, width=50, wrap=tk.WORD)
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.scrollbar = Scrollbar(self.result_frame, command=self.result_text.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text['yscrollcommand'] = self.scrollbar.set

    def update_accommodation_entries(self, event):
        try:
            new_num_days = int(self.num_days_entry.get())
        except ValueError:
            return
        
        if new_num_days != self.num_days:
            self.num_days = new_num_days
            for widget in self.accommodations_frame.winfo_children():
                widget.destroy()

            self.accommodations_entries = []
            for i in range(1, self.num_days + 1):
                label = tk.Label(self.accommodations_frame, text=f"{i}日目宿泊予定地：")
                label.pack()
                entry = tk.Entry(self.accommodations_frame)
                entry.pack()
                self.accommodations_entries.append(entry)

    def add_sightseeing_entry(self):
        index = len(self.sightseeing_entries) + 1
        label = tk.Label(self.sightseeing_frame, text=f"回りたい観光地{index}：")
        label.pack()
        entry = tk.Entry(self.sightseeing_frame)
        entry.pack()
        self.sightseeing_entries.append(entry)
        entry.bind('<FocusOut>', self.check_sightseeing_entries)

    def check_sightseeing_entries(self, event):
        last_entry = self.sightseeing_entries[-1]
        if last_entry.get():
            self.add_sightseeing_entry()

    def calculate_route(self):
        try:
            num_days = int(self.num_days_entry.get())
        except ValueError:
            messagebox.showerror("エラー", "宿泊日数は整数で入力してください。")
            return
        
        start = self.start_entry.get()
        end = self.end_entry.get()
        
        if not get_coordinates(start):
            messagebox.showerror("エラー", f"開始地点 {start} の座標が見つかりません。")
            return
        
        if not get_coordinates(end):
            messagebox.showerror("エラー", f"最終地点 {end} の座標が見つかりません。")
            return

        accommodations = [entry.get() for entry in self.accommodations_entries if entry.get()]
        for accommodation in accommodations:
            if not get_coordinates(accommodation):
                messagebox.showerror("エラー", f"宿泊予定地 {accommodation} の座標が見つかりません。")
                return

        sightseeing = [entry.get() for entry in self.sightseeing_entries if entry.get()]
        for place in sightseeing:
            if not get_coordinates(place):
                messagebox.showerror("エラー", f"観光地 {place} の座標が見つかりません。")
                return

        routes = plan_route(start, end, sightseeing, num_days, accommodations)
        
        self.result_text.delete(1.0, tk.END)
        total_distance = 0
        for i, day_route in enumerate(routes):
            day_text = f"Day {i + 1}:\n"
            day_distance = 0
            for j in range(len(day_route) - 1):
                from_place = next(key for key, value in coordinates.items() if value == day_route[j])
                to_place = next(key for key, value in coordinates.items() if value == day_route[j + 1])
                distance = calculate_distance(day_route[j], day_route[j + 1])
                day_distance += distance
                day_text += f"{from_place} -> "
            day_text += f"{to_place}\n"
            day_text += f"約 {day_distance:.2f} km\n"
            total_distance += day_distance
            self.result_text.insert(tk.END, day_text)

        self.result_text.insert(tk.END, f"総移動距離：約 {total_distance:.2f} km\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = KyotoSightseeingApp(root)
    root.mainloop()
