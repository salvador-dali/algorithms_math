// https://www.hackerrank.com/contests/infinitum12/challenges/polynomial-and-its-roots
// Vieta theorem

package main
import (
    "fmt"
    "bufio"
    "strings"
    "strconv"
    "os"
)

func main() {
    arr := []int{}
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
    scanner.Scan()
	for _, v := range (strings.Fields(scanner.Text())) {
		num, _ := strconv.Atoi(v)
		arr = append(arr, num)
	}
    n := len(arr) - 1
    sum := - arr[n - 1] / arr[n]
    prod:= arr[0] / arr[n]
    if n % 2 == 1 {
        prod = - prod
    }
    fmt.Print(sum, " ", prod)
}
