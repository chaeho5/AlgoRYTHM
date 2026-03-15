package main

import (
	"fmt"
	"bufio"
	"os"
)

var reader = bufio.NewReader(os.Stdin)

func main() {
	var id string
	fmt.Fscan(reader, &id)
	fmt.Printf("%v??!", id)
}