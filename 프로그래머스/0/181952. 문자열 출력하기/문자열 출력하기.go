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
    var s1 string
    fmt.Fscan(reader, &s1)
    fmt.Fprint(writer, s1)
}