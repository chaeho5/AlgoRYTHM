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
	var n, x int

	fmt.Fscan(reader, &n, &x)

	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &a[i])
		if a[i] < x {
			fmt.Fprintf(writer,"%v ",a[i])
		}
	}

}