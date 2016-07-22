/**
 check all possible variation:
 - the numbers are on the row
 - the numbers are on the column
 - the numbers are on the diagonal in right/down
 - the numbers are on the diagonal in left/down
 */
package main

import (
	"fmt"
	"strconv"
)

func findMax(matrix [][]int)int{
    var max int = 0
    for i:=0; i<20; i++{
        for j:=0; j<17; j++{
            tmp := matrix[i][j] * matrix[i][j + 1] * matrix[i][j + 2] * matrix[i][j + 3]
            if tmp > max{
                max = tmp
            }
        }
    }

    for i:=0; i<17; i++{
        for j:=0; j<20; j++{
            tmp := matrix[i][j] * matrix[i + 1][j] * matrix[i + 2][j] * matrix[i + 3][j]
            if tmp > max{
                max = tmp
            }
        }
    }

    for i:=0; i<17; i++{
        for j:=0; j<17; j++{
            tmp := matrix[i][j] * matrix[i + 1][j + 1] * matrix[i + 2][j + 2] * matrix[i + 3][j + 3]
            if tmp > max{
                max = tmp
            }
        }
    }

    for i:=3; i<20; i++{
        for j:=0; j<17; j++{
            tmp := matrix[i][j] * matrix[i - 1][j + 1] * matrix[i - 2][j + 2] * matrix[i - 3][j + 3]
            if tmp > max{
                max = tmp
            }
        }
    }
    return max
}

func main(){
    var s string
    arr := [][]int {}
    for i:=0; i<20; i++{
        tmp := []int{}
        for j:=0; j<20; j++{
            fmt.Scanf("%s", &s)
            val, _ := strconv.Atoi(s)
            tmp = append(tmp, val)
        }
        arr = append(arr, tmp)

    }
	fmt.Println(findMax(arr))
}
