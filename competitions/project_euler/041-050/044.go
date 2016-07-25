/**
 for every number i, checks whether i - k and i + k are pentagonal,
 using O(1) is pentagonal check
 */

package main

import (
	"fmt"
	"math"
)

func isPentagonal(n uint64)bool{
	x := (math.Sqrt(float64(24 * n + 1)) + 1) / 6
	return x == math.Floor(x)
}

func P_n(n int)uint64{
	return uint64(n) * (3 * uint64(n) - 1) / 2
}

func main(){
	var n, k int
    fmt.Scanf("%d %d", &n, &k)
	for i:=1; i<n; i++{
		P1 := P_n(i)
		if i - k >= 1{
			P2 := P_n(i - k)
			if isPentagonal(P1 - P2){
				fmt.Println(P1)
			} else if isPentagonal(P1 + P2){
				fmt.Println(P1)
			}
		}
	}
}
