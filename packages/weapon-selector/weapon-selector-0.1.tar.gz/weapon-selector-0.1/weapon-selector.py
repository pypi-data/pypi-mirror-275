import tkinter as tk
from tkinter import messagebox

class WeaponSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("スプラトゥーン武器選びアシスタント")
        
        # 質問ラベル
        self.label1 = tk.Label(root, text="射程距離はどれがいいですか？ (長射程/中射程/短射程)")
        self.label1.pack()
        self.range_var = tk.StringVar()
        self.range_entry = tk.Entry(root, textvariable=self.range_var)
        self.range_entry.pack()

        self.label2 = tk.Label(root, text="あなたのプレイスタイルは？ (攻撃/防御/サポート)")
        self.label2.pack()
        self.playstyle_var = tk.StringVar()
        self.playstyle_entry = tk.Entry(root, textvariable=self.playstyle_var)
        self.playstyle_entry.pack()

        self.label3 = tk.Label(root, text="機動力は重要ですか？ (はい/いいえ)")
        self.label3.pack()
        self.mobility_var = tk.StringVar()
        self.mobility_entry = tk.Entry(root, textvariable=self.mobility_var)
        self.mobility_entry.pack()

        self.label4 = tk.Label(root, text="好きなスペシャルウェポンの種類は？ (攻撃系/サポート系)")
        self.label4.pack()
        self.special_var = tk.StringVar()
        self.special_entry = tk.Entry(root, textvariable=self.special_var)
        self.special_entry.pack()

        self.label5 = tk.Label(root, text="インク効率は重要ですか？ (はい/いいえ)")
        self.label5.pack()
        self.ink_var = tk.StringVar()
        self.ink_entry = tk.Entry(root, textvariable=self.ink_var)
        self.ink_entry.pack()

        self.submit_button = tk.Button(root, text="武器を選ぶ", command=self.recommend_weapon)
        self.submit_button.pack()

    def recommend_weapon(self):
        range_pref = self.range_var.get().strip()
        playstyle_pref = self.playstyle_var.get().strip()
        mobility_pref = self.mobility_var.get().strip()
        special_pref = self.special_var.get().strip()
        ink_pref = self.ink_var.get().strip()

        weapons = [
            {"name": "スプラシューター", "range": "中射程", "playstyle": "攻撃", "mobility": "中", "special": "攻撃系", "ink": "中"},
            {"name": "スプラローラー", "range": "短射程", "playstyle": "攻撃", "mobility": "低", "special": "攻撃系", "ink": "高"},
            {"name": "バレルスピナー", "range": "長射程", "playstyle": "防御", "mobility": "低", "special": "サポート系", "ink": "低"},
            {"name": "スプラスコープ", "range": "長射程", "playstyle": "攻撃", "mobility": "低", "special": "攻撃系", "ink": "低"},
            {"name": "N-ZAP85", "range": "中射程", "playstyle": "サポート", "mobility": "高", "special": "サポート系", "ink": "高"},
            {"name": "プロモデラーMG", "range": "短射程", "playstyle": "攻撃", "mobility": "高", "special": "攻撃系", "ink": "高"},
            {"name": "ジェットスイーパー", "range": "長射程", "playstyle": "防御", "mobility": "中", "special": "サポート系", "ink": "中"},
        ]

        for weapon in weapons:
            if (weapon["range"] == range_pref and
                    weapon["playstyle"] == playstyle_pref and
                    (weapon["mobility"] == "高" if mobility_pref == "はい" else True) and
                    weapon["special"] == special_pref and
                    (weapon["ink"] == "高" if ink_pref == "はい" else True)):
                messagebox.showinfo("おすすめの武器", f"あなたにおすすめの武器は: {weapon['name']} です。")
                return

        messagebox.showinfo("おすすめの武器", "適した武器が見つかりませんでした。")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeaponSelectorApp(root)
    root.mainloop()