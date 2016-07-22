package main
import (
	"fmt"
	"strings"
)

func helper(n int) string {
	var hundred int = n / 100
	var other int = n % 100
	res := []string {}
	small := []string{
		"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
		"Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen",
	}
	big := []string{
		"Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety",
	}
	if hundred > 0{
		res = append(res, small[hundred - 1], "Hundred")
	}
	if other > 0{
		if other < 20 {
			res = append(res, small[other - 4])
		} else {
			res = append(res, big[other / 10 - 1])
			if other % 10 > 0{
				res = append(res, small[other % 10 - 1])
			}
		}
	}
	return strings.Join(res, " ")
}

func spell(n uint64)string{
	if n == 0{
		return "Zero"
	}
	var trillion = n / 1000000000000
	n -= trillion * 1000000000000
	var billion = n / 1000000000
	n -= billion * 1000000000
	var million = n / 1000000
	n -= million * 1000000
	var thousand= n / 1000
	n -= thousand * 1000
	res := []string {}

	if trillion > 0{
		res = append(res, helper(int(trillion)), "Trillion")
	}
	if billion > 0{
		res = append(res, helper(int(billion)), "Billion")
	}
	if million > 0{
		res = append(res, helper(int(million)), "Million")
	}
	if thousand > 0{
		res = append(res, helper(int(thousand)), "Thousand")
	}
	if n > 0{
		res = append(res, helper(int(n)))
	}
	return strings.Join(res, " ")
}

func main(){

}
