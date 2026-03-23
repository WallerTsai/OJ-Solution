package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func solve() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)

	if !scanner.Scan() {
		return
	}
	n, _ := strconv.Atoi(scanner.Text())

	var candidate int
	count := 0

	for i := 0; i < n; i++ {
		scanner.Scan()
		num, _ := strconv.Atoi(scanner.Text())

		if count == 0 {
			candidate = num
			count = 1
		} else if num == candidate {
			count++
		} else {
			count--
		}
	}

	fmt.Println(candidate)
}

func main() {
	solve()
}


package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func majorityElementK(scanner *bufio.Scanner, k int) int {
	candidates := make(map[int]int)

	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())

	for i := 0; i < n; i++ {
		scanner.Scan()
		num, _ := strconv.Atoi(scanner.Text())

		if count, ok := candidates[num]; ok {
			candidates[num] = count + 1
		} else if len(candidates) < k-1 {
			candidates[num] = 1
		} else {
			for key, val := range candidates {
				if val-1 == 0 {
					delete(candidates, key)
				} else {
					candidates[key] = val - 1
				}
			}
		}
	}


	var result int
	for key := range candidates {
		result = key
		break
	}
	return result
}

func main() {

	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)

	fmt.Println(majorityElementK(scanner, 2))
}