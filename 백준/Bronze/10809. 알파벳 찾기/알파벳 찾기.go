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

	var alpha [26]int
	for i := 0; i < 26; i++{
		alpha[i] = -1
	}

	var s string
	fmt.Fscan(reader, &s)
	for i, v := range s {
		idx := v - 'a'

		if alpha[idx] == -1 {
			alpha[idx] = i
		}
	}


	for i := 0; i < 26; i++{
		fmt.Fprintf(writer, "%v ", alpha[i])
	}
}