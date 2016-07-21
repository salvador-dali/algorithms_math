/**
 the total number of all fibonacci numbers will be small (fibonacci growths exponentially).
 then create an array of sum of the numbers till N. For example first element will hold the
 sum of first number, second - the sum of first 2 numbers, and n-th the sum of first n numbers

 then you can answer queries in log(n) time, where n is the size of an array
 */
package main
import (
	"fmt"
	"sort"
)

func getAnswers(questions []int){
	var prev uint64 = 1
	var curr uint64 = 2
	var tmp uint64
	var i int
	eFibs:= []uint64{2}
	sums := []uint64{2}
	for curr < 10000{
		tmp = prev
		prev = curr
		curr += tmp

		if curr % 2 == 0{
			sums = append(sums, sums[len(sums) - 1] + curr)
			eFibs= append(eFibs, curr)
		}
	}
	for _, value := range questions {
		i = sort.Search(len(eFibs), func(i int) bool { return eFibs[i] > uint64(value) })
		fmt.Println(sums[i - 1])
	}
}

func main(){
	var T int
	var n int
	questions := []int{}
	fmt.Scanf("%d", &T)
	for T > 0{
		fmt.Scanf("%d", &n)
		questions = append(questions, n)
		getAnswers(questions)
		T--
	}
}
