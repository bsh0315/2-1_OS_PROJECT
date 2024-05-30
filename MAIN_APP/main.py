# main.py
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.label import Label
import sys # 경로 추가를 위해
import time

sys.path.append("./../yolo/yolov5/yolov5") # yolo 모델 사용을 위한 경로 추가

import detect # yolo의 detect 모듈 추가

class MainScreen(Screen):
    def capture_image(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("photos/IMG.png".format(timestr))

        # yolo v5 사용부분
        opt = detect.parse_opt() 
        result = detect.main(opt)
        print(result) # 디버깅
        result = sorted(result,reverse=True,key=lambda x: x[1]) #확률을 기준으로 내림차순으로 정렬
        print(result) # 디버깅 
        product = result[0][0] # 가장 확률이 높은 아이템을 갖고오기
        print(product)
        
        
        print("Captured")

class SecondScreen(Screen):
    def toggle_microphone(self):
        # Add logic for enabling/disabling the microphone here
        pass

class SettingScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(SettingScreen(name='setting'))
        return sm


if __name__ == '__main__':
    MyApp().run()