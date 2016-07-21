/**
 slightly modified sieve of eratosthenes which instead of saving all primes,
 saves the sum of all the primes before a particular number
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
	primes := []int{0}
	for i := 1; i < n; i++{
		if c[i] == false{
			primes = append(primes, primes[len(primes) - 1] + i)
		} else {
			primes = append(primes, primes[len(primes) - 1])
		}
	}
	return primes
}

func main(){
	sums := sieveEratosthenes(10)
	sum := []int{}
	var T, n int
	fmt.Scanf("%d", &T)
	for T > 0 {
		fmt.Scanf("%d", &n)
		fmt.Println(primes[n - 1])
		T--
	}
}


