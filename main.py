from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MasterEarn(App):
    def build(self):
        self.balance = 0.0
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.label = Label(text=f"Wallet: INR {self.balance}", font_size='25sp')
        layout.add_widget(self.label)
        btn = Button(text="Earn INR 0.50", size_hint=(1, 0.2))
        btn.bind(on_press=self.add_money)
        layout.add_widget(btn)
        return layout

    def add_money(self, instance):
        self.balance += 0.50
        self.label.text = f"Wallet: INR {self.balance}"

if __name__ == "__main__":
    MasterEarn().run()
