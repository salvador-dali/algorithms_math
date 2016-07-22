/**
 straightforward implementation of log time a^n calculation using bigInt
 */

package main

import (
	"fmt"
	"math/big"
)

func pow(a, n int) *big.Int{
	tmp := big.NewInt(int64(a))
	res := big.NewInt(1)
	for n > 0 {
		temp := new(big.Int)
		if n % 2 == 1 {
			temp.Mul(res, tmp)
			res = temp
		}
		temp = new(big.Int)
		temp.Mul(tmp, tmp)
		tmp = temp
		n /= 2
	}
    return res
}

func sum(n int){
	var s string = pow(2, n).String()
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
