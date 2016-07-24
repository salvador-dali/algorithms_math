/**
 using the algorithm that generates all the pythagorean triples
 http://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples
 one can find a formula to get all the perimeters of triples less then
 maxPerimenter. it will be 2 * k * m (m + n), where m is the bigger size and
 m and n are coprime.

 This will take sqrt(n).
 Then calculate the number of occurrences of each perimeter and use this numbers
 to calculate the best number for every value
 */

package main

import (
	"fmt"
	"sort"
)

func gcd(a, b int) int{
	var tmp int
	for b > 0 {
		tmp = a
		a = b
		b = tmp % a
	}

	return a
}

func generate(maxP int) map[int]int{
	counts := map[int]int{}
	for n := 1; n < maxP; n++{
		for m := n + 1; m < maxP; m++{
			if gcd(m, n) != 1 || (m + n) % 2 == 0{
				continue
			}
			if m * (m + n) > maxP{
				break
			}

			for k := 1; true; k++ {
				p := 2 * k * m * (m + n)
				if p > maxP{
					break
				}
				counts[p]++
			}
		}
	}

	return counts
}

func main(){
	counts := generate(5001000)
	list := []int{}
	for k, _ := range(counts){
		list = append(list, k)
	}
	sort.Ints(list)

	results := make([]int, 5001000)
	prevPosition := 0
	maximumNumber:= 0
	bestValue    := 0

	for _, v := range(list){
		for i := prevPosition; i < v; i++{
			results[i] = bestValue
		}
		prevPosition = v
		if maximumNumber < counts[v]{
			maximumNumber = counts[v]
			bestValue = v
		}
	}

    var T, n int
    fmt.Scanf("%d", &T)
    for T > 0{
        T--
        fmt.Scanf("%d", &n)
	    fmt.Println(results[n])
    }
}
