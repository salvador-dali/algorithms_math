/**
https://www.hackerrank.com/challenges/coinage
You have to found all the tuples (a, b, c, d) that every number is positive and

a + 2b + 5c + 10d = price

Now decrease it to 3 loops and you will pass the tests
 */
package main
import (
	"fmt"
)

func coinage(num_a, num_b, num_c, num_d, price int) int {
	count, sum := 0, 0
	for b := 0; b <= num_b; b++ {
		sum = 2 * b
		if sum > price { break }
		for c := 0; c <= num_c; c++ {
			sum = 2 * b + 5 * c
			if sum > price { break }
			for d := 0; d <= num_d; d++ {
				sum = 2 * b + 5 * c + 10 * d
				if sum > price { break }

				if num_a + sum >= price {
					count++
				}
			}
		}
	}
	return count
}

func main(){
    T, a, b, c, d, price := 0, 0, 0, 0, 0, 0
    fmt.Scanf("%d", &T)
    for i:=0; i < T; i++ {
        fmt.Scanf("%d %d %d %d %d", &price, &a, &b, &c, &d)
        res := coinage(a, b, c, d, price)
        fmt.Println(res)
    }
}
