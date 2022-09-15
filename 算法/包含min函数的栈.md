## 题目：

​		定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数，并且调用 min函数、push函数 及 pop函数的时间复杂度都是 O(1)



push(value)：将value压入栈中

pop()：弹出栈顶元素

top()：获取栈顶元素

min()：获取栈中最小元素

示例：

输入：["PSH-1","PSH2","MIN","TOP","POP","PSH1","TOP","MIN"]

输出：-1,2,1,-1

解析：

"PSH-1" 表示将-1压入栈中，栈中元素为 -1

"PSH2" 表示将2压入栈中，栈中元素为 2，-1

“MIN” 表示获取此时栈中最小元素==>返回 -1

"TOP" 表示获取栈顶元素==>返回 2

"POP" 表示弹出栈顶元素，弹出 2，栈中元素为 -1

"PSH-1" 表示将1压入栈中，栈中元素为 1，-1

"TOP" 表示获取栈顶元素==>返回 1

“MIN” 表示获取此时栈中最小元素==>返回 -1



## 题解：

**辅助栈**

```java
public class Solution {

    int[] stack = new int[50];
    int top = -1;

    int[] mins = new int[10];
    int index = -1;

    public void push(int node) {
        if (top < 0){
            index ++;
            mins[index] = node;
        } else {
            if (mins[index] >= node){
                index ++;
                mins[index] = node;
            }
        }

        top ++;
        stack[top] = node;
    }

    public void pop() {
        if (stack[top] == mins[index]){
            index --;
        }
        top --;
    }

    public int top() {
        return stack[top];
    }

    public int min() {
        return mins[index];
    }
}
```

