# 0519_Exercise

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>exercise</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
</head>
<body>
  <h1>Dog Image(s)</h1>
  <hr>

  <h2>강아지</h2>
  <div class="container dogs"></div>
  <button id="dog">강아지</button>

  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    // Javascript (Library) -> Browser (요청)
    // axios: XHR 활용한 HTTP request 라이브러리
    // XHR: 비동기 함수
    const url = 'https://dog.ceo/api/breeds/image/random'
    const dogs = document.querySelector('.dogs')
    const dogButton = document.querySelector('#dog')
    dogButton.addEventListener('click', function(event) {
      axios.get(url)
        .then(res => {
          imgURL = res.data.message
          const imgTag = document.createElement('img')
          imgTag.src = imgURL
          imgTag.classList = 'col-4'

          dogs.appendChild(imgTag)
        })
    })


  </script>
</body>
</html>
```
