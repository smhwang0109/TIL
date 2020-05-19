# 0518_Exercise

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>0518 exercise & workshop</title>
</head>
<body>
  <h2>Add New Todo</h2>
  <p id="addNewTodo"></p>
  <hr>

  <h2>Todo List</h2>
  <ul id="todoList"></ul>
  <hr>

  <h2>Completed Tasks</h2>
  <ul id="completedTasks"></ul>
  <hr>

  <script>


    const newTodo = document.querySelector('#addNewTodo')

    const newTodoLabel = document.createElement('label')
    newTodoLabel.innerText = 'Add New Todo: '

    const newTodoInput = document.createElement('input')
    // 상용 어트리뷰트 사용 시
    // newTodoInput.type = 'text'

    // 사용자 정의 어트리뷰트 사용 시
    // newTodoInput.setAttribute('설정할 attribute명', 'attribute값')
    newTodoInput.setAttribute('type', 'text')

    const newTodoButton = document.createElement('button')
    newTodoButton.innerText = 'Add'

    newTodo.appendChild(newTodoLabel)
    newTodo.appendChild(newTodoInput)
    newTodo.appendChild(newTodoButton)

    const todoList = document.querySelector('#todoList')

    function makeTodoList(text) {
      const todoLi = document.createElement('li')
  
      const todoCheck = document.createElement('input')
      todoCheck.setAttribute('type', 'checkbox')
  
      const todoLabel = document.createElement('label')
      todoLabel.innerText = text
  
      const todoInput = document.createElement('input')
  
      const todoEdit = document.createElement('button')
      todoEdit.innerText = 'Edit'
  
      const todoDelete = document.createElement('button')
      todoDelete.innerText = 'Delete'

      todoList.appendChild(todoLi)
      todoLi.appendChild(todoCheck)
      todoLi.appendChild(todoLabel)
      todoLi.appendChild(todoInput)
      todoLi.appendChild(todoEdit)
      todoLi.appendChild(todoDelete)

    }

    makeTodoList('Django ModelForm 복습')
    makeTodoList('Javascript DOM 조작 복습')
    makeTodoList('Django static, media 복습')




  </script>
</body>
</html>
```

