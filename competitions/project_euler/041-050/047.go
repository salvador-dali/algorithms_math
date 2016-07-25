/**
 factorize each number and get its set of primes.
 Take number + k - 1, because we will need to check the last number as well
 then iterate over all the numbers and if one of them has len(set) == k, check k-1 number after it
 */

package main
import (
	"fmt"
)

func divisorSieve(n uint64) []uint64{
	sieve := []uint64{}
	for i:= uint64(0); i < n + 1; i++{
		if i % 2 == 0{
			sieve = append(sieve, 2)
		} else {
			sieve = append(sieve, 0)
		}

	}
	sieve[0] = 0
	sieve[1] = 0

	p := uint64(3)
	for p * p <= n {
		for i := p; i <= n; i += p {
			if sieve[i] == 0 {
				sieve[i] = p
			}
		}

		for p < uint64(len(sieve)) && sieve[p] > 0{
			p += 2
		}
	}

	for p < n + 1 {
		if sieve[p] == 0 {
			sieve[p] = p
		}
		p += 2
	}
	return sieve
}

func getDivisorsFromSieve(sieve []uint64, num uint64)map[uint64]bool{
	divisors := map[uint64]bool{}
	for num > 1{
		divisors[sieve[num]] = true
		num /= sieve[num]
	}
	return divisors
}

func main(){
	var k, n int
	fmt.Scanf("%d %d", &n, &k)
//	n := 644
//	k := 3
    m := uint64(n + k)
    sieve := divisorSieve(m)
    for i := uint64(2); i <= uint64(n); i++{
		if len(getDivisorsFromSieve(sieve, i)) == k{
			count := 1
			for j := 1; j < k; j++{
				if len(getDivisorsFromSieve(sieve, i + uint64(j))) != k{
					break
				}
				count++
			}
			if count == k{
				fmt.Println(i)
			}
		}
	}
}
