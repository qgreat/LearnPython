// ============================================================
// Dart 基础 - 类和对象（封装、继承、多态）
// 对移动端开发者来说概念与 Swift/Kotlin 类似
// ============================================================

void main() {
  // ==================== 基本类 ====================
  print('=== 基本类 ===');

  // 类定义：与 Swift/Kotlin 类似
  var myDog = Dog('旺财', 3);
  var yourDog = Dog('小白', 2);

  print('我的狗: ${myDog.name}, ${myDog.age}岁');
  print(myDog.bark());
  print(yourDog.description());
  print('物种: ${Dog.species}'); // 类变量

  // ==================== 封装与私有 ====================
  print('\n=== 封装 ===');

  var account = BankAccount('张三', 1000);
  print('所有者: ${account.owner}');
  print('余额: ${account.balance}');
  account.deposit(500);
  account.withdraw(300);
  // account._balance; // 同一库内可访问；其他文件不可（Dart 库私有是下划线前缀）

  // ==================== 继承 ====================
  print('\n=== 继承 ===');

  var cat = Cat('咪咪', '白色');
  var dog2 = Dog2('旺财', '金毛');
  print(cat.describe());
  print(cat.makeSound());
  print(cat.purr());
  print(dog2.describe());
  print(dog2.makeSound());
  print(dog2.fetch());

  // ==================== 多态 ====================
  print('\n=== 多态 ===');

  animalSound(cat);
  animalSound(dog2);

  List<Animal> animals = [Cat('小白', '白'), Dog2('大黄', '柴犬')];
  for (var a in animals) {
    print('  ${a.makeSound()}');
  }

  // ==================== 类方法与静态方法 ====================
  print('\n=== 类方法 / 静态方法 ===');

  print('圆面积: ${MathUtils.circleArea(5)}');
  print('加法: ${MathUtils.add(3, 5)}');
  print('乘法: ${MathUtils.multiply(3, 5)}');

  print('\n--- 小结 ---');
  print('class 类名 { 字段; 构造函数; 方法 }');
  print('私有：下划线前缀 _name（库内可见）');
  print('继承: class B extends A；super 调用父类');
  print('static 类成员；工厂构造函数等可后续学');
}

// ---------------------------------------------------------------------------
// 类定义（通常放在 main 外或单独文件）
// ---------------------------------------------------------------------------

class Dog {
  // 实例字段
  String name;
  int age;

  // 类变量（静态，所有实例共享）
  static String species = '犬科动物';

  // 构造函数：与类同名
  Dog(this.name, this.age); // 简写：this.name 表示把参数赋给同名字段

  String bark() => '$name 说: 汪汪!';
  String description() => '$name 今年 $age 岁';
}

// 封装：下划线前缀表示库内私有（同一文件可访问，其他文件不可）
class BankAccount {
  String owner;
  double _balance; // 私有字段

  BankAccount(this.owner, [this._balance = 0]);

  double get balance => _balance; // getter

  void deposit(double amount) {
    if (amount > 0) {
      _balance += amount;
      print('存入 $amount，余额: $_balance');
    }
  }

  void withdraw(double amount) {
    if (amount > 0 && amount <= _balance) {
      _balance -= amount;
      print('取出 $amount，余额: $_balance');
    }
  }
}

// ---------------------------------------------------------------------------
// 继承
// ---------------------------------------------------------------------------

class Animal {
  String name;
  String species;
  Animal(this.name, this.species);

  String makeSound() => '$name 发出声音';
  String describe() => '$name 是一只 $species';
}

class Cat extends Animal {
  String color;
  Cat(String name, this.color) : super(name, '猫'); // 调用父类构造

  @override
  String makeSound() => '$name 说: 喵喵!';

  String purr() => '$name 发出呼噜声';
}

class Dog2 extends Animal {
  String breed;
  Dog2(String name, this.breed) : super(name, '狗');

  @override
  String makeSound() => '$name 说: 汪汪!';

  String fetch() => '$name 去捡球了';
}

void animalSound(Animal animal) {
  print(animal.makeSound());
}

// ---------------------------------------------------------------------------
// 静态方法 / 类方法
// ---------------------------------------------------------------------------

class MathUtils {
  static const double pi = 3.14159;

  static double circleArea(double radius) => pi * radius * radius;
  static int add(int a, int b) => a + b;
  static int multiply(int a, int b) => a * b;
}
