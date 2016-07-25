/**
 find all the primes. For each prime check its digits and create a map, where
 the key is the digits (10 element array) and value is the array of the primes that have
 these digits. Now for each of this key, check if there is an arithmetic progression there.

 Note that there are more than one progression.

 Then sort of the answers.
 */
package main

import (
	"fmt"
	"sort"
	"strconv"
    "bufio"
    "os"
    "strings"
)

func sieveEratosthenes(n uint64)[]uint64{
	c := make([]bool, n)
	c[1] = true
	var p uint64 = 2
	var i, p2 uint64

	for {
		p2 = p * p
		if p2 >= n {
			break
		}
		for i = p2; i < n; i += p {
			c[i] = true
		}
		for {
			p++
			if !c[p] {
				break
			}
		}
	}

	primes := []uint64{}
	for i = 1; i < n; i++{
		if c[i] == false {
			primes = append(primes, i)
		}
	}
	return primes
}

func numToArr(n int)[10]int{
	res := [10]int{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
	for n > 0{
		res[n % 10]++
		n /= 10
	}
	return res
}

func isArithmeticProgressionExist(arr []int)[][]int{
	set := map[int]bool{}
	for _, v := range(arr){
		set[v] = true
	}

	allProgressions := [][]int{}
	for i := 0; i < len(arr); i++{
		for j := i + 1; j < len(arr); j++{
			diff := arr[j] - arr[i]

			if set[arr[j] + diff]{
				progression := []int{arr[i], arr[j], arr[j] + diff}
				next := progression[len(progression) - 1] + diff
				for set[next]{
					progression = append(progression, next)
					next = progression[len(progression) - 1] + diff
				}

				allProgressions = append(allProgressions, progression)
			}
		}
	}

	return allProgressions
}

func printArr(arr []int){
	s := ""
	for _, v := range(arr){
		s += strconv.Itoa(v)
	}
	fmt.Println(s)
}

func readArr()[]int{
    arr := []int{}
    scanner := bufio.NewScanner(os.Stdin)
    scanner.Scan()
    for _, v := range(strings.Fields(scanner.Text())) {
        num, _ := strconv.Atoi(v)
        arr = append(arr, int(num))
    }
    return arr
}

func main(){
    array := readArr()
	N := array[0]
	K := array[1]
	primes := sieveEratosthenes(uint64(10 * N))
	permutations := map[[10]int][]int{}
	for _, v := range(primes){
		arr := numToArr(int(v))
		permutations[arr] = append(permutations[arr], int(v))
	}


	answers := [][]int{}
	for _, v := range(permutations){
		if len(v) >= K && v[0] <= N{
			all_progressions := isArithmeticProgressionExist(v)
			for _, prog := range(all_progressions){
				if len(prog) >= K && prog[0] <= N{
					answers = append(answers, prog[:K])
				}
			}
		}
	}

	keys := []int{}
	map_of_keys := map[int][][]int{}
	for _, v := range(answers){
		keys = append(keys, v[0])
		map_of_keys[v[0]] = append(map_of_keys[v[0]], v)
	}
	sort.Ints(keys)
	prev := 0
	for _, k := range(keys){
		if prev != k {
			for _, v := range(map_of_keys[k]){
				printArr(v)
			}
		}
		prev = k
	}
}
