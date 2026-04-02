package main

import (
	"fmt"
	"bufio"
	"os"
)

var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)

func main() {
	defer writer.Flush()

	var n int
	var nums [42]bool
	count := 0
	for i := 0; i < 10; i++ {
		fmt.Fscan(reader, &n)
		nums[n % 42] = true
	}

	for _, v := range nums {
		if v {
			count++
		}
	}

	fmt.Fprint(writer, count)
}