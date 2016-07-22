/**
 just a bigint factorial formula: http://stackoverflow.com/a/19308076/1090562
 */

package main

import (
	"fmt"
	"math/big"
)

func factorial(n int) *big.Int{
	res := new(big.Int)
    res.MulRange(1, int64(n))
    return res
}

func sum(n int){
	var s string = factorial(n).String()
	var sum int = 0
	for i := 0; i < len(s); i++{
		sum += int(s[i]) - 48
	}
	fmt.Println(sum)
}

func main(){
	var T int
	fmt.Scanf("%d", &T)
	for T > 0 {
		T--
		var n int
		fmt.Scanf("%d", &n)
		sum(n)
	}
}
