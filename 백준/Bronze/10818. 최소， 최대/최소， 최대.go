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
	fmt.Fscan(reader, &n)

	num := make([]int, n)

	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &num[i])
	}

	minVal, maxVal := num[0], num[0]
	for _, v := range num {
		minVal = min(minVal, v)
		maxVal = max(maxVal, v)
	}

	fmt.Fprintf(writer, "%v %v", minVal, maxVal)
}