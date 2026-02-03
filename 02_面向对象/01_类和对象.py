"""
Python 面向对象编程 - 类和对象
对移动端开发者来说，这部分概念应该很熟悉
"""

# ==================== 基本类定义 ====================
print("=== 基本类 ===")

# 使用 class 关键字定义类
class Dog:
    """一个简单的狗类"""
    
    # 类变量（所有实例共享）
    species = "犬科动物"
    
    # 构造函数（初始化方法）
    # self 类似其他语言的 this，但必须显式声明
    def __init__(self, name, age):
        """
        初始化方法
        __init__ 是特殊方法（魔术方法），会在创建对象时自动调用
        """
        # 实例变量（每个实例独有）
        self.name = name
        self.age = age
    
    # 实例方法
    def bark(self):
        """让狗叫"""
        return f"{self.name} 说: 汪汪!"
    
    def description(self):
        """描述狗"""
        return f"{self.name} 今年 {self.age} 岁"

# 创建对象（实例化）
my_dog = Dog("旺财", 3)
your_dog = Dog("小白", 2)

# 访问属性
print(f"我的狗: {my_dog.name}, {my_dog.age}岁")
print(f"你的狗: {your_dog.name}, {your_dog.age}岁")

# 调用方法
print(my_dog.bark())
print(your_dog.description())

# 访问类变量
print(f"物种: {Dog.species}")
print(f"我的狗的物种: {my_dog.species}")

# ==================== 封装和访问控制 ====================
print("\n=== 封装 ===")

