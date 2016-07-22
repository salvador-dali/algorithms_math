/**
 take only first 14 digits (may be you can take less) and sum them up
 in the number you received, check it length and remove last irrelevant digits
 till the length will be 10
 */
package main

import (
	"fmt"
	"strconv"
	"math"
)

func summation(list []string){
	var num, sum int
	for _, val := range list{
		num, _ = strconv.Atoi(val[0:14])
		sum += num
	}
	i := len(strconv.Itoa(sum)) - 10
	res := sum / int(math.Pow(float64(10), float64(i)))
	fmt.Println(res)
}

func main(){
	var T int
	var s string
	list := []string{}
	fmt.Scanf("%d", &T)
	for T > 0{
		T--
		fmt.Scanf("%s", &s)
		list = append(list, s)
	}
	summation(list)
}
