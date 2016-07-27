/**
 http://www.mathblog.dk/project-euler-70-investigate-values-of-n-for-which-%CF%86n-is-a-permutation-of-n/
 with the only difference that we are adding squares of primes as well.
 */

package main
import (
	"fmt"
	"math"
	"sort"
)

func isPermutation(n, m int)bool{
	if math.Floor(math.Log10(float64(n))) != math.Floor(math.Log10(float64(m))){
		return false
	}

	arr1 := [10]uint8{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
	arr2 := [10]uint8{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
	for n > 0{
		arr1[uint8(n % 10)]++
		n /= 10
	}

	for m > 0{
		arr2[uint8(m % 10)]++
		m /= 10
	}

	return arr1 == arr2
}

func sieveEratosthenes(n int)[]int{
	c := make([]bool, n)
	c[1] = true
	var p int = 2
	var i, p2 int

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

	primes := []int{}
	for i = 1; i < n; i++{
		if c[i] == false {
			primes = append(primes, i)
		}
	}
	return primes
}

func main(){
	var n int
  	fmt.Scanf("%d", &n)

	minimum, result := float64(n), 1
	primes := sieveEratosthenes(n)
	squares := []int{}
	squaresMap := map[int]int{}
	for i := 0; i < len(primes); i++{
		square := primes[i] * primes[i]
		if square < n{
			squares = append(squares, square)
			squaresMap[square] = primes[i]
		}
	}

	all := append(primes, squares...)
	sort.Ints(all)

	for i := 0; i < len(all); i++{
		for j := i; j < len(all); j++{
			mul := all[i] * all[j]
			if mul >= n{ break }

			n1, n2 := all[i] - 1, all[j] - 1
			if squaresMap[all[i]] != 0{
				n1 = squaresMap[all[i]] * (squaresMap[all[i]] - 1)
			}

			if squaresMap[all[j]] != 0{
				n2 = squaresMap[all[j]] * (squaresMap[all[j]] - 1)
			}

			phi := n1 * n2
			if isPermutation(phi, mul){
				attempt := float64(mul) / float64(phi)
				if attempt < minimum{
					minimum = attempt
					result = mul
				}
			}


		}
	}

	fmt.Println(result)
}
