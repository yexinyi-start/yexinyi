print("hello,world!")
#【dateime的实验】
from datetime import  datetime
#前面为要从中导入的可重复使用的代码的标准库模块的名字，后面是子模块的名字
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]
for i in range(5):
    #增加for循环行
    right_this_minute = datetime.today().minute
#这里创建了另一个变量并对它赋值；后面是调用生成一个值，这个值将赋给一个变量
    if right_this_minute in odds:
     print("this minute seems a little odd.")
    else:
     print("not an odd minute.")
    import  time
    import  random
    wait_time = random.randint(1, 6)
    time.sleep(wait_time)

#ps:冒号引入了缩进的代码组，是代码不能缺少的一部分，否则可能会引起错误
#注意：1，为了使if和else对齐，取消了else的缩进
# 2.代码组可以包含嵌套的代码组
#循环行的加入，使得9-14行相应的缩进


#指定延缓练习
import  time
#告诉shell导入“time”模块
time.sleep(5)
#调用sleep时，shell会暂停5s


#循环联系练习
for i in [1,2,3]:
    print(i)
    #i是一个循环的迭代变量，不过完全可以用任何的名字。实际上，在这种情况下，我们常用i/j/k的字母表示

for ch in "hi!":
    print(ch)
    #ch是循环变量名，hi的字符串要迭代处理，一次处理一个字符

for num in range(5):
    print('head first rocks!')
    #我们请求一个包含5个数的范围，所以迭代5次，这会得到5个消息，要记住，按两次回车键才会运行包含一个代码族的代码！

#随机数生成练习
import  random
random.randint(1,60)
random.randint(1,60)
random.randint(1,60)

#【啤酒童谣的实验】
print("Distinguished guest! Welcome to my beer house")
#尊贵的客人，欢迎来到我的啤酒屋！
word = "bottles"
#将bottles赋给word的新变量
for beer_num in range(99, 0, -1):
    print(beer_num, word, "of beer on the wall.")
    print(beer_num,word,"of beer.")
    print("Take one down.")
    print("Pass it around.")
#现在你将从99个beer中拿走啤酒，每次墙上的啤酒数上都会减一
    if beer_num == 1:
        print("No more bottles of beer on the wall.")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = "bottle"
        print(new_num,word, "of beer on the wall.")
    print()
#当你拿到啤酒总数只剩下1个时，我们会告诉你没有再多的啤酒啦。



#课堂笔记：
#1.学习了循环函数，随机函数，datime的简单运用，感觉自己仍然有很多不足的地方可以加以改进。
#2.代码的注释可以有效的帮助我们理解代码的含义
#3.每一个字母都有含义，凭空出生的词汇会报错
#4.报错时请即使更改和检查，看自己的拼写和语法是否有缺漏的地方。例如“：”
#5，老师的课要认真听......如果缺少了一些小的步骤也没关系，课后要及时的补充上去。ps，老师课堂上的讲课速度也可以慢一点，跟不上的感觉真的太难受了。













