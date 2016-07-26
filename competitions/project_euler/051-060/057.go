/**
 let starting point
 1 + 1/2 = x/y.
 then next step will be 1 + 1/(1 + x/y), which means that (2y + x)/(x + y)

 so we have iterations:

 x_1 = 2 * y_0 + x_0
 y_1 = y_0 + x_0
 */
package main
import (
	"fmt"
	"math/big"
)

func main(){
	x, y := big.NewInt(3), big.NewInt(2)

	n := 14
	fmt.Scanf("%d", &n)
	for i := 1; i <= n; i++{
		tmp1, tmp2 := new(big.Int), new(big.Int)
		tmp1.Add(x, y)
		tmp2.Add(tmp1, y)
		x, y = tmp2, tmp1
		if len(x.String()) > len(y.String()){
			if i <= n{
				fmt.Println(i)
			}
		}
	}
}
