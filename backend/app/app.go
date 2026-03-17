package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hi there, I love %s!", r.URL.Path[1:])
}

func main() {
	fmt.Printf("Starting server on http://%s:%s", os.Getenv("GO_HOST"), os.Getenv("GO_PORT"))

	http.HandleFunc("/", handler)
	log.Fatal(http.ListenAndServe(fmt.Sprintf("%s:%s", os.Getenv("GO_HOST"), os.Getenv("GO_PORT")), nil))
}
