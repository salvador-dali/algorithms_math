/**
here is my implementation
http://stackoverflow.com/a/30317680/1090562
Calculates correctly but takes too much time
 */
package main

import (
	"fmt"
	"math"
	"math/big"
)

func square(n int64, precision int64)int{
	limit	:= new(big.Int).Exp(big.NewInt(10), big.NewInt(precision + 1), nil)
	a		:= big.NewInt(5 * n)
	b		:= big.NewInt(5)
	five	:= big.NewInt(5)
	ten		:= big.NewInt(10)
	hundred	:= big.NewInt(100)

	for b.Cmp(limit) < 0{
		if a.Cmp(b) < 0{
			a.Mul(a, hundred)
			tmp := new(big.Int).Div(b, ten)
			b.Add(tmp.Mul(tmp, hundred), five)
		} else {
			a.Sub(a, b)
			b.Add(b, ten)
		}
	}
	b.Div(b, hundred)
	sum := 0
	for _, v := range(b.String()){
		sum += int(v - 48)
	}

	return sum
}

func main(){
	n := 100
	sum := 0
	for i := 2; i <= n; i++{
		x := math.Sqrt(float64(i))
		if x != math.Floor(x){
			fmt.Println(i, square(int64(i), 100))
			sum += square(int64(i), 100)
		}
	}
	fmt.Println(sum)
}
