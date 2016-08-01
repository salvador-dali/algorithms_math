/**
https://www.hackerrank.com/challenges/game-of-throne-ii
to be an anagram a word should be symmetrical around the center. I mean that it will have at most
one odd number of chars and all other chars should be even. Divide all the numbers by two to get
the number of each chars on one side. To count the number of rearrangements you need to calculate
multinomial coefficient.
 */
package main
import (
	"fmt"
)

func extractNumbers (s string) []int {
	lookup := map[byte] int {}
	for i := 0; i < len(s); i++ {
		lookup[s[i]]++
	}
	
	found_odd := false

	arr := []int{}
	for _, v := range lookup {
		if v % 2 == 1 {
			if found_odd {
				return []int{0}
			}
			found_odd = true
		}
		if v > 1 {
			arr = append(arr, v / 2)
		}
	}

	return arr
}

func powMod(base, exponent, modulo int)int{
	res := 1
	base %= modulo
	for exponent > 0{
		if exponent % 2 == 1{
			res = (res * base) % modulo
		}
		exponent /= 2
		base = (base * base) % modulo
	}
	return res
}

func multinomialModulo(arr []int) int{
	s, mod := 0, 1000000007
	for _, v := range arr {
		s += v
	}

	factor_mod := make([]int, s + 1)
	factor_mod[0] = 1
	for i := 1; i <= s; i++ {
		factor_mod[i] = (factor_mod[i - 1] * i) % mod
	}

	res := factor_mod[s]
	for _, v := range arr {
		res = (res * powMod(factor_mod[v], mod - 2, mod)) % mod
	}
	return res
}

func main(){
    var s string
	fmt.Scanf("%s", &s)
	arr := extractNumbers(s)
    fmt.Println(multinomialModulo(arr))
}
