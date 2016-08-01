package main
import (
	"fmt"
)

func shifts(arr []int){
	for i := 0; i < len(arr); i++ {
		arr = append(arr[1:], arr[0])
		fmt.Println(arr)
	}

}

func main(){
	arr := []int{1, 2, 3, 4, 5}
	shifts(arr)
}
