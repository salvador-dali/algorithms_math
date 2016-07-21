/**
 the question boils down to finding a lcm of a multiple numbers
 */
package main

import "fmt"

func gcd(a, b uint64) uint64{
	var tmp uint64
	for b > 0 {
		tmp = a
		a = b
		b = tmp % a
	}

	return a
}

func lcm(a, b uint64) uint64{
	return a / gcd(a, b) * b
}

func main(){
	var T, n, i int
	var res uint64
	fmt.Scanf("%d", &T)
	for T > 0{
		res = 1
		fmt.Scanf("%d", &n)
		for i = 1; i <= n; i++ {
			res = lcm(res, uint64(i))
		}
		fmt.Println(res)
		T--
	}
}
