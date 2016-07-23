/**
 To get the n-th permutation you have to convert a n into a factorial number system
 and prepend it with 0 to the length of permutation alphabet.
 http://en.wikipedia.org/wiki/Factorial_number_system

 having an alphabet and an array of digits that represent a factorial number system
 a permutation is generated as taking the alphabet[digit_arr[0]]
 then removing that element from alphabet, then alphabet[digit_arr[1]] and so on
 */

package main
import (
	"fmt"
)

func toFactorial(n uint64)[]uint8{
	digits := []uint8{}
	for i:=uint64(1); n > 0; i++{
		digits = append([]uint8{uint8(n % i)}, digits...)
		n /= i
	}
	return digits
}
func getPermutation(elements []string, n uint64){
	res := toFactorial(n - 1)
	for i := len(res); i < len(elements); i++{
		res = append([]uint8{uint8(0)}, res...)
	}
	for _, v := range res{
		fmt.Print(elements[int(v)])
		elements = append(elements[:int(v)], elements[int(v) + 1:]...)
	}
	fmt.Println("")
}

func main(){
    var T, n uint64
    fmt.Scanf("%d", &T)
    for T > 0{
        T--
        fmt.Scanf("%d", &n)
        elements := []string{"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"}
	    getPermutation(elements, n)
    }
}
