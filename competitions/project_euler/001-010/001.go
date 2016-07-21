/**
 to find the sum of all the numbers, one need to add all the numbers divisible by 3
 and all divisible by 5 and subtract sum of numbers divisible by 5.
 Sums can be found as arithmetic progression
 */
package main

import "fmt"

func helper(n uint64) uint64{
	var n_3 uint64 = n / 3
	var n_5 uint64 = n / 5
	var n_15 uint64 = n / 15

	return uint64(3) * n_3 * (n_3 + 1) / 2 + uint64(5) * n_5 * (n_5 + 1) / 2 - uint64(15) * n_15 * (n_15 + 1) / 2
}

func main(){
	var T int
	fmt.Scanf("%d", &T)
	for T > 0 {
		var n uint64
		fmt.Scanf("%d", &n)
		fmt.Println(helper(n - uint64(1)))
		T--
	}
}

