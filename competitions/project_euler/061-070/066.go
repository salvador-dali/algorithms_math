// http://oeis.org/A033316
// http://en.wikipedia.org/wiki/Pell%27s_equation
// this is an example of how to find a solution.
//	working with Big int sucks in golang, so in project_euler I just submitted a list of OEIS

package main
import (
	"fmt"
	"math"
)

func fractionRepresentation(n int)(int, []int){
	s := int(math.Sqrt(float64(n)))
	if s * s == n{
		return -1, []int{}
	}

	d, m, a := 1, 0, s
	period := []int{a}
	for a != 2 * s{
		m = d * a - m
		d = (n - m * m) / d
		a = (s + m) / d
		period = append(period, a)
	}
	return period[0], period[1:]
}

func calculateContinuousFraction(fraction []int, k int)(int, int){
	numerator, denominator := 1, 0
	for i := k; i >=0; i--{
		numerator, denominator = fraction[i] * numerator + denominator, numerator
	}
	return numerator, denominator
}

func solvePell(n int)(int, int){
	first, period := fractionRepresentation(n)
	if first == -1 {
		return -1, -1
	}

	list := append([]int{first}, period...)
	for i := 0; true; i++{
		if i >= len(list){
			list = append(list, period...)
		}

		numerator, denominator := calculateContinuousFraction(list, i)
		if numerator * numerator - n * denominator * denominator == 1 {
			return numerator, denominator
		}
	}
	return -1, -1
}

func main(){
	n := 3
	fmt.Scanf("%d", &n)
	fmt.Println(solvePell(n))
}
