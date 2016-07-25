/**
 generate all possible pandigital numbers. There will not be a lot of them
 f(9) + f(8) + ... + f(1) ~= half a million
 for each of these numbers check whether it is a prime
 sort all the primes.

 then for every query run a bisect
 */

package main
import (
	"fmt"
	"sort"
)

func isPrime(n uint64)bool{
	if n == 1{
		return false
	}
	if n > 2 && n % 2 == 0{
		return false
	}

	for i := uint64(3); i * i <= n; i++{
		if n % i == 0{
			return false
		}
	}
	return true
}

func permutations(arr []int)[][]int{
	var helper func([]int, int)
	res := [][]int{}

	helper = func(arr []int, n int){
        if n == 1{
			tmp := make([]int, len(arr))
			copy(tmp, arr)
			res = append(res, tmp)
		} else {
			for i := 0; i < n; i++{
				helper(arr, n - 1)
				if n % 2 == 1{
					tmp := arr[i]
					arr[i] = arr[n - 1]
					arr[n - 1] = tmp
				} else {
					tmp := arr[0]
					arr[0] = arr[n - 1]
					arr[n - 1] = tmp
				}
			}
		}
    }

	helper(arr, len(arr))
	return res
}

func num(arr []int)int{
	tmp := 1
	res := 0
	for i := len(arr); i > 0; i--{
		res += arr[i - 1] * tmp
		tmp *= 10
	}
	return res
}

func main(){
	panPrime := []int{}
	arr := []int{1}
	for i := 2; i <= 9; i++{
		arr = append(arr, i)
		for _, v := range(permutations(arr)){
			if isPrime(uint64(num(v))){
				panPrime = append(panPrime, num(v))
			}
		}
	}

	sort.Ints(panPrime)
    var T, n int
    fmt.Scanf("%d", &T)
    for T > 0{
        T--
        fmt.Scanf("%d", &n)
        if n > panPrime[len(panPrime) - 1]{
            fmt.Println(panPrime[len(panPrime) - 1])
        } else if n < panPrime[0]{
            fmt.Println(-1)
        } else {
            pos := sort.Search(len(panPrime), func(i int) bool {
	           return panPrime[i] > n
	        })
            fmt.Println(panPrime[pos - 1])
        }
    }
}
