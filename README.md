# jp-it-internship

日本のIT企業のサイトからインターンシップに関する記述があると思われるページを検索するプログラムです。

本モジュールはGoogle Custom Search APIを使っており、[1000回のクエリ辺り$5の料金](https://support.google.com/programmable-search/answer/9069107?hl=ja)が発生します。一回の実行で3000回程度のクエリが実行されますのでご注意ください。

# 設定

docker-compose.yml内にAPIに利用するトークンとSearch Engine IDを設定します。
設定に必要なAPI KEYとIDは[GCPのコンソール](https://developers.google.com/custom-search/v1/overview?hl=en_US)から作成してください。

```yml
    environment:
      - PYTHONIOENCODING=utf-8
      - LANG=C.UTF-8
      - PYTHONUSERBASE=/pip_modules
      - GOOGLE_API_KEY=<Custom Search APIが有効なAPI KEY>
      - GOOGLE_SEARCH_ENGINE=<Web全体が検索可能なCustom Search EngineのID>
```

# usage

コンテナのセットアップとライブラリのインストール
```sh
make install
```

[女性の活躍推進企業データベース](https://positive-ryouritsu.mhlw.go.jp/positivedb/opendata/)からCSVデータをダウンロードし、jsonファイルを構築
```sh
make download
```

CSVから取得した企業名をCustom Search APIで検索し、1件目にヒットした結果をjsonファイルに格納
```sh
make url
```

CSVから取得した企業名と「インターンシップ」で検索した結果のうち上位3件をjsonファイルに格納
```sh
make internship
```

jsonファイルをCSVとして再度、保存
```sh
make convert
```



