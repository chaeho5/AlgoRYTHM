package main

import (
	"fmt"
	"bufio"
	"os"
)

var reader = bufio.NewReader(os.Stdin)

func main() {
	var yoonyear int
	fmt.Fscan(reader, &yoonyear)

	if yoonyear%400 == 0 || yoonyear%4 == 0 && yoonyear%100 != 0{
		fmt.Print("1")
	} else {
		fmt.Print("0")
	}
}