// ============================================================
// Dart 基础 - 控制流（条件、循环）
// 与 Swift/Kotlin 类似：大括号表示代码块，条件不必加括号
// ============================================================

void main() {
  // ==================== 条件语句 ====================
  print('=== if / else if / else ===');

  int score = 85;
  if (score >= 90) {
    print('优秀');
  } else if (score >= 80) {
    print('良好');
  } else if (score >= 60) {
    print('及格');
  } else {
    print('不及格');
  }

  // 比较运算符：== != > < >= <=
  // 逻辑运算符：&& || !（注意是 ! 不是 not）

  int age = 25;
  bool isStudent = true;
  if (age >= 18 && !isStudent) {
    print('成年非学生');
  } else if (age >= 18 || isStudent) {
    print('成年或学生');
  }

  // 成员测试：contains（List/Set）
  var fruits = ['苹果', '香蕉', '橙子'];
  if (fruits.contains('苹果')) {
    print('列表中有苹果');
  }
  if (!fruits.contains('葡萄')) {
    print('列表中没有葡萄');
  }

  // 三元表达式：condition ? trueValue : falseValue
  String status = age >= 18 ? '成年' : '未成年';
  print('状态: $status');

  // ==================== for 循环 ====================
  print('\n=== for 循环 ===');

  var numbers = [1, 2, 3, 4, 5];
  for (var num in numbers) {
    print('数字: $num');
  }

  // 遍历字符串
  for (var char in 'Dart'.split('')) {
    print(char);
  }

  // 传统 for：for (初始化; 条件; 更新)
  for (var i = 0; i < 5; i++) {
    print('i = $i');
  }
  for (var i = 1; i <= 5; i++) {
    print('i = $i');
  }
  for (var i = 0; i < 10; i += 2) {
    print('偶数 i = $i');
  }

  // 带索引遍历：List 没有内置 enumerate，用 index 或 asMap()
  var langs = ['Dart', 'Swift', 'Kotlin'];
  for (var i = 0; i < langs.length; i++) {
    print('$i: ${langs[i]}');
  }
  langs.asMap().forEach((index, value) {
    print('第${index + 1}个: $value');
  });

  // 遍历 Map
  var user = {'name': '张三', 'age': 28, 'job': '开发者'};
  for (var entry in user.entries) {
    print('${entry.key} = ${entry.value}');
  }

  // ==================== while 循环 ====================
  print('\n=== while 循环 ===');

  var count = 0;
  while (count < 5) {
    print('计数: $count');
    count++; // Dart 支持 ++ / --
  }

  // do-while：先执行再判断
  var n = 0;
  do {
    print('do-while: $n');
    n++;
  } while (n < 3);

  // ==================== break 和 continue ====================
  print('\n=== break / continue ===');

  print('break 示例:');
  for (var i = 0; i < 10; i++) {
    if (i == 5) break;
    print(i);
  }

  print('continue 示例:');
  for (var i = 0; i < 10; i++) {
    if (i % 2 == 0) continue;
    print(i); // 只打印奇数
  }

  // ==================== switch ====================
  print('\n=== switch ===');

  var command = 'open';
  switch (command) {
    case 'open':
      print('打开');
      break; // Dart 的 switch 必须 break，否则会 fall-through
    case 'close':
      print('关闭');
      break;
    case 'save':
      print('保存');
      break;
    default:
      print('未知命令');
  }

  // switch 可针对多种类型；支持枚举、字符串等
  var value = 2;
  switch (value) {
    case 1:
      print('一');
      break;
    case 2:
      print('二');
      break;
    default:
      print('其他');
  }

  // ==================== 小结 ====================
  print('\n--- 小结 ---');
  print('if/else、for、while、do-while、switch');
  print('for-in 遍历集合；传统 for(i;i<n;i++) 可用');
  print('三元: condition ? a : b');
  print('逻辑: && || !');
}
