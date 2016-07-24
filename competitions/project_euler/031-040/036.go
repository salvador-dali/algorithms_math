/**
 with the help of palindrom utility function check if the number is a palindrom in
 base_10 and the if base_k is a palindrom
 */
package main
import (
	"fmt"
	"strconv"
)

func isPalindrom(s string)bool{
	for i := 0; i < len(s)/2; i++{
		if s[i] !=s[len(s) - i - 1]{
			return false
		}
	}
	return true
}

func main(){
	var n, k int
	fmt.Scanf("%d %d", &n, &k)
	sum:=0
	for i:=1; i<n; i++{
		if isPalindrom(strconv.Itoa(i)) && isPalindrom(strconv.FormatInt(int64(i), k)){
			sum += i
		}
	}
	fmt.Println(sum)
}
