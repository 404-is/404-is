from turtle import Screen
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<Screenone>:
    GridLayout:
        rows: 2
        cols:1
        #image
        Image:
            source: 'logo.png.jpg'
            allow_stretch: False
            keep_ratio: True
        #button
        Button:
            text:"Click to Proceed"
            bold: True
            size_hint: (.05, .05)
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 0
                root.manager.current = "screen_two"

<ScreenTwo>:
    GridLayout:
        rows: 
        cols: 1
        #image
        Image:
            source: 'logo.png.jpg'
        #label
        Label:
            text: "Kindly select a module"
    BoxLayout:
        #button1
        Button:
            text: "Reconnaissance"
            size_hint: (.05, .05)
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 0
                root.manager.current = "screen_three"
        #button2
        Button:
            text: "Scanning"
            size_hint: (.05, .05)
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 0
                root.manager.current = "screen_four"
        #button3 
        Button:    
            text: "Gaining Access"
            size_hint: (.05, .05)
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 0
                root.manager.current = "screen_five" 
        #button4
        Button:
            text: "Maintaining access"
            size_hint: (.05, .05)
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 0
                root.manager.current = "screen_six"  
        #button 5
        Button:
            text: "Covering Tracks"
            size_hint: (.05, .05)
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 0
                root.manager.current = "screen_seven"

<ScreenThree>:
    GridLayout:
        rows: 
        cols: 1
        #image
        Image: 
            source: 'logo.png.jpg'
        #label
        Label:
            text: "Reaconnaisse"
    BoxLayout:
        #button
        Button:
            text: "Network Scanner"
            size_hint: (.05, .05)
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 0
                root.manager.current = "screen_two"
            on_release:
                import subprocess
                from subprocess import Popen
                subprocess.Popen(['gnome-terminal -x python3 /home/_404/Desktop/404Framework/networkscan/main.py '], shell=True)
              
        Button:
            text: "MacAddress Changer"
            size_hint: (.05, .05)
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 0
                root.manager.current = "screen_one"
            on_release:
                import subprocess
                from subprocess import Popen
                subprocess.Popen(['gnome-terminal -x sudo python3 /home/_404/Desktop/404Framework/macchanger/macaddchanger.py '], shell=True)


<ScreenFour>:
    GridLayout:
        rows: 
        cols: 1
        #image
        Image:
            source: 'logo.png.jpg'
        #label
        Label:
            text: "Scanning"
    BoxLayout:
        #button
        Button:
            text: "Website Crawler"
            size_hint: (.05, .05)
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 0
                root.manager.current = "screen_two"
            on_release:
                import subprocess
                from subprocess import Popen
                subprocess.Popen(['gnome-terminal -x sudo python3 /home/_404/Desktop/404Framework/fuzzer/fuzz.py '], shell=True)
        Button:
            text: "Cross-Site Scripting Scanner"
            size_hint: (.05, .05)
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 0
                root.manager.current = "screen_two"
            on_release:
                import subprocess
                from subprocess import Popen
                subprocess.Popen(['gnome-terminal -x sudo python3 /home/_404/Desktop/404Framework/xssscaner/xxs.py '], shell=True)
        Button:
            text: "SQLI Scanner"
            size_hint: (.05, .05)
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 0
                root.manager.current = "screen_two"
            on_release:
                import subprocess
                from subprocess import Popen
                subprocess.Popen(['gnome-terminal -x sudo python3 /home/_404/Desktop/404Framework/sqlscanner/sqlscan.py '], shell=True)
        Button:
            text: "Subdomain Scanner"
            size_hint: (.05, .05)
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 0
                root.manager.current = "screen_two"
            on_release:
                import subprocess
                from subprocess import Popen
                subprocess.Popen(['gnome-terminal -x sudo python3 /home/_404/Desktop/404Framework/subdomain/subdomainscan.py '], shell=True)

<ScreenFive>:
    GridLayout:
        rows: 
        cols: 1
        #image
        Image:
            source: 'logo.png.jpg'
        #label
        Label:
            text: "Gaining Access"
    BoxLayout:
        #button
        Button:
            text: "ARP Spoofer"
            size_hint: (.05, .05)
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 0
                root.manager.current = "screen_two"
        Button:
            text: "Packet Sniffer"
            size_hint: (.05, .05)
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 0
                root.manager.current = "screen_two"
        Button:
            text: "DNS Spoofer"
            size_hint: (.05, .05)
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 0
                root.manager.current = "screen_two"
        Button:
            text: "File Interceptor"
            size_hint: (.05, .05)
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 0
                root.manager.current = "screen_two"
        Button:
            text: "Bruteforcer"
            size_hint: (.05, .05)
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 0
                root.manager.current = "screen_two"
        Button:
            text: "Code Injector"
            size_hint: (.05, .05)
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 0
                root.manager.current = "screen_two"

<ScreenSix>:
    GridLayout:
        rows: 
        cols: 1
        #image
        Image:
            source: 'logo.png.jpg'
        #label
        Label:
            text: "Maintaining Access"
    BoxLayout:
        #button
        Button:
            text: "Keylogger"
            size_hint: (.05, .05)
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 0
                root.manager.current = "screen_two"
        Button:
            text: "Backdoor Creator"
            size_hint: (.05, .05)
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 0
                root.manager.current = "screen_two"
        Button:
            text: "Malware Manager"
            size_hint: (.05, .05)
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 0
                root.manager.current = "screen_two"

<ScreenSeven>:
    GridLayout:
        rows: 
        cols: 1
        #image
        Image:
            source: 'logo.png.jpg'
        #label
        Label:
            text: "Covering Tracks"
    BoxLayout:
        #button
        Button:
            text: "Read Note"
            size_hint: (.05, .05)
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = 0
                root.manager.current = "screen_two"

""")

class Screenone(Screen):
    pass


class ScreenTwo(Screen):
    pass

class ScreenThree(Screen):
    pass

class ScreenFour(Screen):
    pass

class ScreenFive(Screen):
    pass

class ScreenSix(Screen):
    pass

class ScreenSeven(Screen):
    pass

screen_manager = ScreenManager()


screen_manager.add_widget(Screenone(name="screen_one"))
screen_manager.add_widget(ScreenTwo(name="screen_two"))
screen_manager.add_widget(ScreenThree(name="screen_three"))
screen_manager.add_widget(ScreenFour(name="screen_four"))
screen_manager.add_widget(ScreenFive(name="screen_five"))
screen_manager.add_widget(ScreenSix(name="screen_six"))
screen_manager.add_widget(ScreenSeven(name="screen_seven"))


class framework(App):

    def build(self):
        return screen_manager

sample_app = framework()
sample_app.run()