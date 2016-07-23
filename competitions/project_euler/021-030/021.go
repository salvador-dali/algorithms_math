/**
 first of all use theta divisor function to calculate the sum of divisors of a number. If to subtract this number
 will be sum of all proper divisors
 When computing theta divisors, we need a factorization of a number. It is inefficient to find it for each number
 separately. Use a divisors sieve to find factorization for all numbers.

 Now we have the sum of all proper divisors for all the numbers. Store them in the hash and for every pair try to find
 a hash that has this number as a pair
 */

package main
import (
	"fmt"
	"math"
)

func getDivisors(sieve []uint64, num uint64)[]uint64{
	divisors := []uint64{}
	for num > 1{
		divisors = append(divisors, sieve[num])
		num /= sieve[num]
	}
	return divisors
}

func divisorSieve(n uint64) []uint64{
	sieve := []uint64{}
	for i:= uint64(0); i < n + 1; i++{
		if i % 2 == 0{
			sieve = append(sieve, 2)
		} else {
			sieve = append(sieve, 0)
		}

	}
	sieve[0], sieve[1] = 0, 0

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

func DivisorsFunc(factors []uint64, x1 int)uint64{
	dict := map[uint64]uint64{}
	x := float64(x1)
	var res uint64 = 1
	for _, v := range factors{
		dict[v] += 1
	}
	for p, a := range dict{
		res *= uint64((math.Pow(float64(p), (float64(a) + float64(1)) * x) - 1) / (math.Pow(float64(p), x) - 1))
	}
	return res
}

func amicable(n uint64)[]uint64{
	sieve := divisorSieve(n)
	dict := map[uint64]uint64{}
	for i := uint64(2); i < n; i++{
		factors := getDivisors(sieve, i)
		a := DivisorsFunc(factors, 1) - uint64(i)
		dict[i] = a
	}

	all := []uint64{}
	for i:= uint64(2); i < n; i++{
		if i == dict[dict[i]] && i != dict[i]{
			all = append(all, i)
		}
	}
	return all
}

func main(){
	nums := amicable(uint64(100000))
	var T, n int
	fmt.Scanf("%d", &T)
	for T > 0{
		T--
		fmt.Scanf("%d", &n)
		var sum uint64 = 0
		for _, v := range nums{
			if v < uint64(n){
				sum += v
			} else {
				break
			}
		}
        fmt.Println(sum)
	}
}

