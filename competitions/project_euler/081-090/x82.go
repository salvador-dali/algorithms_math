package main
import (
	"fmt"
	"bufio"
	"os"
    "strconv"
	"strings"
	"container/heap"
	"time"
)

type Item struct {
	value 		int	// The value of the item; arbitrary.
	priority	int // The priority of the item in the queue.
	index 		int // The index of the item in the heap.
}

type PriorityQueue []*Item

func (pq PriorityQueue) Len() int {
	return len(pq)
}

func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].priority < pq[j].priority
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueue) Push(x interface{}) {
	n := len(*pq)
	item := x.(*Item)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	item.index = -1
	*pq = old[0 : n-1]
	return item
}

func (pq *PriorityQueue) update(item *Item, value int, priority int) {
	item.value = value
	item.priority = priority
	heap.Fix(pq, item.index)
}

func matrixToGraph(matrix [][]int)map[int]map[int]int{
	x, y := len(matrix[0]), len(matrix)
	graph := map[int]map[int]int{}

	for i, row := range(matrix){
		for j, _ := range(row){
			value := i * x + j
			graph[value] = map[int]int{}
			if i > 0{
				graph[value][value - x] = matrix[i - 1][j]
			}
			if i < y - 1{
				graph[value][value + x] = matrix[i + 1][j]
			}
			if j < x - 1{
				graph[value][value + 1] = matrix[i][j + 1]
			}
		}
	}

	graph[-1] = map[int]int{}
	graph[-2] = map[int]int{}
	for i := 0; i < y; i++{
		graph[-1][x * i] = matrix[i][0]
		graph[x * i + x - 1][-2] = 0
	}
	return graph
}

func dijkstraCost(graph map[int]map[int]int, start, end int) int{
	if start == end{
		return 0
	}
	frontier := make(PriorityQueue, 1)
	frontier[0] = &Item{value: start, priority: 0, index: 0}
	visited := map[int]bool{}
	heap.Init(&frontier)

	for frontier.Len() > 0 {
		element := heap.Pop(&frontier).(*Item)
		vertex, cost := element.value, element.priority
		visited[vertex] = true
		neighbors := graph[vertex]
		for vertex_new, cost_new := range(neighbors){
			if !visited[vertex_new]{
				if vertex_new == end{
					return cost + cost_new
				}
				heap.Push(&frontier, &Item{
					value: vertex_new,
					priority: cost + cost_new,
				})
			}
		}
	}
	return -1
}

func readMatrix()[][]int{
    scanner := bufio.NewScanner(os.Stdin)
    matrix  := [][]int{}
	for scanner.Scan() {
        line := []int{}
        for _, v := range(strings.Fields(scanner.Text())){
            num, _ := strconv.Atoi(v)
            line = append(line, int(num))
        }
        matrix = append(matrix, line)
    }
    return matrix
}

func main(){
	// takes 3 seconds to calculate 450 x 450 matrix
 	matrix := readMatrix()
	graph := matrixToGraph(matrix)
	cost := dijkstraCost(graph, -1, -2)
	fmt.Println(cost)
}
