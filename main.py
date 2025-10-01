from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from plyer import filechooser
import os

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        self.btn = Button(
            text='📁 انتخاب عکس',
            size_hint=(1, 0.3),
            background_color=(0.2, 0.6, 1, 1),
            font_size='20sp'
        )
        self.btn.bind(on_press=self.pick_image)
        
        self.image = Image(size_hint=(1, 0.6))
        self.label = Label(text='عکسی انتخاب نشده', size_hint=(1, 0.1))
        
        layout.add_widget(self.btn)
        layout.add_widget(self.image)
        layout.add_widget(self.label)
        return layout
    
    def pick_image(self, instance):
        self.label.text = 'در حال باز کردن گالری...'
        filechooser.open_file(
            title="عکس انتخاب کنید",
            filters=[["Images", "*.jpg", "*.png", "*.jpeg"]],
            on_selection=self.got_image
        )
    
    def got_image(self, selection):
        if selection:
            self.image.source = selection[0]
            self.label.text = f'عکس انتخاب شد!'
        else:
            self.label.text = 'عکسی انتخاب نشد'

if __name__ == '__main__':
    MyApp().run()
