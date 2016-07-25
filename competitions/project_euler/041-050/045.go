/**
 we have two formulas for checking if the number is triangular and pentagonal in O(1)
 if the query is of the type triangular/pentagonal, we iterate over all pentagonal numbers
 and check if the same number is triangular

 if the query is pentagonal/hexagonal, we iterate over all hexagonal numbers and check if it is
 also pentagonal
 */

package main
import (
	"fmt"
	"math"
)

func isTriangular(n uint64)bool{
	x := (math.Sqrt(float64(8 * n + 1)) - 1) / 2
	return x == math.Floor(x)
}

func isPentagonal(n uint64)bool{
	x := (math.Sqrt(float64(24 * n + 1)) + 1) / 6
	return x == math.Floor(x)
}

func main(){
    var num, a, b uint64
    var n uint64 = 1
    fmt.Scanf("%d %d %d", &num, &a, &b)

    if a == 3{
        for i:= uint64(1); true; i++{
		    n = i * (3 * i - 1) / 2
            if n >= num{
                break
            }
		    if isTriangular(n){
			    fmt.Println(n)
		    }
	    }
    } else {
        for i:= uint64(1); true; i++{
		    n = i * (2 * i - 1)
            if n >= num{
                break
            }
		    if isPentagonal(n){
			    fmt.Println(n)
		    }
	    }
    }
}
