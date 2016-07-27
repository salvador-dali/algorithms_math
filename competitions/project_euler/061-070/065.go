// http://www.mathblog.dk/project-euler-65-numerator-continued-fraction-e/
package main
import (
	"fmt"
	"math/big"
)

func calc(num int64)int{
	prev := big.NewInt(1)
	curr := big.NewInt(2)
	for i := int64(2); i <= num; i++{
		tmp := prev
		value := big.NewInt(1)
		if i % 3 == 0{
			value = big.NewInt(2 * i / 3)
		}
		prev = curr
		tmp1 := new(big.Int).Mul(value, prev)
		curr = new(big.Int).Add(tmp1, tmp)
	}
	s := curr.String()
	sum := 0

	for i := 0; i < len(s); i++{
		sum += int(s[i] - 48)
	}
	return sum
}

func main(){
	var n int64
	fmt.Scanf("%d", &n)
	fmt.Println(calc(n))
}
