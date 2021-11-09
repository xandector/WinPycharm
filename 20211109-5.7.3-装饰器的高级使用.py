# 产品经理：提需求 / 改需求
# 如果超过22点不让玩游戏，不告诉时间当超22点处理

def can_play(fn):
    def inner(x, y, *args, **kwargs):
        # *args 可变参数，使用数组保存和读取
        # **kwargs 使用传入的已定义变量，即实参字典
        clock = kwargs.get('clock', 23)
        if clock <= 22:
            fn(x, y)
        else:
            print('{} is too late for {}'.format(x, y))

    return inner


@can_play
def play_game(name, game):
    print('{} is playing {}'.format(name, game))


play_game('XL', 'Dota2', clock=18)
play_game('SL', 'CSgo')
