/**
 implementation after I read:
 http://www.suntzupoker.com/one-pair.aspx
 */

package main
import (
    "fmt"
    "bufio"
    "os"
    "sort"
    "strings"
)

func readManyStrings()[]string{
    var T int
    fmt.Scanf("%d", &T)

    scanner, arr_strings := bufio.NewScanner(os.Stdin), []string{}
    for T > 0 {
        T--
        scanner.Scan()
		arr_strings = append(arr_strings, scanner.Text())
    }
    return arr_strings
}

func isStraight(cards []int)bool{
	withAceCards := []int{2, 3, 4, 5, 14}
	isWithAce := true
	for i:=0; i < 5; i++{
		if cards[i] != withAceCards[i]{
			isWithAce = false
		}
	}
	if isWithAce{
		return true
	}

	for i := 0; i < 4; i++{
		if cards[i + 1] - cards[i] != 1{
			return false
		}
	}
	return true
}

func analyseHand(arr []string)([10]bool, [10]int){
	cards, suits := []int{}, []int{}
	cardsMap := map[string]int{"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14, }
	suitsMap := map[string]int{"S": 0, "C": 1, "H": 2, "D": 3, }
	suitsSet, cardsCount := map[int]bool{}, map[int]int{}

	for _, v := range(arr){
		cardNum, suitNum := cardsMap[string(v[0])], suitsMap[string(v[1])]
		cards = append(cards, cardNum)
		suits = append(suits, suitNum)

		suitsSet[suitNum] = true
		cardsCount[cardNum]++
	}
	sort.Ints(cards)

	answersBool := [10]bool{}
	answersNums := [10]int{}

	// find the highest value card
	num, mul := 0, 1
	for i := 0; i < 5; i++{
		num += cards[i] * mul
		mul *= 100
	}
	answersNums[0] = num

	for k, v := range(cardsCount){
		if v == 2 && answersBool[1]{		// Two Pairs
			answersBool[2] = true
			answersNums[2] = k

			if answersNums[2] < answersNums[1]{
				answersNums[2], answersNums[1] = answersNums[1], answersNums[2]
			}
		}

		// One Pair
		if v == 2 && !answersBool[1]{
			answersBool[1] = true
			answersNums[1] = k
		}

		// Three of a kind
		if v == 3{
			answersBool[3] = true
			answersNums[3] = k
		}

		// Four of a kind
		if v == 4{
			answersBool[7] = true
			answersNums[7] = k
		}
	}

	// Flush
	if len(suitsSet) == 1{
		answersBool[5] = true
	}

	// Full house
	if answersBool[3] && answersBool[1]{
		answersBool[6] = true
	}

	// Straight
	if isStraight(cards){
		answersBool[4] = true
		// check if it was created with an Ace
		if cards[4] == 14{
			answersNums[4] = 5
		} else {
			answersNums[4] = cards[4]
		}
	}

	// Straight Flush
	if answersBool[4] && answersBool[5]{
		answersBool[8] = true
	}

	// Royal Flush
	if answersBool[8] && cards[0] == 10{
		answersBool[9] = true
	}

	return answersBool, answersNums
}

func parse(s string)([]string, []string){
	arr := strings.Fields(s)
	return arr[:5], arr[5:]
}

func compareScore(boolean_1, boolean_2 [10]bool, numbers_1, numbers_2 [10]int)bool{
	equal := 0
	for i := 9; i >= 0; i--{
		if boolean_1[i] || boolean_2[i]{
			if boolean_1[i] != boolean_2[i]{
				return boolean_1[i]
			}
			equal = i
			break
		}
	}

	for i := equal; i >= 0; i--{
		if numbers_1[i] == numbers_2[i]{
			continue
		}

		return numbers_1[i] > numbers_2[i]
	}
	return true
}

func findWinner(s string){
	hand1, hand2 := parse(s)
	booleans_1, nums_1 := analyseHand(hand1)
	booleans_2, nums_2 := analyseHand(hand2)
	res := compareScore(booleans_1, booleans_2, nums_1, nums_2)
	if res{
		fmt.Println("Player 1")
	} else {
		fmt.Println("Player 2")
	}
}

func main(){
    list := readManyStrings()
    for _, s := range(list){
        findWinner(s)
    }
}

