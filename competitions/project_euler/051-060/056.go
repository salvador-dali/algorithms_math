/*
 iterate over all possible value of a and b, get their a^b,
 convert to string and sum all the digits. But do not recalculate a^b, use the fact that a^b = a^(b-1) * a
 */

package main
import (
	"fmt"
	"math/big"
)

func getSum(s string) int{
	sum := 0
	for i := 0; i < len(s); i++{
		sum += int(s[i] - 48)
	}
	return sum
}


func sumPow(n int64)int{
	max := 0
	for a := int64(2); a < n; a++{
		num := big.NewInt(1)
		for b := int64(1); b < n; b++{
			temp := new(big.Int)
			temp.Mul(num, big.NewInt(a))
			num = temp
			candidate := getSum(num.String())
			if candidate > max{
				max = candidate
			}
		}
	}
	return max
}

func main(){
	var n int64
	fmt.Scanf("%d", &n)
	fmt.Println(sumPow(n))
}
