/**
 store all the names, sort them and
 calculate the score for each of the name in the loop
 and store them in the dictionary
 then extract each needed value from the dictionary
 */

package main
import (
	"fmt"
    "sort"
)

func getScore(s string, n int)int{
	var sum int = 0
	for i:=0; i < len(s); i++{
		sum += int(s[i] - 64)
	}
	return sum * n
}

func main(){
	var T int
	var s string
	dict := map[string]int{}
    list := []string{}
	fmt.Scanf("%d", &T)
	for i := 1; i <= T; i++ {
		fmt.Scanf("%s", &s)
        list = append(list, s)
	}
    sort.Strings(list)

    for i := 1; i <= T; i++{
        dict[list[i - 1]] = getScore(list[i - 1], i)
    }

	fmt.Scanf("%d", &T)
	for T > 0 {
		T--
		fmt.Scanf("%s", &s)
		fmt.Println(dict[s])
	}
}
