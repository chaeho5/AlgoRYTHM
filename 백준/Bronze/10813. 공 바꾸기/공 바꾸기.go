package main

import (
	"bufio"
	"fmt"
	"os"
)

var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)

func main() {
	defer writer.Flush()

	var n, m int
	fmt.Fscan(reader, &n, &m)

	var a, b int
	basket := make([]int, n)

	for i := 0; i < n; i++ {
		basket[i] = i + 1
	}

	for i := 0; i < m; i++ {
		fmt.Fscan(reader, &a, &b)
		basket[a-1], basket[b-1] = basket[b-1], basket[a-1]
	}

	for i := 0; i < n; i++ {
		fmt.Fprintf(writer, "%v ", basket[i])
	}

}
