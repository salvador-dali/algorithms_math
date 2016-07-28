/**
 this is pentagonal number theorem:
 http://en.wikipedia.org/wiki/Pentagonal_number_theorem
 */

package main
import (
	"fmt"
)

func pentagonal(k int64)int64{
	return k * (3 * k - 1) / 2
}

func partition(n int64, partitions []int64)int64{
	res := int64(0)
	for i := int64(1); ; i++{
		num := pentagonal(i)
		if num > n{ break }
		if i % 2 == 1{
			res += partitions[n - num]
		} else {
			res -= partitions[n - num]
		}

		num = pentagonal(-i)
		if num > n{ break }
		if i % 2 == 1{
			res += partitions[n - num]
		} else {
			res -= partitions[n - num]
		}

	}

	tmp := res % 1000000007
	if tmp < 0{
		tmp += 1000000007
	}

	return tmp
}

func main(){
	result := []int64{1, 1, 2, 3}
	for i := int64(4); i <= 1000000; i++{
		res := partition(i, result)
		result = append(result, res)
	}
	fmt.Println(result[55374])
	fmt.Println(-66 % 7)
}
