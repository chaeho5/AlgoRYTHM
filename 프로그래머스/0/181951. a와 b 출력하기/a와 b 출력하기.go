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
    var a, b int
    fmt.Fscan(reader, &a, &b)
    fmt.Fprintf(writer, "a = %v\n", a)
    fmt.Fprintf(writer, "b = %v", b)
}