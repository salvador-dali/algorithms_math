/**
 using an algorithm for generating pythagorean triples
 http://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples
 one can find a formula to get all the perimeters of triples less then
 maxPerimenter. it will be 2 * k * m (m + n), where m is the bigger size and
 m and n are coprime.

 generate will return key-value, where key is a perimeter and value is the number of triangles with
 such perimeter

 After this return only one, which have value 1. Then create an array where value is the result.
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
	n := 5000005
	result := make([]int, n)

	onlyOnce := []int{}
	for k, v := range(generate(n)){
		if v == 1{
			onlyOnce = append(onlyOnce, k)
		}
	}
	sort.Ints(onlyOnce)

	prevIndex := 0
	prevValue := 0
	for _, v := range(onlyOnce){
		for i:=prevIndex; i<=v; i++{
			result[i] = prevValue
		}
		prevValue++
		prevIndex = v
	}

	for i:=prevIndex; i<n; i++{
		result[i] = prevValue
	}

	var T, m int
    fmt.Scanf("%d", &T)
	for T > 0{
        T--
		fmt.Scanf("%d", &m)
		fmt.Println(result[m])
	}
}
