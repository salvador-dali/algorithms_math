/**
 DP solution. Calculate the next possible number of coin changes.
 let's assume that you can give 0 in one possible way.
 It is obvious that having only one coin (1p) you can give any number only in one way

 This is your result.
 Lets look how you can give 1 having (1, 2p). You can do it only 1 way.
 2p you can give result[2 - 1] = 1  and result[2-2] = 1, so in two ways.
 Lets look how you can give

 x with coins (y1, y2, ..., y_n).
 it is result[x - y1] + result[x - y2] + ... + result[x - y_n]
 */

package main

import (
	"fmt"
)

func solution(coins []int, n int)[]int{
	MOD := 1000000007
	result := make([]int, n + 1)
	result[0] = 1

    for _, coin := range(coins){
		for i:=coin; i<=n; i++{
            result[i] = (result[i] + result[i - coin]) % MOD
		}
	}
	return result
}

func main(){
    var T, n int
    fmt.Scanf("%d", &T)
	res := solution([]int{1, 2, 5, 10, 20, 50, 100, 200}, 100005)
    for T > 0{
        T--
        fmt.Scanf("%d", &n)
        fmt.Println(res[n])
    }
}

