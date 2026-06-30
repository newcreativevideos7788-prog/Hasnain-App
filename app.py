from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class DragonBotApp(App):

    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text="DragonBot APK Ready")
        self.layout.add_widget(self.label)

        btn1 = Button(text="Add D")
        btn1.bind(on_press=self.add_d)
        self.layout.add_widget(btn1)

        btn2 = Button(text="Add T")
        btn2.bind(on_press=self.add_t)
        self.layout.add_widget(btn2)

        btn3 = Button(text="Analyze")
        btn3.bind(on_press=self.analyze)
        self.layout.add_widget(btn3)

        return self.layout

    def add_d(self, instance):
        self.label.text = "D Added"

    def add_t(self, instance):
        self.label.text = "T Added"

    def analyze(self, instance):
        self.label.text = "Analyzing Data..."

DragonBotApp().run()
