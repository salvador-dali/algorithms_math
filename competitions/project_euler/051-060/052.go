/**
 iterate over each number and check whether
 x and 2x is permutation, then x and 3x and so on, if not, then iterate next one
 */
package main

import (
	"fmt"
	"math"
)

func isPermutation(n, m uint64)bool{
	if math.Floor(math.Log10(float64(n))) != math.Floor(math.Log10(float64(m))){
		return false
	}
	arr1 := [10]uint8{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
	arr2 := [10]uint8{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
	for n > 0{
		arr1[uint8(n % 10)]++
		n /= 10
	}

	for m > 0{
		arr2[uint8(m % 10)]++
		m /= 10
	}

	return arr1 == arr2
}

func main(){
	n := uint64(125875)
	k := uint64(2)

	for x := uint64(1); x <= n; x++{
		count := uint64(0)
		for i := uint64(2); i <= k; i++{
			if !isPermutation(x, i * x){
				break
			}
			count++
		}
		if count == k - 1{
			for i := uint64(1); i < k; i++{
				fmt.Print(x * i, " ")
			}
			fmt.Println(x * k, " ")
		}
	}
}
