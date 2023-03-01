# Hello World in Nim

|  言語   |          README          |
| :-----: | :----------------------: |
| English | [README.md](./README.md) |
| 日本語  |      (このファイル)      |

## 使い方

```sh
nim c -r src/main.nim
# Hello World
```

## テスト

```sh
testament p 'tests/*.nim'
```

## Dockerで環境構築する方法

```sh
# イメージをビルド
docker image build -t awesome-helloworld-in-nim-1 .

# コンテナを実行してシェルを開く
docker container run --rm -it awesome-helloworld-in-nim-1
```
