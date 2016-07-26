package main
import (
	"fmt"
	"time"
	"sort"
)

func isPrime(n int, primes []int, is_prime[]bool)bool{
	if n < len(is_prime){
		return is_prime[n]
	}
	
	for i := 0; i < len(primes); i++{
		p := primes[i]
		if p * p > n{
			return true
		}
		if n % primes[i] == 0{
			return false
		}
	}
	return true
}

func sieve(n int)[]bool{
	is_primes := make([]bool, n + 1)
	for i := 2; i <= n; i++{
		is_primes[i] = true
	}

	for i := 2; i * i <= n; i++{
		if is_primes[i]{
			for j := i * i; j <= n; j += i{
				is_primes[j] = false
			}
		}
	}
	return is_primes
}

func concatNum(n1, n2 int)(int, int){
	num1Length, num2Length, n1_tmp, n2_tmp := 1, 1, n1, n2

	for n1_tmp > 0{
		n1_tmp /= 10
		num1Length *= 10
	}

	for n2_tmp > 0{
		n2_tmp /= 10
		num2Length *= 10
	}

	return n1 * num2Length + n2, n2 * num1Length + n1
}

func test_3(connections map[int][]int){
	keys := []int{}
	s := 0
	for k, v := range(connections){
		keys = append(keys, k)
		if len(v) >= 5{
			s++
		}
	}
	sort.Ints(keys)
	fmt.Println(len(keys))
	fmt.Println(s)
	for i := 0; i < len(keys); i++{
		for j := i + 1; j < len(keys); j++{
			for k := j + 1; k < len(keys); k++{
//				fmt.Println(connections[keys[i]], connections[keys[j]], connections[keys[k]])
//				fmt.Println(i, j, k)
			}
		}
	}
}

func calculations(n int){
	is_prime, primes, primesAll := sieve(100000000), []int{}, []int{} // 100000000
	for k, v := range(is_prime){
		if v{
			if k == 5 || k == 2 {

			} else if k < n {
				primes = append(primes, k)
			}
			primesAll = append(primesAll, k)
		}
	}

	connections := map[int][]int{}
	for i := 0; i < len(primes); i++{
		for j := i + 1; j < len(primes); j++{
			p1, p2 := primes[i], primes[j]
			left, right := concatNum(p1, p2)
			if isPrime(right, primesAll, is_prime) && isPrime(left, primesAll, is_prime){
				connections[p1] = append(connections[p1], p2)
				connections[p2] = append(connections[p2], p1)
			}
		}
	}

	test_3(connections)
}



func main(){
	start := time.Now()
	calculations(20000)
	elapsed := time.Since(start)
	fmt.Println(elapsed)
}

