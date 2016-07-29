/**
 the idea is to take a look at the number of rectangles in the
 1xn rectangle. There are n * (n + 1) / 2

 the same for another dimension. So in total n * (n + 1) * m * (m + 1) / 4
 */

package main
import (
	"fmt"
	"sort"
	"bufio"
	"strconv"
	"os"
	"math"
)

func readManyNumbers()(int, []int){
	var T int
	fmt.Scanf("%d", &T)

	scanner, numbers, max := bufio.NewScanner(os.Stdin), []int{}, 0
	for T > 0 {
		T--
		scanner.Scan()
		num, _ := strconv.Atoi(scanner.Text())
		numbers = append(numbers, num)
		if num > max{
			max = num
		}
	}
	return max, numbers
}

func main(){
	max, numbers := readManyNumbers()

	backwardMap := map[int]int{}
	arr := []int{}
	for i := 1; i * i < max + 3; i++{
		for j := 1; j <= i; j++{
			num := i * (i + 1) / 2 * j * (j + 1) / 2
			if i * j > backwardMap[num]{
				backwardMap[num] = i * j
			}
			arr = append(arr, num)
			if num > max{
				break
			}
		}
	}
	sort.Ints(arr)

	for _, v := range(numbers){
		i := sort.Search(len(arr), func(i int) bool {
			return arr[i] >= v
		})

		bestDelta, ans := math.Abs(float64(arr[i] - v)), arr[i]

		if i > 0 {
			attempt := math.Abs(float64(arr[i - 1] - v))
			if attempt < bestDelta{
				bestDelta, ans = attempt, arr[i - 1]
			} else if (attempt == bestDelta){
				if backwardMap[arr[i - 1]] > backwardMap[ans]{
					ans = arr[i - 1]
				}
			}
		}

		if i < len(arr) - 1{
			attempt := math.Abs(float64(arr[i + 1] - v))
			if attempt < bestDelta{
				bestDelta, ans = attempt, arr[i + 1]
			} else if (attempt == bestDelta){
				if backwardMap[arr[i + 1]] > backwardMap[ans]{
					ans = arr[i + 1]
				}
			}
		}

		fmt.Println(backwardMap[ans])
	}
}
