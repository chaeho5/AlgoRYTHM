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

	var a, b string
	fmt.Fscan(reader, &a, &b)

	reverseA := ""
	for _, v := range a {
		reverseA = string(v) + reverseA
	}

	reverseB := ""
	for _, v := range b {
		reverseB = string(v) + reverseB
	}

	if reverseA > reverseB {
		fmt.Fprint(writer, reverseA)
	} else {
		fmt.Fprint(writer, reverseB)
	}
}