### 题目：&emsp;  
&emsp;  
​&emsp;&emsp;给定一个数组，找出其中最小的K个数。例如数组元素是4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。&emsp;  
&emsp;  
## 题解：&emsp;  
&emsp;  
​&emsp;&emsp;可以利用堆（PriorityQueue）和快速排序来解决。&emsp;  
&emsp;  
​&emsp;&emsp;在快速排序的算法中，每次（getIndex方法）找到的都是 L 位置上的数的正确排序位置，这个位置左边的数小于 L 位置上的数，右边的数大于 L 位置上的数。所以要找到 k 个最小的数，就要找到一个正确排序位置为 k 的数，这个数的左边就是 k 个最小的数。&emsp;  
&emsp;  
```java
import java.util.*;

public class Solution {

    // 快排思想
    public ArrayList<Integer> GetLeastNumbers_Solution(int[] input, int k) {
        if (input == null || input.length < k || k <= 0) {
            return new ArrayList<>(0);
        }

        ArrayList<Integer> list = new ArrayList<>(k);
        
        int low = 0, high = input.length - 1, mid;
        
        while (low != high) {
            mid = getIndex(input, low, high);
            if (k == mid) {  // 找到理想的分割点
                break;
            } else if (k > mid) {  // 下一次对右边分区
                low = mid + 1;
            } else {  // 下一次对左边分区
                high = mid - 1;
            }
        }

        for (int i = 0; i < k; i++) {
            list.add(input[i]);
        }

        return list;
    }
    
    // 快排的分区函数
	private static int getIndex(int[] arr, int low, int high) {
		int tmp = arr[low];
		while (low < high) {
			while (low < high && arr[high] >= tmp) {
				high--;
			}
			arr[low] = arr[high];
			while (low < high && arr[low] <= tmp) {
				low++;
			}
			arr[high] = arr[low];

		}
		arr[low] = tmp;
		return low;
	}
}
```
&emsp;  
&emsp;  
&emsp;  
**快速排序**&emsp;  
&emsp;  
```java
public class QuickSort {
	public static void main(String[] args) {
		int[] arr = { 49, 38, 65, 97, 23, 22, 76, 1, 5, 8, 2, 0, -1, 22 };
		quickSort(arr, 0, arr.length - 1);
		System.out.println("排序后:");
		for (int i : arr) {
			System.out.println(i);
		}
	}

	private static void quickSort(int[] arr, int low, int high) {
		if (low < high) {
			// 找寻基准数据的正确索引
			int index = getIndex(arr, low, high);

			// 进行迭代对 index 之前和之后的数组进行相同的操作使整个数组变成有序
			quickSort(arr, low, index - 1);
			quickSort(arr, index + 1, high);
		}
	}

	private static int getIndex(int[] arr, int low, int high) {
		// 基准数据
        // 将 arr[low] 的值保存入 tmp，以便让出位置进行数组中元素的交换
		int tmp = arr[low];
		while (low < high) {
			// 当队尾的元素大于等于基准数据时,向前挪动 high 指针
			while (low < high && arr[high] >= tmp) {
				high--;
			}
			// 如果队尾元素小于 tmp 了,需要将其赋值给 low，因为 low 的位置是个空位置
			arr[low] = arr[high];
			// 当队首元素小于等于 tmp 时,向前挪动 low 指针
			while (low < high && arr[low] <= tmp) {
				low++;
			}
			// 当队首元素大于 tmp 时,需要将其赋值给 high，因为 high 的位置是个空位置
			arr[high] = arr[low];

		}
		// 跳出循环时 low 和 high 相等,此时的 low 或 high 就是 tmp 的正确索引位置
		// 由原理部分可以很清楚的知道 low 位置的值并不是 tmp ,所以需要将 tmp 赋值给 arr[low]
		arr[low] = tmp;
		return low; // 返回 tmp 的正确位置
	}
}
```
&emsp;  
&emsp;  
