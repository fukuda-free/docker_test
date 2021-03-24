# プロジェクト構築
docker-compose run web rails new . --force --database=mysql

# config/database.ymlを設定してから次を実行
```
default: &default
  adapter: mysql2
  encoding: utf8
  pool: <%= ENV.fetch("RAILS_MAX_THREADS") { 5 } %>
  username: root
  password: password # docker-compose.ymlのMYSQL_ROOT_PASSWORD
  host: db # docker-compose.ymlのservice名
```

docker-compose build --no-cache
docker-compose run web rake db:create db:migrate
docker-compose build
docker-compose up
