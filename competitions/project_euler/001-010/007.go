/**
 precalculate primes using sieve of eratosthenes, remembering that number there are approximately
 n/log(n) primes before n. Then access all the number from an array.
 */
package main
import (
	"fmt"
)

func sieveEratosthenes(n int)[]int{
	c := make([]bool, n)
	c[1] = true
	p := 2
	for {
		p2 := p * p
		if p2 >= n {
			break
		}
		for i := p2; i < n; i += p {
			c[i] = true
		}
		for {
			p++
			if !c[p] {
				break
			}
		}
	}
	primes := []int{}
	for i := 1; i < n; i++{
		if c[i] == false{
			primes = append(primes, i)
		}
	}
	return primes
}

func main(){
	primes := sieveEratosthenes(110000)
	var T, n int
	fmt.Scanf("%d", &T)
	for T > 0 {
		fmt.Scanf("%d", &n)
		fmt.Println(primes[n - 1])
		T--
	}
}


