package main

import (
    "fmt"
    "bufio"
    "os"
    "unicode"
)

var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)

func main() {
    defer writer.Flush()
    var str string
    fmt.Fscan(reader, &str)
    for _, v := range str {
        if unicode.IsLower(v){
            fmt.Fprintf(writer, "%c",unicode.ToUpper(v))
        } else {
            fmt.Fprintf(writer, "%c",unicode.ToLower(v))
        }
    }
}