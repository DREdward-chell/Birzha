FROM golang:1.26.1-alpine AS builder
WORKDIR /backend
COPY /backend/go.mod .
RUN go mod download
COPY /backend/app .
RUN CGO_ENABLED=0 GOOS=linux go build -o /go-app app.go

FROM alpine:latest
WORKDIR /root/
COPY --from=builder /go-app .
CMD ["./go-app"]