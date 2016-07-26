/**
 generate all numbers on 3 half-diagonals (4-th one always square of some number)
 the for each number check primality with rabin-miller test
 */
package main
import (
	"fmt"
	"math/big"
)

func generate(ratio float64){
	n1 := int64(3)
	n2 := int64(5)
	n3 := int64(7)
	primesNum := 3
	total := 5
	test := 100 * float64(3) / float64(total)
	i := int64(1)
	for test >= ratio{
		tmp := 2 + i * 8
		n1 += tmp
		n2 += 2 + tmp
		n3 += 4 + tmp

		n1_ := big.NewInt(n1)
		n2_ := big.NewInt(n2)
		n3_ := big.NewInt(n3)

		if n1_.ProbablyPrime(2){ primesNum++ }
		if n2_.ProbablyPrime(2){ primesNum++ }
		if n3_.ProbablyPrime(2){ primesNum++ }
		total += 4

		i++
		test = float64(primesNum) / float64(total) * 100
	}
	fmt.Println(i * 2 + 1)
}

func main(){
    n := 0
    fmt.Scanf("%d", &n)
    generate(float64(n))
}
