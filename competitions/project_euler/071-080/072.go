/**
 Generate the number of fractions in Farey series of order n: http://oeis.org/A005728
 http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fractions/fareySB.html
 F_n = F_{n-1} + \phi (n) = 1 + \sum_{i=1}^{n}\phi(i)
 from http://en.wikipedia.org/wiki/Farey_sequence
 http://www.cse.iitd.ernet.in/~mcs103480/farey-icip-100525.pdf
 */

package main

import (
	"fmt"
	"bufio"
	"strconv"
	"os"
)

func readManyNumbers() []int {
	var T int
	fmt.Scanf("%d", &T)

	scanner, numbers := bufio.NewScanner(os.Stdin), []int{}
	for T > 0 {
		T--
		scanner.Scan()
		num, _ := strconv.Atoi(scanner.Text())
		numbers = append(numbers, num)
	}
	return numbers
}

func divisorSieve(n uint64) []uint64 {
	sieve := []uint64{}
	for i := uint64(0); i < n+1; i++ {
		if i%2 == 0 {
			sieve = append(sieve, 2)
		} else {
			sieve = append(sieve, 0)
		}
	}
	sieve[0] = 0

	p := uint64(3)
	for p*p <= n {
		for i := p; i <= n; i += p {
			if sieve[i] == 0 {
				sieve[i] = p
			}
		}

		for p < n+1 && sieve[p] > 0 {
			p += 2
		}
	}

	for p < n+1 {
		if sieve[p] == 0 {
			sieve[p] = p
		}
		p += 2
	}
	return sieve
}

func getTotientFromSieve(sieve []uint64, num uint64) uint64 {
	res := num
	prevDivisor := uint64(1)
	for num > 1 {
		k := sieve[num]
		if k != prevDivisor {
			res = res/k*(k-1)
		}
		num /= k
		prevDivisor = k
	}
	return res
}

func generateFarey(n uint64) []uint64 {
	sieve := divisorSieve(n)
	farey := make([]uint64, n+1)
	farey[0] = 1
	for i := uint64(1); i < n+1; i++ {
		farey[i] = farey[i-1]+getTotientFromSieve(sieve, uint64(i))
	}
	return farey
}

func main() {
	max := 0
	arr := readManyNumbers()
	for _, v := range (arr) {
		if v > max {
			max = v
		}
	}

	farey := generateFarey(uint64(max + 3))
	for _, v := range (arr) {
		fmt.Println(farey[v] - 2)
	}
}
