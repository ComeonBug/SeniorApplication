# 若想兼容python2，需要在类后继承object
class MyClass(object):
    pass


def t1():
    a = MyClass()
    b = MyClass()
    print('a type:')
    print(type(a))
    print('a id:')
    print(id(a))
    print('b id:')
    print(id(b))
    print('a class name:')
    print(a.__class__)
    print('b class name:')
    print(b.__class__)
    c = MyClass
    d = c()
    print('d id:')
    print(id(d))
    print('d class name:')
    print(d.__class__)


class Human(object):
    live = True

    def __init__(self, name):
        # self:放在首位，约定俗成的，代表【对象自身】
        self.name = name

    # 获取属性的4个方法的用法和区别
    # __getattr__、__getattribute__、__get__、 @property
    # def __getattr__(self, item):
    #     # [对象.属性]要获取的属性不存在时，会调用这个__getattr__方法
    #     print('Human2:__getattr')
    #     return '0'

    def __getattribute__(self, item):
        # 拦截存在的属性：
        print('Human2:__getattribute__')
        return '0'

def t4():
    man = Human('Adn')
    # print(man.__dict__)
    # name属性存在，会正常显示name属性值
    print('name属性存在')
    print(man.name)

    # age属性不存在，【man.age】这句会调用Human类的__getattr__方法，【man.age】的结果就 == __getattr__方法的返回值
    print('age属性不存在')
    print(man.age)


def t2():
    man = Human('Adn')
    woman = Human('Eva')

    print('Human类的属性：')
    print(Human.__dict__)
    print('man的属性:')
    print(man.__dict__)
    man.live = False
    print('man的修改了属性:')
    print(man.__dict__)
    print('woman的属性:')
    print(woman.__dict__)
    # setattr：只能对于自己写的类添加属性，内置类型不能增加属性和方法
    setattr(Human, 'age', 10)
    print('setattr之后Human类的属性：')
    print(Human.__dict__)
    print('setattr之后man的属性:')
    print(man.__dict__)


class Human2(object):
    # 单下划线：人为约定不可修改
    _age = 10

    # 私有属性
    # 自动改名的机制来做到属性的隐藏
    # 将【__fly】改为【_Human2__fly】
    # 注意：两边都加了__之后，就不是属性了，变成了魔术方法，模式方法不会自动改名
    __fly = False

    # 如果属性名和python的保留子一样的话，可以在属性后加一个下划线：
    object_ = 'man'


def t3():
    snake = Human2()
    print('snake 属性')
    print(snake.__dict__)
    print('Human2 属性')
    print(Human2.__dict__)


if __name__ == '__main__':
    t4()