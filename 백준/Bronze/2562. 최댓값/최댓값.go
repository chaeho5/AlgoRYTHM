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
	
	var num [9]int
	maxVal := 0
	maxIdx := 0
	for i := range num {
		fmt.Fscan(reader, &num[i])
		if num[i] > maxVal {
			maxVal = num[i]
			maxIdx = i 
		}
	}

	fmt.Fprintln(writer, maxVal)
	fmt.Fprint(writer, maxIdx + 1)
}