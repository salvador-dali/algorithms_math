/**
 using the formula for sum(i) and sum(i^2) after subtraction the result is obvious
 */

package main
import (
	"fmt"
)

func diff(n uint64) uint64{
	return n * (n + 1) * (n - 1) * (3 * n + 2) / 12
}

func main(){
	var T, n int
	fmt.Scanf("%d", &T)
	for T > 0{
		T--
		fmt.Scanf("%d", &n)
		fmt.Println(diff(uint64(n)))
	}
}
