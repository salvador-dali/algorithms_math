/**
 a shorter version of a factorization algorithm where you do not need to worry about
 all the primes and remember only the last (biggest one)
 */

package main

import (
	"fmt"
	"math"
)

func helper(n uint64){
	var p uint64 = 1
	var i uint64
	for i = 2; i < uint64(math.Sqrt(float64(n))) + uint64(1); i++ {
		for n % i == 0 {
			n /= i
			p = i
		}
	}
    if n > 1 {
        p = n
    }
	fmt.Println(p)
}

func main(){
	var T, n int
	fmt.Scanf("%d", &T)
    for T > 0{
		T--
		fmt.Scanf("%d", &n)
		helper(uint64(n))
	}
}
