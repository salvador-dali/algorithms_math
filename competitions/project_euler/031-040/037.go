/**
 extract all the primes and save them into a map
 then for each prime check whether it is trancatable
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

func isTrancatable(n uint64, primes map[uint64]bool)bool{
	original := n
	digits := uint64(1)
	// check if it is trancatable from right
	for n > 9 {
		n /= 10
		digits *= 10
		if !primes[n]{
			return false
		}
	}

	// check if it is trancatable from left
	for original > 9 {
		original %= digits
		digits /= 10
		if !primes[original]{
			return false
		}
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

	sum := uint64(0)
	for _, v := range primes{
		if isTrancatable(v, primesMap){
			if v > 10{
				sum += v
			}
		}
	}
	fmt.Println(sum)
}
