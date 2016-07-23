/*
 This did not really work and fails on some cases (tiny part)
 after writing down the square, one can see that the four diagonal have:
 1, 3, 13, 31, 57, ...
 1, 5, 17, 37, 65, ...
 1, 7, 21, 43, ...
 1, 9, 25, 49, ...

 ignoring 1 (we will add it later) and checking the difference between
 the numbers, one can see that it is a + 8, a + 2*8,...
 and for the first numbers it is the sum
 3 + 2i + 4i(i+1)
 5 + 4i + 4i(i+1)
 7 + 6i + 4i(i+1)
 9 + 8i + 4i(i+1)

 summing up:
 4*(4i^2 + 9i + 6) where i from 0 to n
 closed form is (n+1)*(8*n*n+31*n+36) * 2 / 3

 important thing is that n here is N / 2 - 1


 if n = 3k, then
 2 * (3k + 1) * (24k^2 + 31k + 12) = 144k^3 + 234k^2 + 134k + 24

 if n = 3k + 1
 2 * (3k + 2) * (24k^2 + 47k + 25) = 144k^3 + 378k^2 + 338k + 100

 if n = 3k + 2
 2 * (k + 1) * (72k^2 + 189k + 130)= 144k^3 + 522k^2 + 638k + 260
 */
package main
import (
	"fmt"
)

func k_n(k uint64, mod uint64, n int) uint64{
	res := uint64(1)
	for i := 0; i < n; i++{
		res = (res * (k % mod)) % mod
	}
	return res
}

func sum(x uint64) uint64{
	if x == 1{
        return 1
    }
	MOD := uint64(1000000007)
	n := x / 2 - 1
	mod := n % 3
	k := n / 3
	switch {
	case mod == 0:
		return ((144 * k_n(k, MOD, 3)) % MOD + (234 * k_n(k, MOD, 2)) % MOD + (134 * (k % MOD)) % MOD + 24 + 1) % MOD
	case mod == 1:
		return ((144 * k_n(k, MOD, 3)) % MOD + (378 * k_n(k, MOD, 2)) % MOD + (338 * (k % MOD)) % MOD + 100 + 1) % MOD
	case mod == 2:
		return ((144 * k_n(k, MOD, 3)) % MOD + (522 * k_n(k, MOD, 2)) % MOD + (638 * (k % MOD)) % MOD + 260 + 1) % MOD
	}
	return 0
}

func main(){
    var T, n uint64
    fmt.Scanf("%d", &T)
    for T > 0{
        T--
        fmt.Scanf("%d", &n)
        fmt.Println(sum(n))
    }
}
