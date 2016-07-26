package main
import (
	"fmt"
	"time"
)

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

func generateCombinations(n, m int, emit func([]int)) {
    s := make([]int, m)
    last := m - 1
    var rc func(int, int)
    rc = func(i, next int) {
        for j := next; j < n; j++ {
            s[i] = j
            if i == last {
                emit(s)
            } else {
                rc(i+1, j+1)
            }
        }
        return
    }
    rc(0, 0)
}


func main(){
	start := time.Now()

	N, K := 4, 2
	digits := []int{1, 10, 100, 1000, 10000, 100000, 1000000, 10000000}

	primes := []int{}
	for k, v := range(sieve(10000000)){
		if v && (k > digits[N - 1]) && (k < digits[N]){
			primes = append(primes, k)
		}
	}
	fmt.Println(len(primes))

	generateCombinations(N, K, func(c []int) {
        fmt.Println(c)
    })

	elapsed := time.Since(start)
	fmt.Println(elapsed)

}
