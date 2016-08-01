/**
https://www.hackerrank.com/challenges/number-list
create a binary array where all elements bigger than K are 1 otherwise 0
Total number of subarrays is n(n+1)/2. Now the subarrays that have no zeros can be
calculated by checking consecutive 0 and counting it's number of subarrays
 */

package main
import (
	"fmt"
	"bufio"
	"strconv"
	"strings"
	"os"
)

func helper(n int) uint64 {
	return uint64(n) * uint64(n + 1) / uint64(2)
}

func calc(arr []int, k int) uint64{
	total, n := helper(len(arr)), 0
	for i := 0; i < len(arr); i++ {
		if arr[i] > k {
			if n > 0 {
				total -= helper(n)
				n = 0
			}
		} else {
			n++
		}
	}
	if n > 0 {
		total -= helper(n)
	}

	return total
}

func main(){
	T, reader := 0, bufio.NewReader(os.Stdin)
    fmt.Scanf("%d", &T)
    for T > 0{
        T--
		text, _ := reader.ReadString('\n')
		tmp := []int{}
		for _, v := range (strings.Fields(text)) {
			num, _ := strconv.Atoi(v)
			tmp = append(tmp, num)
		}
		text, _ = reader.ReadString('\n')
		arr := []int{}
		for _, v := range (strings.Fields(text)) {
			num, _ := strconv.Atoi(v)
			arr = append(arr, num)
		}
        fmt.Println(calc(arr, tmp[1]))
    }
}
