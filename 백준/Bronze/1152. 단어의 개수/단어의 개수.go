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

	var s string
	count := 0
	for {
		_, err := fmt.Fscan(reader, &s)
		if err != nil{
			break
		}
		count ++
	}
	
	fmt.Fprint(writer, count)

}