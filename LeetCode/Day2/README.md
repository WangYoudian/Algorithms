**LeetCode原题**  
[Linked List Cycle 1](https://leetcode.com/problems/linked-list-cycle/)  
[Linked List Cycle 2](https://leetcode.com/problems/linked-list-cycle-ii/)  
[Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)  
```
遇到的问题：主要在解决k个已排序好的链表合并过程中，想用分治思想，在时间复杂度$O(nklog_{2}n)$空间复杂度为常数下解决，  
但是对Python中的面向对象不够熟悉（当然根源还是数据结构知识不够扎实），导致卡在这个点上很长时间。  
真的是难cai！
```
关于使用分治写k个链表合并时候卡住的那个点。最简单的方式，就是照着C/C++对结构的数据和操作定义写出Python中对应的抽象数据类型的定义。  
因为链表合并并不难，但是基础不打牢就很难上一个台阶。  
Python中，在类的构造方法中，预先定义几个变量，就等价于结构体中的内部成员。而在链表操作中国，类似结构体指针Node \*的等价则为链表的头结点。  
由于对Python中类的使用仅停留在封装接口、继承、hasattr/setattr的简单概念上，暂时用不出什么炫酷的技巧。只能顺藤摸瓜了。
