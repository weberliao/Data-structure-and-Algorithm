## mergesort
-----------------------------------
拆解:先把數列拆解成一半，且持續切割到只剩下一個數字。                                                                   
合併:再兩兩互相合併成新數列。合併過程完成排序。屬於Divide and Conquer的演算法來執行


## 學習歷程
與heapsort一樣，都是先自己畫完流程圖後，就會比較知道一開始該定義的函數、需要的程式碼是那些。最後找出需要用迴圈、if else跑出的地方。

首先
```class solution( ):
    def merge_sort(nums):
                     if len(nums) <=1 :
                             return nums
                        else :
                        middle = len(nums)//2
                        left= nums[:middle]
                        right = nums[len(nums)-leftlen]
```                        
這是一開始看流程圖需要的地方

2.再來就是要用迴圈分割到最小的地方，發現值些用分割成最小的比較反而比較方便

3.最後發現上述用到的程式碼必須放在```def merge_sort(nums):```裡，放在其他藉由self自訂函數，會偵測不到功能
<img src="https://github.com/weberliao/Data-structure-and-Algorithm/blob/README.md/merge.jpg" height='700' weight='550'>






## 流程圖
<img src="https://github.com/weberliao/Data-structure-and-Algorithm/blob/README.md/mergesort.png" height='500' weight='350'>
