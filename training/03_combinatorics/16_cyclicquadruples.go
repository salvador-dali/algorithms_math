/**
https://www.hackerrank.com/challenges/cyclicquadruples

The number of tuples can b calculated using inclusion exclusion principle. Let us have properties
p1: x1 = x2
p2: x2 = x3
p3: x3 = x4
p4: x4 = x1

So our value will be:
All - A(p1) - A(p2) - A(p3) - A(p4)
    + A(p1 and p2) + A(p2 and p3) + A(p3 and p4) + A(p4 and p1) + A(p1 and p3) + A(p2 and p4)
    - A(p1 and p2 and p3) - A(p2 and p3 and p4) - A(p3 and p4 and p1) - A(p4 and p1 and p2)
    + A(p1 and p2 and p3 and p4)

One observation is that
A(p1 and p2 and p3) + A(p2 and p3 and p4) + A(p3 and p4 and p1) + A(p4 and p1 and p2) = 4 A(p1 and p2 and p3 and p4)
 */
package main
import (
	"fmt"
	"bufio"
	"os"
	"strings"
	"strconv"
)

var mod int = 1000000007

func intersectionPower(intervals [][]int)int{
	p1, p2 := intervals[0][0], intervals[0][1]
	for i := 1; i < len(intervals); i++ {
		if intervals[i][0] > p1 {
			p1 = intervals[i][0]
		}

		if intervals[i][1] < p2 {
			p2 = intervals[i][1]
		}
	}

	if p1 > p2 {
		return 0
	}
	return p2 - p1 + 1
}

func power(intervals [][]int)int{
	all := 1
	for i := 0; i < len(intervals); i++ {
		all = all * (intervals[i][1] - intervals[i][0] + 1) % mod
	}
	return all
}

func calculate(intervals [][]int) int{
	a0 := power(intervals)

	p1 := intersectionPower([][]int{intervals[0], intervals[1]}) * power([][]int{intervals[2], intervals[3]})
	p2 := intersectionPower([][]int{intervals[1], intervals[2]}) * power([][]int{intervals[3], intervals[0]})
	p3 := intersectionPower([][]int{intervals[2], intervals[3]}) * power([][]int{intervals[0], intervals[1]})
	p4 := intersectionPower([][]int{intervals[3], intervals[0]}) * power([][]int{intervals[1], intervals[2]})
	a1 := (p1 + p2 + p3 + p4) % mod

	p1_p2 := intersectionPower([][]int{intervals[0], intervals[1], intervals[2]}) * power([][]int{intervals[3]})
	p2_p3 := intersectionPower([][]int{intervals[1], intervals[2], intervals[3]}) * power([][]int{intervals[0]})
	p3_p4 := intersectionPower([][]int{intervals[2], intervals[3], intervals[0]}) * power([][]int{intervals[1]})
	p4_p1 := intersectionPower([][]int{intervals[3], intervals[0], intervals[1]}) * power([][]int{intervals[2]})
	p1_p3 := intersectionPower([][]int{intervals[0], intervals[1]}) * intersectionPower([][]int{intervals[2], intervals[3]})
	p2_p4 := intersectionPower([][]int{intervals[1], intervals[2]}) * intersectionPower([][]int{intervals[3], intervals[0]})
	a2 := (p1_p2 + p2_p3 + p3_p4 + p4_p1 + p1_p3 + p2_p4) % mod

	p1_p2_p3_p4 := intersectionPower(intervals)
	return ((a0 - a1 + a2 - 3 * p1_p2_p3_p4) % mod + mod) % mod
}

func main(){
	T, reader := 0, bufio.NewReader(os.Stdin)
    fmt.Scanf("%d", &T)
    for T > 0{
        T--
		text, _ := reader.ReadString('\n')
		arr := []int{}
		for _, v := range (strings.Fields(text)) {
			num, _ := strconv.Atoi(v)
			arr = append(arr, num)
		}
		fmt.Println(calculate([][]int{
			[]int{arr[0], arr[1]},
			[]int{arr[2], arr[3]},
			[]int{arr[4], arr[5]},
			[]int{arr[6], arr[7]},
		}))
    }
}
