class Student(object):
    # __init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def print_score(self):
        print('%s : %s' % (self.name, self.score))

# 实例
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
bart.score = 60
bart.print_score()
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：
class Student1(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s : %s' %(self.__name, self.__score))
    # 如果外部代码要获取name和score
    def get_mame(self):
        return self.__name
    def get_score(self):
        return self.__score
    # 允许外部代码修改score怎么办
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

# 继承 
# 父类
class Animal(object):
    def run(self):
        print('Animal is runing ...')

# 子类
class Dog(Animal):
    def run(self):
        print('Dog is runing...')

dog = Dog()

dog.run()
# 判断一个变量是否是某个类型
print(isinstance(dog, Dog))
print(isinstance(dog, Animal)) # True