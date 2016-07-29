/**
straight forward DP which for every element checks the biggest
at the top and on the left and adds it to current.
Only on the first line and first column we do different things
like adding with previous
 */

package main
import (
    "fmt"
    "bufio"
    "strings"
    "os"
    "strconv"
)

func minimum(arr [][]uint64){
	for i:=0; i<len(arr); i++{
		for j:=0; j<len(arr); j++{
			var right, down uint64
			if i == 0 && j == 0{

			} else if i == 0{
				arr[i][j] += arr[i][j - 1]
			} else if j == 0{
				arr[i][j] += arr[i - 1][j]
			} else {
				down = arr[i - 1][j]
				right= arr[i][j - 1]

				if down < right{
					arr[i][j] += down
				} else {
					arr[i][j] += right
				}
			}
		}
	}
	fmt.Println(arr[len(arr) - 1][len(arr) - 1])
}

func readMatrix()[][]uint64{
    scanner := bufio.NewScanner(os.Stdin)
	var n int
    matrix := [][]uint64{} 
	fmt.Scanf("%d", &n)
	for scanner.Scan() {
        line := []uint64{}
        for _, v := range(strings.Fields(scanner.Text())){
            num, _ := strconv.Atoi(v)
            line = append(line, uint64(num))
        }
        matrix = append(matrix, line)
    }
    return matrix
}

func main(){
    matrix := readMatrix()
	minimum(matrix)
}
