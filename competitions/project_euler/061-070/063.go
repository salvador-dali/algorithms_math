/**
 few things here to keep in mind
 numbers will not be able to fit in uint64, so big int are needed
 a^n has Floor(n * log10(i)) + 1 digits
 */

package main
import (
	"fmt"
	"math"
	"math/big"
)

func powBig(a, n int) *big.Int{
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

func main(){
    var n int
	fmt.Scanf("%d", &n)
	for i := 1; true; i++{
		length := int(math.Floor(float64(n) * math.Log10(float64(i)))) + 1
		if length == n{
			fmt.Println(powBig(i, n))
		} else if length > n {
			break
		}
	}
}
