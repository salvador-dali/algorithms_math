/**
 just iterate over all possible values and break if the xor is not in the
 set of normal characters
 */
package main

import (
    "os"
	"fmt"
    "bufio"
    "strings"
    "strconv"
)

func decipher(chars []uint8){
	start	:= uint8(97)
	end		:= uint8(122)
	ASCII	:= map[uint8]bool{97 : true,  98 : true,  99 : true,  100 : true,  101 : true,  102 : true,  103 : true,  104 : true,  105 : true,  106 : true,  107 : true,  108 : true,  109 : true,  110 : true,  111 : true,  112 : true,  113 : true,  114 : true,  115 : true,  116 : true,  117 : true,  118 : true,  119 : true,  120 : true,  121 : true,  122 : true,  48 : true,  49 : true,  50 : true,  51 : true,  52 : true,  53 : true,  54 : true,  55 : true,  56 : true,  57 : true,  65 : true,  66 : true,  67 : true,  68 : true,  69 : true,  70 : true,  71 : true,  72 : true,  73 : true,  74 : true,  75 : true,  76 : true,  77 : true,  78 : true,  79 : true,  80 : true,  81 : true,  82 : true,  83 : true,  84 : true,  85 : true,  86 : true,  87 : true,  88 : true,  89 : true,  90 : true,  40 : true,  41 : true,  32 : true,  59 : true,  58 : true,  44 : true,  46 : true,  39 : true,  63 : true,  45 : true,  33 : true, }
	for c1 := start; c1 <= end; c1++{
		for c2 := start; c2 <= end; c2++{
			for c3 := start; c3 <= end; c3++{
				xorArr := []uint8{c1, c2, c3}
				found := true

				s := ""
				for i, v := range(chars){
					char := v ^ xorArr[i % 3]
					if ASCII[char]{
						s += string(v ^ xorArr[i % 3])
					} else {
						found = false
						break
					}
				}

				if found{
					fmt.Println(string(c1) + string(c2) + string(c3))
				}
			}
		}
	}
}

func readArr()[]uint8{
    arr := []uint8{}
    scanner := bufio.NewScanner(os.Stdin)
    scanner.Scan()
    for _, v := range(strings.Fields(scanner.Text())) {
        num, _ := strconv.Atoi(v)
        arr = append(arr, uint8(num))
    }
    return arr
}

func main(){
    t := 1
    fmt.Scanf("%d", &t)
    arr := readArr()
	decipher(arr)
}
