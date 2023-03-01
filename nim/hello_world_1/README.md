# Hello World in Nim

| Language |             README             |
| :------: | :----------------------------: |
| English  |          (This file)           |
|  日本語  | [README_ja.md](./README_ja.md) |

## Usage

```sh
nim c -r src/main.nim
# Hello World
```

## Testing

```sh
testament p 'tests/*.nim'
```

## With Docker

```sh
# Build the image
docker image build -t awesome-helloworld-in-nim-1 .

# Run the container and open a shell
docker container run --rm -it awesome-helloworld-in-nim-1
```
