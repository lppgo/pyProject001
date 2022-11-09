package main

import (
	"fmt"
	"log"
	"os"

	"github.com/apache/arrow/go/arrow/array"
	"github.com/apache/arrow/go/arrow/ipc"
)

func main() {
	fmt.Printf("go读取arrow/ipc格式文件(feather version v2),magic bytes:%s\n", string(ipc.Magic))

	f, err := os.Open("../test2.fea")
	if err != nil {
		log.Fatalf("open error:%s\n", err.Error())
	}
	defer f.Close()

	info, _ := f.Stat()
	fmt.Printf("读取文件成功:%+v\n", info)

	// reader := bufio.NewReader(f)
	// // chunk := make([]byte, 4096)

	// for i := 0; i < 10; i++ {
	// 	line, _, err := reader.ReadLine()
	// 	fmt.Printf("%d , %s ,%v\n", i, string(line), err)
	// }

	// freader, err := ipc.NewReader(f)
	freader, err := ipc.NewFileReader(f)
	if err != nil {
		log.Fatalf("new file reader error:%s\n", err.Error())
	}
	fmt.Println("version: ", freader.Version().String())

	rec, err := freader.Read()
	if err != nil {
		log.Fatalf("reade error:%s\n", err.Error())
	}
	rec.Retain()
	fmt.Println("rows 行数:", rec.NumRows())
	fmt.Println("cols 列数:", rec.NumCols())
	fmt.Println("cols[1] name:", rec.ColumnName(1))
	fmt.Println("        cols:", rec.Columns())
	fmt.Println("cols[1] dataType:", rec.Columns()[1].DataType())
	fmt.Println("cols[1] dataLen:", rec.Columns()[1].Data().Len())
	fmt.Println("cols[1] dataBuf:", rec.Columns()[1].(*array.Float64).Float64Values()[1])
	// fmt.Println("cols[1] dataBuf:", string(rec.Columns()[1].Data().Buffers()[1].Bytes()))
	// fmt.Println("cols[1] dataBuf:", string(rec.Columns()[1].Data().Buffers()[1].Buf()))
}
