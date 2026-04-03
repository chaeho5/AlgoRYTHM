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

	var n, m, a, b int
	fmt.Fscan(reader, &n, &m)

	basket := make([]int, n)
	for i := range basket{
		basket[i] = i + 1
	}

	for i := 0; i < m; i++{
		fmt.Fscan(reader, &a, &b)
		start, end := a - 1, b - 1
		
		for start < end {
			basket[start], basket[end] = basket[end], basket[start]
			start ++
			end --
		}
	}

	for _, v := range basket {
		fmt.Fprintf(writer, "%v ", v)
	}
	
}