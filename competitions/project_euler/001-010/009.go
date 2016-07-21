/**
 generate all possible triplets while storing maximum product so far and updating it if we
 found a bigger number. Then just check if the number we are looking for is in the map
 */
package main

import (
	"bufio"
	"os"
    "strconv"
	"fmt"
	"math"
)

var scanner = bufio.NewScanner(os.Stdin)

func readString() string {
	return scanner.Text()
}

func readInt() int {
	n, _ := strconv.Atoi(scanner.Text())
	return n
}

func generate()map[int]uint64{
	var a, b, res int
	var c float64
	dict := map[int]uint64{}
	for a = 1; a <= 3000; a++{
		for b = a + 1; b <= 3000; b++{
			c = math.Sqrt(float64(a * a + b * b))
			if math.Abs(c - float64(int(c))) < 0.0001{
				res = a + b + int(c)
				if res <= 3000{
					if dict[res] == 0 {
						dict[res] = uint64(a) * uint64(b) * uint64(c)
					} else {
						if dict[res] < uint64(a) * uint64(b) * uint64(c){
							dict[res] = uint64(a) * uint64(b) * uint64(c)
						}
					}
				}

			}
		}
	}
	return dict
}

func main(){
	fmt.Println(generate())
//	var dict = generate()
//	scanner.Split(bufio.ScanWords)
//	var T = readInt()
//	var n int
//	for T > 0{
//		T--
//		n = readInt()
//		if dict[n] > 0{
//			fmt.Println(dict[n])
//		} else {
//			fmt.Println("-1")
//		}
//	}
}
