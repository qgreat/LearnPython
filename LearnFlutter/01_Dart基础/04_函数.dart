// ============================================================
// Dart 基础 - 函数（参数、返回值、可选参数、闭包）
// 与 Swift/Kotlin 类似；Dart 支持命名参数和位置可选参数
// ============================================================

void main() {
  // ==================== 基本函数 ====================
  print('=== 基本函数 ===');

  // 返回类型可写 void 或具体类型；单表达式可用 => 简写
  String greet(String name) {
    return '你好, $name!';
  }

  print(greet('张三'));

  // 无返回值写 void
  void printInfo(String name, int age) {
    print('姓名: $name, 年龄: $age');
  }
  printInfo('李四', 30);

  // 单表达式函数可省略大括号，用 =>
  int square(int x) => x * x;
  print('5的平方: ${square(5)}');

  // ==================== 可选参数 ====================
  // 1. 可选位置参数：用 [] 包裹，放在最后
  print('\n=== 可选位置参数 ===');

  String say(String from, [String? to, String? msg]) {
    var result = '$from 说';
    if (to != null) result += ' 给 $to';
    if (msg != null) result += ': $msg';
    return result;
  }
  print(say('张三'));
  print(say('张三', '李四'));
  print(say('张三', '李四', '你好'));

  // 带默认值的可选位置参数
  String greet2(String name, [String title = '先生']) {
    return '你好, $title$name!';
  }
  print(greet2('王五'));
  print(greet2('王五', '女士'));

  // 2. 可选命名参数：用 {} 包裹，调用时用名字: 值
  print('\n=== 可选命名参数 ===');

  void describePet(String animalType, {String? petName, int age = 0}) {
    print('$petName 是一只 $age 岁的 $animalType');
  }
  describePet('狗', petName: '旺财', age: 3);
  describePet('猫', age: 2); // petName 为 null

  // 必选命名参数：用 required
  void createUser({required String name, int age = 0}) {
    print('用户: $name, $age 岁');
  }
  createUser(name: '赵六');
  createUser(name: '孙七', age: 25);

  // ==================== 返回值 ====================
  print('\n=== 返回值 ===');

  // 返回多个值：用 List 或 Map（Dart 3 也可用 Record）
  List<int> getMinMax(List<int> list) {
    if (list.isEmpty) return [0, 0];
    return [list.reduce((a, b) => a < b ? a : b),
            list.reduce((a, b) => a > b ? a : b)];
  }
  var minMax = getMinMax([3, 1, 4, 1, 5]);
  print('最小: ${minMax[0]}, 最大: ${minMax[1]}');

  // 返回 Map 也可
  Map<String, dynamic> getUser() {
    return {'name': '张三', 'age': 28, 'skills': ['Dart', 'Flutter']};
  }
  print('用户: ${getUser()['name']}');

  // ==================== 匿名函数与闭包 ====================
  print('\n=== 匿名函数 / Lambda ===');

  // 匿名函数：(参数) => 表达式 或 (参数) { 语句; return 值; }
  var add = (int a, int b) => a + b;
  print('add(3, 5) = ${add(3, 5)}');

  var numbers = [1, 2, 3, 4, 5];
  var squares = numbers.map((x) => x * x).toList();
  var evens = numbers.where((x) => x % 2 == 0).toList();
  print('平方: $squares, 偶数: $evens');

  // 函数作为参数
  int apply(int x, int y, int Function(int, int) op) {
    return op(x, y);
  }
  print('5+3 = ${apply(5, 3, (a, b) => a + b)}');
  print('5*3 = ${apply(5, 3, (a, b) => a * b)}');

  // 闭包：函数捕获外部变量
  Function makeCounter() {
    var count = 0;
    return () {
      count++;
      return count;
    };
  }
  var counter = makeCounter();
  print('counter: ${counter()}, ${counter()}, ${counter()}'); // 1, 2, 3

  // ==================== 顶层函数与 main ====================
  // 当前文件中的 greet、square 等都是在 main 外可再定义；这里为演示写在 main 内也可
  // 通常把复用函数提到 main 外

  print('\n--- 小结 ---');
  print('函数: 返回类型 函数名(参数) { } 或 => 表达式');
  print('可选位置参数: [a, b]；可选命名参数: {a, b}，required 表示必选');
  print('匿名函数: (参数) => 表达式；(参数) { }');
  print('闭包: 函数可捕获外层变量');
}
