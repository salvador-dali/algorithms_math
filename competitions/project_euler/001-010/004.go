/**
 for all three digit number i, j check if the product is a palindrome
 if it is add it to the array. Sort the array and and then find solution to each
 test case in log(n) where n is the size of an array
 */
package main

import (
	"fmt"
	"sort"
)

func reverse(num int) int{
	var num2 int = 0
	for num > 0{
		num2 = (num2 + num % 10) * 10
		num /= 10
	}

	return num2 / 10
}

func generate()[]int{
	var i, j, res int
	var list []int
	for i = 100; i < 1000; i++{
		for j = i + 1; j < 1000; j++{
			res = i * j
			if res > 100000 && res == reverse(res){
				list = append(list, res)
			}
		}
	}

	sort.Ints(list)
	return list
}

func main(){
	var list []int = generate()
	var T, n, i int
	fmt.Scanf("%d", &T)
	for T > 0{
		T--
		fmt.Scanf("%d", &n)
		i = sort.Search(len(list), func(i int) bool { return list[i] >= n })
		fmt.Println(list[i])
	}


}
