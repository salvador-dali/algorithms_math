package main

import (
	"bufio"
	"os"
    "fmt"
    "strconv"
)
var scanner = bufio.NewScanner(os.Stdin)

func helper(s string, k int) int{
	var maxProduct int = 0
	var curProduct int
	for i:= 0; i < len(s) - k; i++{
		curProduct = 1
		for j:=0; j < k; j++{
			curProduct *= int(s[i + j] - 48)
		}
		if curProduct > maxProduct{
			maxProduct = curProduct
		}
	}
	return maxProduct
}

func next() string {
	if !scanner.Scan() {
		panic("Scan error")
	}
	return scanner.Text()
}

func nextInt() int {
	n, err := strconv.Atoi(next())
	if err != nil {
		panic(err)
	}
	return n
}

func main() {
    scanner.Split(bufio.ScanWords)
    var T = nextInt()
    var _, k int
    var s string
    
    for T > 0{
        T--
        _ = nextInt()
        k = nextInt()
        s = next()
        fmt.Println(helper(s, k))
    }
}
