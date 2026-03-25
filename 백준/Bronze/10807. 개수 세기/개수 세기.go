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
	var n, v int

	fmt.Fscan(reader, &n)

	nums := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &nums[i])
	}

	fmt.Fscan(reader, &v)

	count := 0

	for i := 0; i < n; i++ {
		if nums[i] == v {
			count ++
		}
	}

	fmt.Fprintln(writer, count)
}