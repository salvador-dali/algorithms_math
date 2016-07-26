package main
import (
	"fmt"
)

func concatNum(n1, n2 uint64)(uint64, uint64){
	num1Length := uint64(1)
	num2Length := uint64(1)
	n1_tmp := n1
	n2_tmp := n2

	for n1_tmp > 0{
		n1_tmp /= 10
		num1Length *= 10
	}

	for n2_tmp > 0{
		n2_tmp /= 10
		num2Length *= 10
	}

	return n1 * num2Length + n2, n2 * num1Length + n1
}

func sieveEratosthenes(n uint64)[]uint64{
	c := make([]bool, n)
	c[1] = true
	var p uint64 = 2
	var i, p2 uint64

	for {
		p2 = p * p
		if p2 >= n {
			break
		}
		for i = p2; i < n; i += p {
			c[i] = true
		}
		for {
			p++
			if !c[p] {
				break
			}
		}
	}

	primes := []uint64{}
	for i = 1; i < n; i++{
		if c[i] == false {
			primes = append(primes, i)
		}
	}
	return primes
}

func nicePrint(hash map[uint64][]uint64){
	for k, v := range(hash){
		fmt.Println(k, v)
	}
}

func main(){
	n := uint64(40)
	listOfPrimesBig := sieveEratosthenes(n * n)
	setOfPrimes := map[uint64]bool{}
	listOfPrimes:= []uint64{}

	for _, v := range(listOfPrimesBig){
		setOfPrimes[v] = true
		if v < n{
			listOfPrimes = append(listOfPrimes, v)
		}
	}

	output := map[uint64][]uint64{}
	for i := 0; i < len(listOfPrimes); i++{
		for j := i + 1; j < len(listOfPrimes); j++{
			p1 := listOfPrimes[i]
			p2 := listOfPrimes[j]
			left, right := concatNum(p1, p2)

			if setOfPrimes[left] && setOfPrimes[right] {
				output[p1] = append(output[p1], p2)
				output[p2] = append(output[p2], p1)
			}
		}
	}

	nicePrint(output)
}


