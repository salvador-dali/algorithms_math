// rewrite it by using divisorSieve from 021.go

package main

import (
	"fmt"
	"math"
	"time"
)

func factorize(n int) []int {
	factors := []int{}
	for i := 2; i*i <= n; i++ {
		for n % i == 0 {
			factors = append(factors, i)
			n /= i
		}
	}
	if n > 1 {
		factors = append(factors, n)
	}
	return factors
}

func divisorsSum(n int) int {
	dict, res := map[int]int{}, 1.0
	for _, v := range factorize(n) {
		dict[v] += 1
	}
	for p, a := range dict {
		res *= (math.Pow(float64(p), float64(a) + 1.0) - 1) / (float64(p) - 1)
	}
	return int(res) - n
}

func search(n, max int, sums []int) (bool, int, int){
	start, seen, count := n, map[int]bool{}, 0
	for {
		if n >= max || n == 0 || seen[n] {
			break
		}
		seen[n] = true

		n = sums[n]
		count += 1
	}

	if n == start {
		return true, n, count
	}
	return false, 0, 0
}

func amicableChain(n int){
	start := time.Now()
	sums := make([]int, n + 1)
	for i := 2; i <= n; i++ {
		sums[i] = divisorsSum(i)
	}
	elapsed := time.Since(start)
	fmt.Println(elapsed)

	biggestFound := 0
	for i := 2; i <= n; i++ {
		if ok, n, c := search(i, n, sums); ok {
			if c > biggestFound {
				biggestFound = c
				fmt.Println(n, c)
			}

		}
	}
}

func main() {
	start := time.Now()

	amicableChain(10000000)

	elapsed := time.Since(start)
	fmt.Println(elapsed)

}

