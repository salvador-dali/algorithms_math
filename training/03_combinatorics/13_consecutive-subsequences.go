/**
https://www.hackerrank.com/challenges/consecutive-subsequences/
having an array of numbers [a1, a2, .., an] and some divisor k it is easy to create another
accumulative array [a1, a1 + a2, a1 + a2 + a3, ...]. Now take modulo k of all the elements.

Let you get the array [e1, e2, ... e3, e2, e2]. It is clear that the sum of original elements between
all e2-s will be divisible by k. So you can calculate the total number of each individual elements.
Now how many possible ways to connect them (n - 1) * n / 2.
Taking special care of 0 in both arrays you get O(n) solution.
 */

package main
import (
	"fmt"
	"bufio"
	"os"
	"strings"
)

func calculate(arr []int, k int) int{
	m := map[int]int{}
	zero_num, prev, total := 0, 0, 0
	for i := 0; i < len(arr); i++ {
		prev = (arr[i] + prev) % k
		m[prev]++
		if arr[i] == 0 {
			zero_num++
		}
	}

	for _, v := range m {
		total += v * (v - 1) / 2
	}

	return total - zero_num + m[0]
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
		fmt.Println(calculate(arr, tmp[1]))
    }
}
