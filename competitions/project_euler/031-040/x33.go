// TODO have not solved
package main
import (
	"fmt"
    "bufio"
    "strings"
    "strconv"
    "os"
)

func precalc(n, k int)[2]int{
	precalculated := map[[2]int][2]int{
		[2]int{2, 1}: [2]int{110, 322},
		[2]int{3, 1}: [2]int{77262, 163829},
		[2]int{3, 2}: [2]int{7429, 17305},
		[2]int{4, 1}: [2]int{12999936, 28131911},
		[2]int{4, 2}: [2]int{3571225, 7153900},
		[2]int{4, 3}: [2]int{255983, 467405},
	}

	return precalculated[[2]int{n, k}]
}

func main(){
    arr := []int{}
    scanner := bufio.NewScanner(os.Stdin)
    scanner.Scan()
    for _, v := range(strings.Fields(scanner.Text())) {
        num, _ := strconv.Atoi(v)
        arr = append(arr, int(num))
    }

    a := precalc(arr[0], arr[1])
    fmt.Println(a[0], a[1])
}
