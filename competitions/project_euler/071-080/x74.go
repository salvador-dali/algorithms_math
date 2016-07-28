package main
import (
	"fmt"
)

func numToDigits(n uint64)[]int{
	digits := []int{}
	for n > 0{
		digits = append(digits, int(n % 10))
		n /= 10
	}
	return digits
}

func arrToNum(arr []int)uint64{
	f := [10]uint64{1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880}
	num := uint64(0)
	for _, v := range(arr){
		num += f[v]
	}
	return num
}

func chain(n uint64)int{
	num := 1
	set := map[uint64]bool{n: true}

	for {
		fmt.Print(n, " ")
		n = arrToNum(numToDigits(n))
		_, v := set[n]
		if v{
			break
		}
		set[n] = true
		num += 1
	}
	fmt.Println()
	return num
}

func chain2(n uint64, seenMap map[uint64]int)int{
	if seenMap[n] > 0{
		return seenMap[n]
	}

	num := 1
	set := map[uint64]bool{n: true}
	list:= []uint64{n}

	for {
		n = arrToNum(numToDigits(n))
		if seenMap[n] > 0{
			res := seenMap[n] + num
			fmt.Println(list)
			for num > 0{
				num--

			}
			return res
		}

		_, v := set[n]
		if v{
			fmt.Println("This part", n)
			res := num
			fmt.Println(list)
			for num > 0{
				fmt.Println(list[num - 1], num)
				num--
			}
			return res
		}
		set[n] = true
		list = append(list, n)
		num += 1
	}
	return num
}


func main(){
	n := uint64(12)
	chain(n)

	seenMap := map[uint64]int{0: 2}
	fmt.Println(seenMap)
	chain2(n, seenMap)

//	var T, n, l int
//	fmt.Scanf("%d", &T)
//
//	max := 0
//	questions := [][]int{}
//	for T > 0{
//		T--
//		fmt.Scanf("%d %d", &n, &l)
//		if n > max{
//			max = n
//		}
//		tmp := []int{n, l}
//		questions = append(questions, tmp)
//	}
//
//
//	res := []int{2}
//	for i := uint64(1); i <= uint64(max); i++{
//		res = append(res, chain(i))
//	}
//
//	for _, tmp := range(questions){
//		N := tmp[0]
//		L := tmp[1]
//		haveAdded := false
//		for i := 0; i <= N; i++{
//			if res[i] == int(L){
//				fmt.Print(i, " ")
//				haveAdded = true
//			}
//		}
//		if haveAdded{
//			fmt.Println()
//		} else {
//			fmt.Println(-1)
//		}
//
//	}
}
