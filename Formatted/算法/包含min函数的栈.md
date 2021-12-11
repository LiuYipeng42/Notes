## 题目：&emsp;  
&emsp;  
​&emsp;&emsp;定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数，并且调用 min函数、push函数 及 pop函数的时间复杂度都是 O(1)&emsp;  
&emsp;  
push(value)：将value压入栈中&emsp;  
&emsp;  
pop()：弹出栈顶元素&emsp;  
&emsp;  
top()：获取栈顶元素&emsp;  
&emsp;  
min()：获取栈中最小元素&emsp;  
&emsp;  
示例：&emsp;  
&emsp;  
输入：["PSH-1","PSH2","MIN","TOP","POP","PSH1","TOP","MIN"]&emsp;  
&emsp;  
输出：-1,2,1,-1&emsp;  
&emsp;  
解析：&emsp;  
&emsp;  
"PSH-1" 表示将-1压入栈中，栈中元素为 -1&emsp;  
&emsp;  
"PSH2" 表示将2压入栈中，栈中元素为 2，-1&emsp;  
&emsp;  
“MIN” 表示获取此时栈中最小元素==>返回 -1&emsp;  
&emsp;  
"TOP" 表示获取栈顶元素==>返回 2&emsp;  
&emsp;  
"POP" 表示弹出栈顶元素，弹出 2，栈中元素为 -1&emsp;  
&emsp;  
"PSH-1" 表示将1压入栈中，栈中元素为 1，-1&emsp;  
&emsp;  
"TOP" 表示获取栈顶元素==>返回 1&emsp;  
&emsp;  
“MIN” 表示获取此时栈中最小元素==>返回 -1&emsp;  
&emsp;  
## 题解：&emsp;  
&emsp;  
**辅助栈**&emsp;  
&emsp;  
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
&emsp;  
&emsp;  
