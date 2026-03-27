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

	var n, m int
	fmt.Fscan(reader, &n, &m)

	var a, b, k int

	basket := make([]int, n + 1)

	for i := 0; i < m; i++ {
		fmt.Fscan(reader, &a, &b, &k)
		for j := a; j <= b; j++ {
			basket[j] = k
		}
	}

	for v := 1; v < len(basket); v++{
		fmt.Fprintf(writer, "%v " ,basket[v])
	}
}