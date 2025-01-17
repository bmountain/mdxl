# ユーザ情報変更機能

## プロフィール画像変更

### 正常 OK プロフィール画像変更

- 二行に分かれた
- 前提を書けるか

1. アプリを立ち上げる
2. メイン画面でプロフィール画像変更ボタンをクリック
3. 画像を選択
4. 画像変更ボタンをクリック
* [ ] アプリでエラーが表示されないこと
* [ ] 画像が変更されていること

## ユーザ名変更

### 正常 OK 最小長ユーザ名設定

1. アプリを立ち上げる
2. メイン画面でユーザ名を"a" と設定する
3. OKをタップする
* [ ] アプリでエラーが表示されないこと
* [ ] アプリを再起動し、メイン画面でユーザ名が "a" となっていること

- 備考はココに書いてね～

### 正常 OK 最大長ユーザ名設定

1. アプリを立ち上げる
2. メイン画面でユーザ名を"12345678" と設定する
3. OKをタップする
* [ ] アプリでエラーが表示されないこと

* [ ] アプリを再起動し、メイン画面でユーザ名が "12345678" となっていること

### 異常 未実施 最小長以下のユーザ名設定

1. アプリを立ち上げる
2. メイン画面でユーザ名を "" と設定する
3. OKをタップする
* [ ] エラーダイアログ表示 "名前は1文字以上8文字以下で入力してください"

- 備考はココに書いてね～

### 異常 NG 最大長以上のユーザ名設定

1. アプリを立ち上げる
2. メイン画面でユーザ名を"123456789" と設定する
3. OKをタップする
* [ ] エラーダイアログ表示 "名前は1文字以上8文字以下で入力してください"


## パスワード変更

### 正常 未実施 最小長パスワード設定

1. アプリを立ち上げる
2. メイン画面でパスワードを"a" と設定する
3. OKをタップする
* [ ] アプリでエラーが表示されないこと
- 備考はココに書いてね～

### 正常 OK 最大長パスワード設定

1. アプリを立ち上げる
2. メイン画面でパスワードを"12345678" と設定する
3. OKをタップする
* [ ] アプリでエラーが表示されないこと

### 異常 OK 最小長以下のパスワード設定

1. アプリを立ち上げる
2. メイン画面でパスワードを "123" と設定する
3. OKをタップする
* [ ] エラーダイアログ表示 "パスワードは4文字以上20文字以下で入力してください"

- 備考はココに書いてね～

### 異常 NG 最大長以上のパスワード設定

1. アプリを立ち上げる
2. メイン画面でパスワードを"123456789abcdefghijkl" と設定する
3. OKをタップする
* [ ] エラーダイアログ表示 "パスワードは4文字以上20文字以下で入力してください"

# ログイン機能

## ログイン

### 正常 OK ログイン

1. アプリを立ち上げる
2. メイン画面でログインボタンをクリック
3. ユーザ名とパスワードを入力
4. ログインボタンをクリック
5. ログイン成功画面が表示される
* * [ ] ログイン成功画面が表示されること
* [ ] ログイン成功画面にユーザ名が表示されること

### 異常 OK 存在しないユーザ名

1. アプリを立ち上げる
2. メイン画面でログインボタンをクリック
3. 存在しないユーザ名と存在しないパスワードとを入力
4. ログインボタンをクリック
5. ログイン失敗画面が表示される

* [ ] ログイン失敗画面が表示されること
* [ ] ログイン失敗画面にエラーメッセージが表示されること
