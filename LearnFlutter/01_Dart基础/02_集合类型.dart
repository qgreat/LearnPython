// ============================================================
// Dart 基础 - 集合类型（List、Set、Map）
// 对应 Python 的 list、set、dict，与 Swift/Kotlin 的 Array/List、Set、Dictionary/Map 类似
// ============================================================

void main() {
  // ==================== List（列表）- 有序、可重复、可变 ====================
  // 类似 Python 的 list、Swift 的 Array、Kotlin 的 List/MutableList

  // 创建列表：字面量或构造函数
  List<String> fruits = ['苹果', '香蕉', '橙子'];
  var numbers = [1, 2, 3, 4, 5];
  List<dynamic> mixed = [1, 'hello', true, 3.14]; // 混合类型用 dynamic

  print('=== List 操作 ===');
  // 访问元素（下标从 0 开始）
  print('第一个: ${fruits[0]}, 最后一个: ${fruits[fruits.length - 1]}');
  print('第一个: ${fruits.first}, 最后一个: ${fruits.last}'); // 便捷属性

  // 切片：sublist(起始, 结束)，结束索引不包含
  print('前两个: ${numbers.sublist(0, 2)}');   // [1, 2]
  print('从索引2开始: ${numbers.sublist(2)}'); // [3, 4, 5]

  // 修改列表
  fruits.add('葡萄');           // 末尾添加
  fruits.insert(1, '芒果');     // 指定位置插入
  fruits.remove('香蕉');        // 按值删除（只删第一个）
  fruits.removeAt(0);          // 按索引删除
  print('修改后: $fruits');

  // 常用方法
  var nums = [3, 1, 4, 1, 5, 9, 2, 6];
  print('长度: ${nums.length}');
  print('包含 4: ${nums.contains(4)}');
  print('索引 of 1: ${nums.indexOf(1)}');
  nums.sort();                 // 原地排序
  print('排序后: $nums');
  print('反转: ${nums.reversed.toList()}'); // reversed 返回迭代器，需 toList()

  // 列表推导式风格：用 map、where、toList()
  var squares = numbers.map((x) => x * x).toList();        // [1, 4, 9, 16, 25]
  var evens = numbers.where((x) => x % 2 == 0).toList();   // [2, 4]
  print('平方: $squares, 偶数: $evens');

  // 不可变列表：const 或 List.unmodifiable
  const fixedList = [1, 2, 3];
  // fixedList.add(4); // 运行时报错

  // ==================== Set（集合）- 无序、唯一、可变 ====================
  // 自动去重，类似 Python 的 set、Swift 的 Set

  Set<String> colors = {'红', '绿', '蓝'};
  var numbersSet = {1, 2, 3, 3, 4, 5, 5}; // 字面量推断为 Set<int>，去重
  print('\n=== Set 操作 ===');
  print('去重后: $numbersSet');

  colors.add('黄');
  colors.remove('绿');
  colors.remove('紫'); // 不存在不会报错
  print('颜色: $colors');

  // 集合运算
  var set1 = {1, 2, 3, 4};
  var set2 = {3, 4, 5, 6};
  print('并集: ${set1.union(set2)}');
  print('交集: ${set1.intersection(set2)}');
  print('差集: ${set1.difference(set2)}');

  // 成员测试
  print('包含 红: ${colors.contains('红')}');

  // ==================== Map（映射）- 键值对 ====================
  // 类似 Python 的 dict、Swift 的 Dictionary、Kotlin 的 Map

  Map<String, dynamic> user = {
    'name': '李四',
    'age': 30,
    'job': 'iOS 开发者',
    'skills': ['Swift', 'Objective-C', 'UIKit'],
  };

  print('\n=== Map 操作 ===');
  // 访问
  print('姓名: ${user['name']}');
  print('年龄: ${user['age']}');
  print('城市: ${user['city'] ?? '未知'}'); // 键不存在用 ?? 给默认值

  // 修改
  user['age'] = 31;
  user['city'] = '北京';
  user.remove('job');
  print('修改后: $user');

  // 常用方法
  print('键: ${user.keys.toList()}');
  print('值: ${user.values.toList()}');
  print('键值对: ${user.entries.map((e) => '${e.key}:${e.value}').toList()}');

  // 遍历
  user.forEach((key, value) {
    print('  $key => $value');
  });

  // ==================== 常用泛型写法 ====================
  // List<int>、Set<String>、Map<String, int> 等
  List<int> intList = [1, 2, 3];
  Map<String, int> scores = {'语文': 90, '数学': 85};

  // ==================== 小结 ====================
  print('\n--- 小结 ---');
  print('List: 有序可重复，[] 或 List<T>');
  print('Set: 无序唯一，{} 或 Set<T>（注意 {} 空的是 Map，空 Set 用 Set()）');
  print('Map: 键值对，{k:v} 或 Map<K,V>');
  print('遍历: for-in、forEach、map/where 等');
}
