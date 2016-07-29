package main
import (
	"fmt"
	"math"
)

func shortestDistance(a, b, c float64)float64{
	var biggest, x, y float64
	if a >= b && a >= c{
		biggest = a
		x, y = b, c
	} else if b >= a && b >= c{
		biggest = b
		x, y = a, c
	} else {
		biggest = c
		x, y = a, c
	}

	return math.Sqrt(biggest * biggest + (x + y) * (x + y))
}

func main(){
	m := 0
	fmt.Scanf("%d", &m)
	total := 0
	for a := 1; a <= m; a++{
		for b := a; b <= m; b++{
			for c := b; c <= m; c++{
				r := shortestDistance(float64(a), float64(b), float64(c))
				if r - float64(int(r)) == 0{
					total++
				}
			}
		}
	}
	fmt.Println(total)
}
