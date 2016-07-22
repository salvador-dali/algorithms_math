/**
 important thing is to notice the property of a divisor function
 if n = a * b and a is a coprime to b, then div(n) = div(a) * div(b)

 for triangular number multiples are coprimes
 */

package main
import (
	"fmt"
)

func getDivisorsNum(n uint64)int{
	/**
	 O(n^0.5)
     get the number of divisors of a number. Counts 1 and n

     important property of a divisor function
	 if n = a * b and a is a coprime to b, then div(n) = div(a) * div(b)

	 read also this: http://en.wikipedia.org/wiki/Divisor_function
	 and implement getDivisors from factorization

	 */
	var num int = 0
	var i uint64 = 1
	for i = 1; i * i < n; i++{
		if n % i == 0{
			num += 2
		}
	}
	if i * i == n{
		num += 1
	}
	return num
}

func getDivisorsOfTriangular(n int)int{
	if n % 2 == 0{
		return getDivisorsNum(uint64(n / 2)) * getDivisorsNum(uint64(n + 1))
	} else {
		return getDivisorsNum(uint64(n)) * getDivisorsNum(uint64(n + 1) / 2)
	}
}

func main(){
	divisors := []int {}
	for i := 1; i < 50000; i++{
		// can save only biggest so far and position when it has occurred
		// and after that use binary search to find it for each test case
		// but because the number of test cases is small - ignore it
		divisors = append(divisors, getDivisorsOfTriangular(i))
	}

	var T, n int
	fmt.Scanf("%d", &T)
	for T > 0{
		T--
		fmt.Scanf("%d", &n)
		for i := 0; i< len(divisors); i++{
			if divisors[i] > n{
				fmt.Println((i + 1) * (i + 2) / 2)
                break
			}
		}
	}
}
