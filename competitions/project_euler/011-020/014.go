/**
 brute force Collatz sequence
 with caching all the elements before the current
 when I tried to cache everything, got timeout
 */
package main
import (
	"fmt"
)

func precompute()[]int{
	cache := []int {0, 0, 1}
	for i := 3; i <= 5000010; i++{
		tmp := i
		num := 0
		for tmp >= i {
			if tmp % 2 == 0{
				tmp /= 2
			} else {
				tmp = 3 * tmp + 1
			}
			num += 1
		}
		cache = append(cache, num + cache[tmp])
	}
	return cache
}


func main(){
	list := precompute()
	biggestN := []int{0, 0, 1}
	biggest := 0
	for i := 3; i <= 5000010; i++{
		if list[i] >= biggest {
			biggest = list[i]
			biggestN = append(biggestN, i)
		} else {
			biggestN = append(biggestN, biggestN[i - 1])
		}
	}

	var T, n int
	fmt.Scanf("%d", &T)
	for T > 0{
		T--
		fmt.Scanf("%d", &n)
		fmt.Println(biggestN[n])
	}
}
