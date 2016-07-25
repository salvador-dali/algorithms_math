/*
 to check whether the number is triangular, it is enough to check if
 (sqrt(8x + 1) - 1)/2 is an integer. This integer will be a position of this number
 */
package main

import (
	"fmt"
	"math"
)

func isTriangular(n uint64)int64{
	x := (math.Sqrt(float64(8 * n + 1)) - 1) / 2
	if x == math.Floor(x){
		return int64(x)
	}
	return -1
}

func main(){
	var T, n uint64
	fmt.Scanf("%d", &T)
	for T > 0{
		T--
		fmt.Scanf("%d", &n)
		fmt.Println(isTriangular(uint64(n)))
	}

}
