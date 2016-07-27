// http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
package main
import (
	"fmt"
	"math"
)

func findPeriod(n int) int{
	s := int(math.Sqrt(float64(n)))
	if s * s == n{
		return -1
	}

	period, d, m, a := 0, 1, 0, s

	for a != 2 * s{
		m = d * a - m
		d = (n - m * m) / d
		a = (s + m) / d
		period++
	}
	return period
}

func main(){
	N := 0
	fmt.Scanf("%d", &N)
	result := 0
	for n := 2; n <= N; n++{
		period := findPeriod(n)
		if period != -1{
			if period % 2 == 1{
				result++
			}
		}
	}
	fmt.Println(result)
}
