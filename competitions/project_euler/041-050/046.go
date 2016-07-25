/**
 get all the primes, then for each of the testing numbers
 go through all primes (till the prime is smaller then number) and check that
 p + 2 * i^2 = v
 */

package main
import (
	"fmt"
	"math"
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

func goldBach(primes []uint64, n uint64)int{
	count := 0
	for _, p := range primes{
		if p >= n{
			break
		}
		x := math.Sqrt(float64(n - p) / 2)
		if x == math.Floor(x){
			count++
		}
	}
	return count
}

func main(){
    var T, n uint64
	primes := sieveEratosthenes(uint64(500000))
    fmt.Scanf("%d", &T)
    for T > 0 {
        T--
        fmt.Scanf("%d", &n)
        fmt.Println(goldBach(primes, n))
    }
}
