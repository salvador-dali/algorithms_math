/**
 http://en.wikipedia.org/wiki/Repeating_decimal
 use an algorithm (which we used in school to calculate 1345 / 61 on the paper)
 to calculate the repeating and non repeating part.
 Calculate the numbers for each of the value d and store them in the array

 P.S. one possible improvement is to calculate it for all prime numbers, as they would have the biggest
 value
 */
package main

import (
	"fmt"
)

func fraction(a, b uint64)int{
	a = a % b
	digits := []uint64{}
	numbersSeen := map[uint64]uint64{}
	pos := uint64(0)
	var startRepeating uint64
	var isRepeating bool = false

	for a > 0{
		start, ok := numbersSeen[a]
		if ok{
			startRepeating = start
			isRepeating = true
			break
		}
		numbersSeen[a] = pos
		a *= 10

		if a < b{
			digits = append(digits, uint64(0))
		} else {
			digits = append(digits, a / b)
			a %= b
		}
		pos++
	}

	if isRepeating{
		return len(digits) - int(startRepeating)
	} else {
		return 0
	}
}


func main(){
	biggest := []int{0}
	num := 0
	for i:=uint64(1); i<=uint64(10000); i++{
		tmp := fraction(uint64(1), i)
		if tmp > num{
			num = tmp
			biggest = append(biggest, int(i))
		} else {
			biggest = append(biggest, biggest[len(biggest) - 1])
		}

	}
    var T, n int
    fmt.Scanf("%d", &T)
    for T > 0{
        T--
        fmt.Scanf("%d", &n)
        fmt.Println(biggest[n - 1])
    }
}
