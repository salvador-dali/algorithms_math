/**
 first of all the b should be a prime number. So generate all the primes below N.
 A should be odd number, because with even it will be divisible by 2.

 create a dict of primes in the region of n*n
 Iterate over all odd numbers a from -n to n,
 iterate over all primes b from -n to n
 for each a, b check how many primes will you get

 remember the best one
 */

package main
import (
	"fmt"
)

func sieveEratosthenes(n uint64)[]uint64{
	c := make([]bool, n)
	c[1] = true
	var p uint64 = 2
	var i, p2 uint64

	for {
		p2 = p * p
		if p2 >= n {
			break
		}
		for i = p2; i < n; i += p {
			c[i] = true
		}
		for {
			p++
			if !c[p] {
				break
			}
		}
	}

	primes := []uint64{}
	for i = 1; i < n; i++{
		if c[i] == false {
			primes = append(primes, i)
		}
	}
	return primes
}

func polyPrimes(a, b int, primes map[int]bool)int{
	total := 1
	for n := 1; true; n++{
		if primes[n * n + a * n + int(b)]{
			total++
		} else {
			break
		}
	}
	return total
}

func generateNumbers(n int){
	primesDict := map[int]bool{}
	smallPrimes := sieveEratosthenes(uint64(n))
	for _, v := range sieveEratosthenes(uint64(100 * n)){ // to be on the safe side n * n
		primesDict[int(v)] = true
	}
	if n % 2 == 0{
		n = - n + 1
	} else {
		n = -n
	}

	max := 0
	var bestA, bestB int
	for a := n; a <= -n; a+=2{
		for _, b := range smallPrimes{
			total := polyPrimes(a, int(b), primesDict)
			if max < total{
				max = total
				bestA = a
				bestB = int(b)
			}
		}
	}
	fmt.Println(bestA, bestB)
}

func main(){
    var n int
    fmt.Scanf("%d", &n)

	generateNumbers(n)
}

