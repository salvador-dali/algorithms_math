/**
 the task is straightforward.
 Generate all the permutations of numbers, then check whether each number satisfy the
 properties.
 */

package main
import (
	"fmt"
)

func permutations(arr []int)[][]int{
	var helper func([]int, int)
	res := [][]int{}

	helper = func(arr []int, n int){
        if n == 1{
			tmp := make([]int, len(arr))
			copy(tmp, arr)
			res = append(res, tmp)
		} else {
			for i := 0; i < n; i++{
				helper(arr, n - 1)
				if n % 2 == 1{
					tmp := arr[i]
					arr[i] = arr[n - 1]
					arr[n - 1] = tmp
				} else {
					tmp := arr[0]
					arr[0] = arr[n - 1]
					arr[n - 1] = tmp
				}
			}
		}
    }

	helper(arr, len(arr))
	return res
}

func num(arr []int)int{
	tmp := 1
	res := 0
	for i := len(arr); i > 0; i--{
		res += arr[i - 1] * tmp
		tmp *= 10
	}
	return res
}

func checkNumber(arr []int) bool{
	if num(arr[1:4]) % 2 != 0{ return false}
	if len(arr) >= 5{
		if num(arr[2:5]) % 3 != 0{ return false}
	}
	if len(arr) >= 6{
		if num(arr[3:6]) % 5 != 0{ return false}
	}

	if len(arr) >= 7{
		if num(arr[4:7]) % 7 != 0{ return false}
	}

	if len(arr) >= 8{
		if num(arr[5:8]) % 11 != 0{ return false}
	}

	if len(arr) >= 9{
		if num(arr[6:9]) % 13 != 0{ return false}
	}

	if len(arr) >= 10{
		if num(arr[7:10]) % 17 != 0{ return false}
	}
	return true
}

func main(){
	var n int
    fmt.Scanf("%d", &n)
	arr := []int{}
	for i:=0; i<=n; i++{
		arr = append(arr, i)
	}

	allNumbers := permutations(arr)
	sum := 0
	for _, v := range(allNumbers){
		if checkNumber(v){
			sum += num(v)
		}
	}
	fmt.Println(sum)
}
