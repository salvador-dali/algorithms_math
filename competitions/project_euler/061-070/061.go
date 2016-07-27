/**
generate all possible figurative numbers. (there will not be a lot of them)
create a recursive function which adds one number at a time.
Make sure that the final list creates a ring and does not have duplicates
 */

package main
import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"strconv"
	"sort"
)

func readArr()[]int{
    arr := []int{}
    scanner := bufio.NewScanner(os.Stdin)
    scanner.Scan()
    for _, v := range(strings.Fields(scanner.Text())) {
        num, _ := strconv.Atoi(v)
        arr = append(arr, num)
    }
    return arr
}

func getGenerator(n int) []int{
	functions := map[int]func(i int) int {
		3: func(i int)int{	return i * (i + 1) / 2 },
		4: func(i int)int{	return i * i },
		5: func(i int)int{	return i * (3 * i - 1)/2 },
		6: func(i int)int{	return i * (2 * i - 1) },
		7: func(i int)int{	return i * (5 * i - 3)/2 },
		8: func(i int)int{	return i * (3 * i - 2) },
	}

	f := functions[n]
	numbers := []int{}
	for i := 10; ; i++{
		num := f(i)
		if num > 9999{ break }
		if num > 999{
			numbers = append(numbers, num)
		}
	}
	return numbers
}

func findNums(nums []int, set map[int]bool, dict map[int][]int, n int) int{
	if len(nums) == n{
		if nums[0] / 100 == nums[len(nums) - 1 ] % 100{
			s := 0
			setOfNums := map[int]bool{}
			for _, v := range(nums){
				s += v
				if setOfNums[v]{
					return 0
				}
				setOfNums[v] = true
			}
			
			return s
		}
	}

	left := nums[len(nums) - 1] % 100

	for k, arr := range(dict){
		if !set[k]{
			for _, v := range(arr){
				if left == v / 100{
					// create a copy of nums
					copyNums := []int{}
					for _, value := range(nums){ copyNums = append(copyNums, value) }
					copyNums = append(copyNums, v)

					// create a copy of set
					copySet := map[int]bool{}
					for key, _ := range set { copySet[key] = true }
					copySet[k] = true

					r := findNums(copyNums, copySet, dict, n)
					if r > 0{
						return r
					}
				}
			}
		}
	}
	
	return 0
}

func main(){
    ttt := 0
    fmt.Scanf("%d", &ttt)
	arr := readArr()
	answers := map[int]bool{}
	dict := map[int][]int{}
	list := [][2]int{}
	for _, v := range(arr){
		for _, el := range(getGenerator(v)){
			dict[v] = append(dict[v], el)
			list = append(list, [2]int{el, v})
		}
	}
	for _, v := range(list){
		key, value := v[1], v[0]
		r := findNums([]int{value}, map[int]bool{key: true,}, dict, len(arr))
		if r > 0{
			answers[r] = true
		}
	}

	answersList := []int{}
	for k, _ := range(answers){
		answersList = append(answersList, k)
	}

	sort.Ints(answersList)
	for _, v := range(answersList){
		fmt.Println(v)
	}
}
