// ============================================================
// Dart 基础 - 变量和数据类型
// 适合有编程经验的开发者快速上手（与 LearnPython 同系列）
// ============================================================

// 入口函数：Dart 程序从 main() 开始执行
void main() {
  // ==================== 变量声明 ====================
  // 1. var：类型由编译器推断（推荐在局部使用）
  var name = '张三';
  var age = 28;
  var height = 1.75;
  var isDeveloper = true;

  print('姓名: $name, 年龄: $age, 身高: ${height}m, 是否开发者: $isDeveloper');
  // 说明：字符串中用 $变量名 或 ${表达式} 做插值，类似 Swift 的 \(var)

  // 2. 显式类型声明（提高可读性，尤其参数和字段）
  String city = '北京';
  int score = 100;
  double pi = 3.14;
  bool isActive = false;

  // 3. final：只能赋值一次（运行时常量）
  final now = DateTime.now(); // 运行时才确定
  // now = DateTime.now(); // 错误：final 不能再次赋值

  // 4. const：编译时常量，必须能在编译时计算出来
  const maxCount = 100;
  const appName = 'LearnFlutter';
  // const t = DateTime.now(); // 错误：编译时无法知道值

  // ==================== 基本数据类型 ====================

  // 1. 数字：int、double（没有 float，小数就是 double）
  int a = 1;
  double b = 2.5;
  // 字面量：整数字面量是 int，带小数的是 double
  var c = 3;   // int
  var d = 3.0; // double

  // 2. 字符串：单引号、双引号均可，推荐单引号
  String s1 = '单引号';
  String s2 = "双引号";
  String s3 = '''
  多行
  字符串
  ''';

  // 常用方法（与其它语言类似）
  var text = 'Hello Dart';
  print('长度: ${text.length}');
  print('大写: ${text.toUpperCase()}');
  print('小写: ${text.toLowerCase()}');
  print('分割: ${text.split(' ')}');
  print('替换: ${text.replaceAll('Dart', 'Flutter')}');

  // 3. 布尔：bool，只有 true / false（小写）
  bool flag = true;

  // ==================== 空安全（Null Safety）====================
  // Dart 2.12+ 默认开启：变量默认不能为 null，除非显式声明为可空类型

  // 不可空类型（默认）
  String title = 'Flutter';
  // title = null; // 错误：不能赋 null

  // 可空类型：在类型后加 ?
  String? nullableTitle;
  nullableTitle = 'Dart';
  nullableTitle = null; // 允许

  int? maybeCount;
  maybeCount = null;

  // 使用可空变量时要处理 null
  if (nullableTitle != null) {
    print('标题长度: ${nullableTitle.length}');
  }
  // 或使用空安全操作符
  print('标题长度: ${nullableTitle?.length}'); // 为 null 则整个表达式为 null
  print('标题长度: ${nullableTitle?.length ?? 0}'); // 为 null 时用 0
  // 断言非空：若为 null 会抛异常
  // print(nullableTitle!.length);

  // ==================== 类型转换 ====================
  String strNum = '123';
  int intNum = int.parse(strNum);
  double doubleNum = double.parse(strNum);
  String fromInt = 42.toString();
  String fromDouble = (3.14).toStringAsFixed(1); // "3.1"

  print('原始: $strNum, 转 int: $intNum, 转 double: $doubleNum');
  print('42.toString() = $fromInt, 3.14 保留1位 = $fromDouble');

  // ==================== 类型检查 ====================
  var value = 42;
  print('\nvalue 是 int: ${value is int}');
  print('value 是 String: ${value is String}');
  // 类型转换（安全）
  if (value is int) {
    print('value 作为 int: $value');
  }

  // ==================== 命名规范（与 Swift/Kotlin 一致）====================
  // 变量、方法、参数：camelCase
  var userName = '正确';
  // 类、枚举、typedef：PascalCase
  // 常量：camelCase 或 lowerCamelCase，有时全大写
  const defaultCount = 10;

  // ==================== 小结 ====================
  print('\n--- 小结 ---');
  print('var/final/const 声明变量；类型可写可不写');
  print('可空类型用 ?；使用 ?. 和 ?? 处理 null');
  print('字符串插值: \$var 或 \${expr}');
  print('Dart 用 camelCase，和移动端一致');
}
