package main
import (
	"fmt"
	"math"
	"bufio"
	"strconv"
	"sort"
	"os"
)

func sieveEratosthenes(n int) []bool {
	is_primes := make([]bool, n+1)
	for i := 2; i <= n; i++ {
		is_primes[i] = true
	}

	for i := 2; i*i <= n; i++ {
		if is_primes[i] {
			for j := i * i; j <= n; j += i {
				is_primes[j] = false
			}
		}
	}
	return is_primes
}

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

	primes := []int{}
	for k, v := range(sieveEratosthenes(int(math.Sqrt(float64(max))) + 1)){
		if v {
			primes = append(primes, k)
		}
	}

	set := map[int]bool{}
	for i := 0; i < len(primes); i++{
		for j := 0; j < len(primes); j++{
			for k := 0; k < len(primes); k++{
				x, y, z := primes[i], primes[j], primes[k]
				tmp := x * x + y * y * y + z * z * z * z
				if tmp > max {
					break
				}
				set[tmp] = true
			}
		}
	}

	values := []int{}
	for k, _ := range(set){
		values = append(values, k)
	}

	sort.Ints(values)

	for _, v := range(numbers){
		i := sort.Search(len(values), func(i int) bool {
			return values[i] > v
		})
		fmt.Println(i)
	}
}
