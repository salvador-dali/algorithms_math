/**
 just keep track on how many digits have we encountered so far.
 break quickly if at least one is 0, bigger than k or
 if we have seen such digit
 */

package main

import (
	"fmt"
)

func pandigital(n, k int)bool{
	digits := make([]int, k + 1)
	for i := 1; i < 10; i++{
		tmp := n * i
		for tmp > 0{
			digit := tmp % 10
			if digit == 0 || digit > k || digits[digit] == 1{
				return false
			}
			digits[digit] = 1
			tmp /= 10
		}

		sum := 0
		for _, v := range(digits){
			sum += v
		}
		if sum == k {
			return true
		}
	}
	return false
}

func main(){
    var n, k int
    fmt.Scanf("%d %d", &n, &k)
	for i:= 2; i < n; i++{
		if pandigital(i, k){
			fmt.Println(i)
		}
	}
}