class BankAccount:
    """银行账户类"""
    
    def __init__(self, owner, balance=0):
        self.owner = owner  # 公开属性
        self._account_id = "ABC123"  # 受保护属性（约定，单下划线）
        self.__balance = balance  # 私有属性（名称改编，双下划线）
    
    # Getter 方法
    def get_balance(self):
        """获取余额"""
        return self.__balance
    
    # Setter 方法
    def deposit(self, amount):
        """存款"""
        if amount > 0:
            self.__balance += amount
            print(f"存入 {amount} 元，余额: {self.__balance}")
        else:
            print("存款金额必须大于0")
    
    def withdraw(self, amount):
        """取款"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"取出 {amount} 元，余额: {self.__balance}")
        else:
            print("余额不足或金额无效")

account = BankAccount("张三", 1000)
print(f"账户所有者: {account.owner}")
print(f"当前余额: {account.get_balance()}")

account.deposit(500)
account.withdraw(300)

# 尝试直接访问私有属性（不推荐）
# print(account.__balance)  # 报错！
print(f"私有属性访问: {account._BankAccount__balance}")  # 可以但不推荐

# ==================== 属性装饰器 (@property) ====================
print("\n=== @property 装饰器 ===")

class Person:
    """人类"""
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self._age = age  # 使用下划线表示内部属性
    
    # 使用 @property 将方法变成属性
    @property
    def full_name(self):
        """全名（只读属性）"""
        return f"{self.first_name} {self.last_name}"
    
    @property
    def age(self):
        """获取年龄"""
        return self._age
    
    @age.setter
    def age(self, value):
        """设置年龄（带验证）"""
        if value >= 0:
            self._age = value
        else:
            raise ValueError("年龄不能为负数")
    
    @age.deleter
    def age(self):
        """删除年龄"""
        print("删除年龄属性")
        del self._age

person = Person("张", "三", 28)

# 像访问属性一样使用方法
print(f"全名: {person.full_name}")  # 不需要括号

# 使用 setter
print(f"原年龄: {person.age}")
person.age = 30  # 像赋值一样设置
print(f"新年龄: {person.age}")

# ==================== 继承 ====================
print("\n=== 继承 ===")

# 父类（基类）
class Animal:
    """动物基类"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        """发出声音（父类的通用实现）"""
        return f"{self.name} 发出声音"
    
    def describe(self):
        """描述动物"""
        return f"{self.name} 是一只 {self.species}"

# 子类（派生类）
class Cat(Animal):  # 继承 Animal
    """猫类"""
    
    def __init__(self, name, color):
        # 调用父类的构造函数
        super().__init__(name, "猫")
        self.color = color
    
    # 重写父类方法（覆盖）
    def make_sound(self):
        """猫的声音"""
        return f"{self.name} 说: 喵喵!"
    
    # 子类特有的方法
    def purr(self):
        """打呼噜"""
        return f"{self.name} 发出呼噜声"

class Dog(Animal):
    """狗类"""
    
    def __init__(self, name, breed):
        super().__init__(name, "狗")
        self.breed = breed
    
    def make_sound(self):
        """狗的声音"""
        return f"{self.name} 说: 汪汪!"
    
    def fetch(self):
        """捡球"""
        return f"{self.name} 去捡球了"

# 使用继承
cat = Cat("咪咪", "白色")
dog = Dog("旺财", "金毛")

print(cat.describe())  # 继承自父类
print(cat.make_sound())  # 重写的方法
print(cat.purr())  # 子类特有方法

print(dog.describe())
print(dog.make_sound())
print(dog.fetch())

# ==================== 多态 ====================
print("\n=== 多态 ===")

# 多态：不同的类可以定义相同的方法名
def animal_sound(animal):
    """让动物发出声音"""
    print(animal.make_sound())

# 同一个函数，不同的行为
animal_sound(cat)  # 喵喵
animal_sound(dog)  # 汪汪

# 多态的实际应用
animals = [
    Cat("小白", "白色"),
    Dog("大黄", "柴犬"),
    Cat("小黑", "黑色")
]

print("\n所有动物发声:")
for animal in animals:
    print(f"  {animal.make_sound()}")

# ==================== 类方法和静态方法 ====================
print("\n=== 类方法和静态方法 ===")

class MathUtils:
    """数学工具类"""
    
    pi = 3.14159  # 类变量
    
    def __init__(self):
        pass
    
    # 类方法（使用 @classmethod 装饰器）
    # 第一个参数是 cls（类本身），而不是 self
    @classmethod
    def circle_area(cls, radius):
        """计算圆的面积（类方法）"""
        return cls.pi * radius ** 2
    
    # 静态方法（使用 @staticmethod 装饰器）
    # 不需要 self 或 cls 参数
    @staticmethod
    def add(a, b):
        """加法（静态方法）"""
        return a + b
    
    @staticmethod
    def multiply(a, b):
        """乘法（静态方法）"""
        return a * b

# 类方法：可以通过类名直接调用
print(f"圆的面积: {MathUtils.circle_area(5)}")

# 静态方法：也可以通过类名直接调用
print(f"加法: {MathUtils.add(3, 5)}")
print(f"乘法: {MathUtils.multiply(3, 5)}")

# ==================== 特殊方法（魔术方法）====================
print("\n=== 特殊方法 ===")

class Book:
    """书籍类"""
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # __str__: 定义 print() 和 str() 的输出
    def __str__(self):
        return f"《{self.title}》 by {self.author}"
    
    # __repr__: 定义对象的"官方"字符串表示
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    # __len__: 定义 len() 的行为
    def __len__(self):
        return self.pages
    
    # __eq__: 定义 == 的行为
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False
    
    # __lt__: 定义 < 的行为（用于排序）
    def __lt__(self, other):
        return self.pages < other.pages

book1 = Book("Python 编程", "张三", 300)
book2 = Book("Swift 开发", "李四", 250)

print(f"打印书籍: {book1}")  # 调用 __str__
print(f"书籍表示: {repr(book1)}")  # 调用 __repr__
print(f"页数: {len(book1)}")  # 调用 __len__
print(f"两本书相等? {book1 == book2}")  # 调用 __eq__
print(f"book2 < book1? {book2 < book1}")  # 调用 __lt__

# 排序书籍
books = [book1, book2, Book("Java 编程", "王五", 400)]
sorted_books = sorted(books)  # 使用 __lt__ 排序
print("\n按页数排序:")
for book in sorted_books:
    print(f"  {book} - {len(book)} 页")

print("\n=== 练习题 ===")
print("1. 创建一个 Rectangle 类，包含长宽属性和计算面积、周长的方法")
print("2. 创建一个 Student 类，使用 @property 实现成绩的 getter 和 setter（带验证）")
print("3. 创建一个 Vehicle 基类，让 Car 和 Motorcycle 继承它")
print("4. 实现一个 Vector 类，支持加法运算（重载 __add__ 方法）")
