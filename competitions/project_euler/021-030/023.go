/**
 factorize all numbers from 2 to maximum
 then for each of the number find sum of divisors with the formula
 and filter only abundant ones and store them in the dictionary
 which will be used to find two numbers which sums up to a certain number
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

func isSum(list map[uint64]int, n int)bool{
	for k, _ := range list{
		if list[uint64(n) - k] > 0{
			return true
		}
	}
	return false
}

func main(){
	n := uint64(28126)
	sieve := divisorSieve(n)
	abundant := map[uint64]int{}
	for i := uint64(3); i <= n; i++{
		if i < DivisorsFunc(getDivisors(sieve, i), 1) - i {
			abundant[i] = 1
		}
	}

	var T, m int
	fmt.Scanf("%d", &T)
	for T > 0{
		T--
		fmt.Scanf("%d", &m)
        if m > 28124 {
            fmt.Println("YES")
        } else {
            if isSum(abundant, m){
		  	   fmt.Println("YES")
		    } else {
			   fmt.Println("NO")
		    }
        }
	}

}
