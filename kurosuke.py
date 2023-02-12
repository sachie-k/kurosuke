# https://kitao.github.io/pyxel/wasm/launcher/?play=sachie-k.kurosuke.kurosuke

import random
import pyxel

SCENE_TITLE = 0
SCENE_PLAY = 1

endroll_x = 160

class Cat:
    def __init__(self, x, y, d, status):
        self.x = x
        self.y = y
        self.d = d
        self.status = status

class Cha:
    def __init__(self, x, y, d, status):
        self.x = x
        self.y = y
        self.d = d
        self.status = status

class Mike:
    def __init__(self, x, y, d, status):
        self.x = x
        self.y = y
        self.d = d
        self.status = status

class Shiro:
    def __init__(self, x, y, d, status):
        self.x = x
        self.y = y
        self.d = d
        self.status = status

class Dog:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d

class Mouse:
    def __init__(self, x, y, count):
        self.x = x
        self.y = y
        self.count = count
        
class Churu:
    def __init__(self, x, y, flg):
        self.x = x
        self.y = y
        self.flg = flg

class App:
    def __init__(self):
        pyxel.init(160, 208, title="KUROSUKE", fps = 20)
        pyxel.load("kurosuke_ast.pyxres")
        
        self.scene = SCENE_TITLE
        
        self.cat = Cat(72, 16, 3, 1)
        self.cha = Cha(-72, 16, 3, 0)
        self.mike = Mike(-72, 16, 3, 0)
        self.shiro = Shiro(-72, 16, 3, 0)
        self.dog = Dog(80, 64, 1)
        self.mouse = Mouse(80, 48, 0)
        self.churu = Churu(-32, 16, 0)
        self.churu_flame = 0
        self.music_flg = False
        
        pyxel.playm(3, loop=True)
        
        pyxel.run(self.update, self.draw)

    def update_cat_move(self):

        if self.cat.status == 1:
            if abs(self.cha.x - self.cat.x) < 8 and abs(self.cha.y - self.cat.y) < 8:
                self.cat.status = 0
            if abs(self.mike.x - self.cat.x) < 8 and abs(self.mike.y - self.cat.y) < 8:
                self.cat.status = 0
            if abs(self.shiro.x - self.cat.x) < 8 and abs(self.shiro.y - self.cat.y) < 8:
                self.cat.status = 0
            if abs(self.dog.x - self.cat.x) < 8 and abs(self.dog.y - self.cat.y) < 8:
                self.cat.status = 0
            
            if self.cat.x < 35 or self.cat.x >= 114 or (self.cat.x >= 50 and self.cat.x < 98):  # 川に落ちる判定
                if self.cat.y >= 75 and self.cat.y <= 88:
                    self.cat.status = 0
            if (pyxel.btnp(pyxel.KEY_LEFT, 1, 1) or \
                    ((56 <= pyxel.mouse_x <= 72) and (144 <= pyxel.mouse_y <= 192) and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT)))\
                        and self.cat.x > 3:  # 左移動
                self.cat.x -= 2
                self.cat.d = 1
            elif (pyxel.btnp(pyxel.KEY_RIGHT, 1, 1) or \
                    ((88 <= pyxel.mouse_x <= 104) and (144 <= pyxel.mouse_y <= 192) and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT)))\
                        and self.cat.x < 141:  # 右移動
                self.cat.x += 2
                self.cat.d = 0
            if (pyxel.btnp(pyxel.KEY_UP, 1, 1) or \
                    ((56 <= pyxel.mouse_x <= 104) and (144 <= pyxel.mouse_y <= 160) and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT)))\
                        and self.cat.y > 20:  # 上移動
                self.cat.y -= 2
                self.cat.d = 2
            elif (pyxel.btnp(pyxel.KEY_DOWN, 1, 1) or \
                    ((56 <= pyxel.mouse_x <= 104) and (176 <= pyxel.mouse_y <= 192) and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT)))\
                        and self.cat.y < 113:  # 下移動
                self.cat.y += 2
                self.cat.d = 3
                
            if (pyxel.btnp(pyxel.KEY_C, 1, 1) or \
                    ((104 <= pyxel.mouse_x <= 120) and (176 <= pyxel.mouse_y <= 192) and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT))): # チュール
                self.churu.flg = 1
                
                pyxel.playm(0, loop=False)

                
                self.churu_flame = pyxel.frame_count

    def update_cha_move(self):

        if self.churu.flg != 0:
            if self.cha.x > self.churu.x + 5:  # 左移動
                self.cha.x -= 0.6
                self.cha.d = 1
            elif self.cha.x < self.churu.x - 5:  # 右移動
                self.cha.x += 0.6
                self.cha.d = 0
            elif self.cha.y > self.churu.y + 5:  # 上移動
                self.cha.y -= 0.6
                self.cha.d = 2
            if (self.cha.x > self.churu.x + 5) and (self.cha.y > self.churu.y + 5):  # 左上移動
                self.cha.x -= 0.4
                self.cha.y -= 0.4
                self.cha.d = 1
            if (self.cha.x < self.churu.x - 5) and (self.cha.y > self.churu.y + 5):  # 右上移動
                self.cha.x += 0.4
                self.cha.y -= 0.4
                self.cha.d = 0
        else:
            if (self.cha.x > self.mouse.x) and (self.cha.y == self.mouse.y):  # 左移動
                self.cha.x -= 0.6
                self.cha.d = 1
            elif (self.cha.x < self.mouse.x) and (self.cha.y == self.mouse.y):  # 右移動
                self.cha.x += 0.6
                self.cha.d = 0
            if (self.cha.y > self.mouse.y) and (self.cha.x == self.mouse.x):  # 下移動
                self.cha.y -= 0.6
                self.cha.d = 3
            elif (self.cha.y < self.mouse.y) and (self.cha.x == self.mouse.x):  # 上移動
                self.cha.y += 0.6
                self.cha.d = 2
            if (self.cha.x > self.mouse.x) and (self.cha.y > self.mouse.y):  # 左上移動
                self.cha.x -= 0.4
                self.cha.y -= 0.418
                self.cha.d = 1
            elif (self.cha.x < self.mouse.x) and (self.cha.y < self.mouse.y):  # 右下移動
                self.cha.x += 0.4
                self.cha.y += 0.4
                self.cha.d = 0
            if (self.cha.x < self.mouse.x) and (self.cha.y > self.mouse.y):  # 右上移動
                self.cha.x += 0.4
                self.cha.y -= 0.4
                self.cha.d = 0
            elif (self.cha.x > self.mouse.x) and (self.cha.y < self.mouse.y):  # 左下移動
                self.cha.x -= 0.4
                self.cha.y += 0.4
                self.cha.d = 1
        

    def update_mike_move(self):
        
        if self.churu.flg != 0:
            if self.mike.x > self.churu.x + 5:  # 左移動
                self.mike.x -= 0.6
                self.mike.d = 1
            elif self.mike.x < self.churu.x - 5:  # 右移動
                self.mike.x += 0.6
                self.mike.d = 0
            elif self.mike.y > self.churu.y + 5:  # 上移動
                self.mike.y -= 0.6
                self.mike.d = 2
            if (self.mike.x > self.churu.x + 5) and (self.mike.y > self.churu.y + 5):  # 左上移動
                self.mike.x -= 0.4
                self.mike.y -= 0.4
                self.mike.d = 1
            if (self.mike.x < self.churu.x - 5) and (self.mike.y > self.churu.y + 5):  # 右上移動
                self.mike.x += 0.4
                self.mike.y -= 0.4
                self.mike.d = 0
        else:
            if (self.mike.x > self.mouse.x) and (self.mike.y == self.mouse.y):  # 左移動
                self.mike.x -= 0.6
                self.mike.d = 1
            elif (self.mike.x < self.mouse.x) and (self.mike.y == self.mouse.y):  # 右移動
                self.mike.x += 0.6
                self.mike.d = 0
            if (self.mike.y > self.mouse.y) and (self.mike.x == self.mouse.x):  # 下移動
                self.mike.y -= 0.6
                self.mike.d = 3
            elif (self.mike.y < self.mouse.y) and (self.mike.x == self.mouse.x):  # 上移動
                self.mike.y += 0.6
                self.mike.d = 2
            if (self.mike.x > self.mouse.x) and (self.mike.y > self.mouse.y):  # 左上移動
                self.mike.x -= 0.8
                self.mike.y -= 0.3
                self.mike.d = 1
            elif (self.mike.x < self.mouse.x) and (self.mike.y < self.mouse.y):  # 右下移動
                self.mike.x += 0.8
                self.mike.y += 0.3
                self.mike.d = 0
            if (self.mike.x < self.mouse.x) and (self.mike.y > self.mouse.y):  # 右上移動
                self.mike.x += 0.8
                self.mike.y -= 0.3
                self.mike.d = 0
            elif (self.mike.x > self.mouse.x) and (self.mike.y < self.mouse.y):  # 左下移動
                self.mike.x -= 0.8
                self.mike.y += 0.3
                self.mike.d = 1

    def update_shiro_move(self):
        
        if self.churu.flg != 0:
            if self.shiro.x > self.churu.x + 5:  # 左移動
                self.shiro.x -= 0.6
                self.shiro.d = 1
            elif self.shiro.x < self.churu.x - 5:  # 右移動
                self.shiro.x += 0.6
                self.shiro.d = 0
            elif self.shiro.y > self.churu.y + 5:  # 上移動
                self.shiro.y -= 0.6
                self.shiro.d = 2
            if (self.shiro.x > self.churu.x + 5) and (self.shiro.y > self.churu.y + 5):  # 左上移動
                self.shiro.x -= 0.4
                self.shiro.y -= 0.4
                self.shiro.d = 1
            if (self.shiro.x < self.churu.x - 5) and (self.shiro.y > self.churu.y + 5):  # 右上移動
                self.shiro.x += 0.4
                self.shiro.y -= 0.4
                self.shiro.d = 0
        else:
            if (self.shiro.x > self.cat.x) and (self.shiro.y == self.cat.y):  # 左移動
                self.shiro.x -= 0.6
                self.shiro.d = 1
            elif (self.shiro.x < self.cat.x) and (self.shiro.y == self.cat.y):  # 右移動
                self.shiro.x += 0.6
                self.shiro.d = 0
            if (self.shiro.y > self.cat.y) and (self.shiro.x == self.cat.x):  # 下移動
                self.shiro.y -= 0.6
                self.shiro.d = 3
            elif (self.shiro.y < self.cat.y) and (self.shiro.x == self.cat.x):  # 上移動
                self.shiro.y += 0.7
                self.shiro.d = 2
            if (self.shiro.x > self.cat.x) and (self.shiro.y > self.cat.y):  # 左上移動
                self.shiro.x -= 0.7
                self.shiro.y -= 0.3
                self.shiro.d = 1
            elif (self.shiro.x < self.cat.x) and (self.shiro.y < self.cat.y):  # 右下移動
                self.shiro.x += 0.7
                self.shiro.y += 0.3
                self.shiro.d = 0
            if (self.shiro.x < self.cat.x) and (self.shiro.y > self.cat.y):  # 右上移動
                self.shiro.x += 0.7
                self.shiro.y -= 0.3
                self.shiro.d = 0
            elif (self.shiro.x > self.cat.x) and (self.shiro.y < self.cat.y):  # 左下移動
                self.shiro.x -= 0.7
                self.shiro.y += 0.3
                self.shiro.d = 1
    
    def update_dog_move(self):

        if self.dog.x > self.cat.x:  # 左向き
            self.dog.d = 1
        elif self.dog.x < self.cat.x:  # 右向き
            self.dog.d = 0


    def update_mouse_status(self):
        
        if (abs(self.mouse.x - self.cat.x) < 8 and abs(self.mouse.y - self.cat.y) < 8) or \
            (abs(self.mouse.x - self.cha.x) < 8 and abs(self.mouse.y - self.cha.y) < 8) or \
            (abs(self.mouse.x - self.mike.x) < 8 and abs(self.mouse.y - self.mike.y) < 8) or \
            (abs(self.mouse.x - self.shiro.x) < 8 and abs(self.mouse.y - self.shiro.y) < 8):
            
            if (abs(self.mouse.x - self.cat.x) < 8 and abs(self.mouse.y - self.cat.y) < 8):
                self.mouse.count += 1
                pyxel.playm(2, loop=False)

                if self.mouse.count >= 10:
                    self.cat.status = 2
            
            pos_f = 1
            while pos_f == 1:
                self.mouse.x = random.randint(8, 136)
                self.mouse.y = random.randint(16, 96)
                if self.mouse.y < 60 or self.mouse.y > 91: # 川以外
                    pos_f = 0
                    break
                elif (self.mouse.x >= 35 and self.mouse.x <= 45) or (self.mouse.x >= 99 and self.mouse.x <= 109):
                    pos_f = 0
                    
                if (self.mouse.x >= 75 and self.mouse.x <= 91) and self.mouse.y <= 52: # 犬
                    pos_f = 1

        
    def update(self):

        self.update_cat_move()
        self.update_dog_move()

        if (self.mouse.count >= 3):
            if self.cha.status == 0:
                self.cha = Cha(72, 16, 3, 1)
            self.update_cha_move()
        if (self.mouse.count >= 5):
            if self.mike.status == 0:
                self.mike = Mike(72, 16, 3, 1)
            self.update_mike_move()
        if (self.mouse.count >= 8):
            if self.shiro.status == 0:
                self.shiro = Shiro(72, 16, 3, 1)
            self.update_shiro_move()
        
        if self.churu.flg != 0:
            self.churu = Churu(8, 16, 1)
            if pyxel.frame_count - self.churu_flame > 80:
                self.churu = Churu(-32, 16, 0)
                self.churu_flame = 0

        self.update_mouse_status()
        
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
    

    def draw_title_scene(self):
        pyxel.bltm(0, 0, 1, 0, 0, 160, 96, 4) # タイルマップ
        pyxel.blt(72, 144, 1, 16, 208, 16, 16, 0) #up
        pyxel.blt(72, 160, 1, 16, 224, 16, 16, 0) #mid
        pyxel.blt(72, 176, 1, 16, 240, 16, 16, 0) #down

        pyxel.blt(56, 144, 1, 0, 208, 16, 16, 0) #left_up
        pyxel.blt(88, 144, 1, 32, 208, 16, 16, 0) #right_up

        pyxel.blt(56, 160, 1, 0, 224, 16, 16, 0) #left
        pyxel.blt(88, 160, 1, 32, 224, 16, 16, 0) #right

        pyxel.blt(56, 176, 1, 0, 240, 16, 16, 0) #left_down
        pyxel.blt(88, 176, 1, 32, 240, 16, 16, 0) #right_down

        pyxel.blt((pyxel.frame_count)*0.1 % (pyxel.width), 10, 1, 0, 48, 32, 16, 6)
        pyxel.blt((pyxel.frame_count) % (pyxel.width + 100), 72 + pyxel.frame_count % 5, 1, 16, 80, 16, 16, 6)
        pyxel.blt((pyxel.frame_count - 48) % (pyxel.width + 100), 76, 1, 0, 64, 16, 16, 6)
        pyxel.blt((pyxel.frame_count - 80) % (pyxel.width + 100), 76, 1, 16, 64, 16, 16, 6)
        pyxel.blt((pyxel.frame_count - 95) % (pyxel.width + 100), 76, 1, 32, 64, 16, 16, 6)
        pyxel.blt((pyxel.frame_count - 110) % (pyxel.width + 100), 76, 1, 48, 64, 16, 16, 6)
        
        pyxel.text(67, 98, "> PLAY", 0)
        
        # mouse icon
        pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 2, 64, 0, 16, 16, 0)
        
        #ENTERでゲーム画面に遷移
        if pyxel.btnp(pyxel.KEY_RETURN) or \
            (pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and (67 <= pyxel.mouse_x <= 99) and (90 <= pyxel.mouse_y <= 106)):
            self.scene = SCENE_PLAY
            pyxel.stop()

    def draw_play_scene(self):
        global endroll_x
        
        pyxel.cls(11)
        pyxel.bltm(0, 16, 0, 0, 0, 160, 96, 0)
        pyxel.blt(72, 144, 1, 16, 208, 16, 16, 0) #up
        pyxel.blt(72, 160, 1, 16, 224, 16, 16, 0) #mid
        pyxel.blt(72, 176, 1, 16, 240, 16, 16, 0) #down

        pyxel.blt(56, 144, 1, 0, 208, 16, 16, 0) #left_up
        pyxel.blt(88, 144, 1, 32, 208, 16, 16, 0) #right_up

        pyxel.blt(56, 160, 1, 0, 224, 16, 16, 0) #left
        pyxel.blt(88, 160, 1, 32, 224, 16, 16, 0) #right

        pyxel.blt(56, 176, 1, 0, 240, 16, 16, 0) #left_down
        pyxel.blt(88, 176, 1, 32, 240, 16, 16, 0) #right_down

        pyxel.blt(104, 176, 1, 48, 240, 16, 16, 0) #チュールボタン
        
        if self.cat.status == 2 : # クリア
            
            if self.music_flg == False:
                pyxel.playm(4, loop=False)
                self.music_flg = True
            
            endroll_x += -1
            if endroll_x > 18:
                pyxel.bltm(endroll_x, 32, 1, 0, 98, 128, 76, 14)
            else:
                self.scene = SCENE_TITLE
                endroll_x = 160
                self.cat = Cat(72, 16, 3, 1)
                self.cha = Cha(-72, 16, 3, 0)
                self.mike = Mike(-72, 16, 3, 0)
                self.shiro = Shiro(-72, 16, 3, 0)
                self.dog = Dog(80, 64, 1)
                self.mouse = Mouse(80, 48, 0)
                self.churu = Churu(-32, 16, 0)
                pyxel.playm(3, loop=True)
                self.music_flg = False


        if self.cat.status == 0: # 死んだ時
        
            if self.music_flg == False:
                pyxel.playm(1, loop=False)
                self.music_flg = True
                    
            endroll_x += -1
            if endroll_x > 18:
                pyxel.bltm(endroll_x, 32, 1, 0, 178, 128, 80, 3)

            # retry button
            pyxel.text(67, 98, "> RETRY", 0)
                
            if pyxel.btnp(pyxel.KEY_RETURN) or \
                    (pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and (67 <= pyxel.mouse_x <= 99) and (90 <= pyxel.mouse_y <= 106)):
                    self.scene = SCENE_TITLE
                    endroll_x = 160
                    self.cat = Cat(72, 16, 3, 1)
                    self.cha = Cha(-72, 16, 3, 0)
                    self.mike = Mike(-72, 16, 3, 0)
                    self.shiro = Shiro(-72, 16, 3, 0)
                    self.dog = Dog(80, 64, 1)
                    self.mouse = Mouse(80, 48, 0)
                    self.churu = Churu(-32, 16, 0)
                    pyxel.playm(3, loop=True)
                    self.music_flg = False

        text_mouse = "SCORE:{}".format(self.mouse.count)
        pyxel.text(5, 6, text_mouse, 8)

        if self.cat.status == 1:
            pyxel.blt(self.mouse.x, self.mouse.y, 0, 16 * (self.mouse.count % 4), 80, 16, 16, 6)
            pyxel.blt(self.cat.x, self.cat.y, 0, 16 * self.cat.d, 16 + 16 * (pyxel.frame_count % 4), 16, 16, 6)
            pyxel.blt(self.cha.x, self.cha.y, 0, 16 * self.cha.d, 96 + 16 * (pyxel.frame_count % 2), 16, 16, 6)
            pyxel.blt(self.mike.x, self.mike.y, 0, 16 * self.mike.d, 128 + 16 * (pyxel.frame_count % 2), 16, 16, 6)
            pyxel.blt(self.shiro.x, self.shiro.y, 0, 16 * self.shiro.d, 160 + 16 * (pyxel.frame_count % 2), 16, 16, 6)
            pyxel.blt(self.dog.x, self.dog.y, 0, 32 * self.dog.d + 16 * (pyxel.frame_count % 2) , 0, 16, 16, 6)
            pyxel.blt(self.churu.x, self.churu.y, 0, 0,192, 16, 16, 6)
                
        
        pyxel.bltm(0, 112, 0, 0, 96, 160, 16, 11)
        
        # mouse icon
        pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 2, 64, 0, 16, 16, 0)
        
        

    def draw(self):
        # 画面クリア
        pyxel.cls(11)

        #描画の画面分岐
        if self.scene == SCENE_TITLE:
            self.draw_title_scene()
        elif self.scene == SCENE_PLAY:
            self.draw_play_scene()

App()
