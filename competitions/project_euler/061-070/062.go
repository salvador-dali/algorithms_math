/**
 for each of the numbers from 1 to N, store all the digits of i^3 in the array
  this array will be the key for the dictionary. The value will be the array of I
  after all the dictionary is generated, iterate over it and use only the values, where len() ==k
  get the smallest of these value

  then store all of them in another array, which you will sort and print
 */

package main
import (
	"fmt"
	"sort"
)

func convertN(n int)[10]uint8{
	num := n * n * n
	digits := [10]uint8{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
	for num > 0{
		digits[num % 10] += 1
		num /= 10
	}
	return digits
}

func findMin(arr []int)int{
	min := arr[0]
	for _, v := range arr{
		if v < min{
			min = v
		}
	}
	return min
}

func analysis(n, k int)[]int{
	res := []int{}
	dictionary := map[[10]uint8][]int{}

	for i := 1; i < n; i++{
		digits := convertN(i)
		dictionary[digits] = append(dictionary[digits], i)
	}

	for _, value := range(dictionary){
		if len(value) == k{
			res = append(res, findMin(value))
		}
	}
	return res
}

func main(){
	var n, k int
	fmt.Scanf("%d %d", &n, &k)
	res := analysis(n, k)
	sort.Ints(res)
	for _, v := range(res){
		fmt.Println(uint64(v) * uint64(v) * uint64(v))
	}
}
