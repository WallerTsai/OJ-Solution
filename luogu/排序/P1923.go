package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strconv"
)

func partition(nums []int, left, right int) int {
	pivotIdx := left + rand.Intn(right-left)
	pivot := nums[pivotIdx]
	nums[pivotIdx], nums[left] = nums[left], nums[pivotIdx]

	i, j := left+1, right-1
	for {
		for i <= j && nums[i] < pivot {
			i++
		}
		for i <= j && nums[j] > pivot {
			j--
		}
		if i >= j {
			break
		}
		nums[i], nums[j] = nums[j], nums[i]
		i++
		j--
	}
	nums[left], nums[j] = nums[j], nums[left]
	return j
}

func findKthSmallest(nums []int, k int) int {
	left, right := 0, len(nums)
	for {
		idx := partition(nums, left, right)
		if idx == k {
			return nums[idx]
		} else if idx > k {
			right = idx
		} else {
			left = idx + 1
		}
	}
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)

	next := func() int {
		scanner.Scan()
		val, _ := strconv.Atoi(scanner.Text())
		return val
	}

	n := next()
	k := next()

	nums := make([]int, n)
	for i := 0; i < n; i++ {
		nums[i] = next()
	}

	fmt.Print(findKthSmallest(nums, k))
}