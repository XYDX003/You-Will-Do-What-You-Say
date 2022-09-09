# 夏云风雪 制作 代码
# 2022.8.31

import pygame
import random


pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
pink = (255,192,203)
silvery = (192,192,192,10)
cyan = (0,128,128) # 青色
# 快捷颜色

window = pygame.display.set_mode((800,494),pygame.RESIZABLE)
pygame.display.set_caption('言出必行')
window.fill(black)
# 设置窗口、标题和背景颜色

f = pygame.font.Font('字体/翩翩体.ttf', 20)
# 加载命令字体为f

det_image = pygame.transform.rotozoom(pygame.image.load('图片/-_-.jpeg'),0,0.1)
# 载入'-_-.jpeg'图片成为主角

class Action:
    # 定义类Action来实现命令输入功能

    def __init__(self):
        self.start = False
        self.commod = ''
        # 初始化命令字符串

    def input(self,keys):
        # 输入文本函数

        global window_h,window_w

        window_w,window_h = window.get_size()

        if self.start:

            if keys == pygame.K_RETURN:

                window.fill(black)
                self.start = False
                action.run(self.commod)
                self.commod = ''

            elif keys == pygame.K_BACKSPACE:

                self.commod = self.commod[:-1]

            else:
                self.commod += event.unicode


        if tishifu:
            # 提示符显示
            self.commod += '|'

        window.fill(black)
        # 先擦除一遍屏幕

        commod_text = f.render(self.commod,True,white)
        # 制作字体图片

        window.blit(commod_text,(0,window_h-25))
        # 绘制字体

        if tishifu:
            self.commod = self.commod[:-1]

    def run(self,commod):
        # 执行命令函数

        words = commod.split(' ')
        # 分割字符串commod入列表words中

        if '/I' in words[0]:
            # 识别主语为“我”
            pass



action = Action()

TISHIFU_O = pygame.USEREVENT + 1
tishifu_O = pygame.event.Event(TISHIFU_O)
pygame.time.set_timer(TISHIFU_O,1500)
# 发送提示符显示事件
pygame.time.wait(1500)
TISHIFU_F = pygame.USEREVENT + 1
tishifu_F = pygame.event.Event(TISHIFU_F)
pygame.time.set_timer(TISHIFU_F,1500)
# 发送提示符隐藏事件

pygame.display.flip()

while True:
    # main loop

    for event in pygame.event.get():
        # 遍历事件列表

        if event.type == pygame.QUIT:
            #退出游戏的方法
            exit()
        
        if event.type == TISHIFU_O:
            tishifu = True

        if event.type == TISHIFU_F:
            tishifu = False

        # -----------------------------------------1.命令台模块
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SLASH:
                # 判断是否启动命令台(按下“/(K_SLASH)”键)
                action.start = True
                # 启动命令台开关打开
        
            action.input(event.key)
        # -----------------------------------------1.end
    


    pygame.display.update()
    # 刷新屏幕