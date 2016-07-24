/**
 get all the primes in our diapason with sieve and store them in the dictionary
 then for each prime check whether it is circularPrime, by creating each circular number
 and checking if it is in primes.

 At the end just sum all such primes
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

func isCircular(n uint64, primes map[uint64]bool)bool{
	digits := 0
	pow := uint64(1)
	tmp := n
	for n > 9{
		n /= 10
		digits++
		pow *= 10
	}


	for i:=0; i <= digits; i++{
		if !primes[tmp]{
			return false
		}
		tmp = tmp / 10 + (tmp % 10) * pow
	}
	return true
}

func main(){
	var n uint64
	fmt.Scanf("%d", &n)
	primesMap := map[uint64]bool {}
	primes := sieveEratosthenes(n)
	for _, v := range primes{
		primesMap[v] = true
	}

	var totalSum uint64 = 0
	for _, v := range primes{
		if isCircular(v, primesMap){
			//fmt.Println(v)
			totalSum += v
		}
	}
	fmt.Println(totalSum)
}
