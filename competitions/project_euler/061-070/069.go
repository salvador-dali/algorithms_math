/**
 euler totient is equal to $n \cdot \prod_{all \ primes} (1 - \frac{1}{p})$
 so $n / \varphi (n)$ will be equal $\prod_{all \ primes} \frac{p}{p-1}$

 We need to find a maximum for this one.
 Definitely the maximum will be if we will take a lot of primes

 So we need to find first couple of distinct primes, and multiply them together
 to get the value of the number.

 Keep in mind that 3 * 5 and 3 * 3 * 5 * 5 * 5 will have the same n/phi(n)
 but the first one is smaller, so that is exactly what we need
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


func main(){
	primes := sieveEratosthenes(uint64(70))
	res := uint64(1)
	results := []uint64{1}
	for _, v := range(primes){
		res *= v
		results = append(results, res)
	}
	
	var T int
    var n uint64
    fmt.Scanf("%d", &T)
    for T > 0{
        T--
        fmt.Scanf("%d", &n)
        for i:=0; true; i++{
            if results[i] >= n{
                fmt.Println(results[i - 1])
                break
            }
        }
    }
}
