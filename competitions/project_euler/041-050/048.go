/**
straight forward summation with a quick power calculation in log(n)
 */
package main

import (
	"fmt"
    "math/big"
)

func main(){
	var n int
	fmt.Scanf("%d", &n)
	res := int64(0)
    m := int64(10000000000)
	for i:=1; i<=n; i++{
        z := new(big.Int).Exp(big.NewInt(int64(i)), big.NewInt(int64(i)), big.NewInt(m))
        res = (res + z.Int64()) % m
	}
	fmt.Println(res)
}
