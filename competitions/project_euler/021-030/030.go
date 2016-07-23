/**
 important thing is to find out the upper bound of the numbers we need to check
 and it is 9**n * k, k can be found using testing. k = 6 is suffice
 one optimization is to store the values of pow(i, n) where i is 0-9
 */

package main
import (
	"fmt"
	"math"
)

func test(n uint64) uint64{
	var biggest = uint64(math.Pow(9, float64(n)) * 6)
	var totalSum = uint64(0)
	pows := []uint64{}
	for i := 0; i < 10; i++{
		pows = append(pows, uint64(math.Pow(float64(i), float64(n))))
	}

	for i := uint64(10); i < biggest; i++{
		sum := uint64(0)
		tmp := i
		for tmp > 0 {
			sum += pows[tmp % 10]
			tmp /= 10
		}
		if sum == i{
			//fmt.Println(i)
			totalSum += i
		}
	}
	return totalSum
}

func main(){
    var n int
    fmt.Scanf("%d", &n)
    fmt.Println(test(uint64(n)))
}
