/**
 just a pascal triangle which handles big numbers in a slightly different way.
 All numbers bigger than maximum possible K, it substitutes with a slightly bigger number
 to be sure that we do not get stackoverflow
 */

package main
import (
    "fmt"
    "bufio"
    "os"
    "strconv"
    "strings"
)

func readArr()[]uint64{
    arr := []uint64{}
    scanner := bufio.NewScanner(os.Stdin)
    scanner.Scan()
    for _, v := range(strings.Fields(scanner.Text())) {
        num, _ := strconv.Atoi(v)
        arr = append(arr, uint64(num))
    }
    return arr
}

func main(){
    arr := readArr()
	N := int(arr[0])
	K := arr[1]
	MAX, total := uint64(2000000000000000000), 0
	pascal_prev := []uint64{1, 1}
	for N > 1{
		N--
		pascal_curr := []uint64{1}
		for i := 0; i < len(pascal_prev) - 1; i++{
			nextNum := pascal_prev[i] + pascal_prev[i + 1]
			if nextNum > MAX{
				nextNum = MAX
			}
			if nextNum > K{
				total++
			}
			pascal_curr = append(pascal_curr, nextNum)
		}
		pascal_curr = append(pascal_curr, 1)
		pascal_prev = pascal_curr
	}
	fmt.Println(total)
}
