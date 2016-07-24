/**
 create an array of factorials of the digits (serve as cache)
 then iterate over all the numbers, parse them into digits and sum their factorials
 if the last sum is divisible by the number, then it is interesting

 sum all interesting numbers
 */

package main
import (
	"fmt"
)

func test(n int, factorials []uint64) bool{
	sum := uint64(0)
	tmp := uint64(n)
	for n > 0{
		sum += factorials[n % 10]
		n /= 10
	}
	if sum % tmp == 0{
		return true
	} else {
		return false
	}
}

func main(){
	var n int
	fmt.Scanf("%d", &n)
	factorials := []uint64{1}
	f := uint64(1)
	for i := uint64(1); i < 10; i++{
		f *= i
		factorials = append(factorials, f)
	}

	totalSum := 0
	for i := 10; i < n; i++{
		if test(i, factorials){
			totalSum += i
			fmt.Println(i)
		}
	}
	fmt.Println(totalSum)
}
