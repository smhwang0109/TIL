# 0518_Workshop

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

      todoCheck.addEventListener('click', function(event) {
        makeCompletedTask(todoLabel.innerText)
        todoLi.remove()
      })
  
      const todoLabel = document.createElement('label')
      todoLabel.innerText = text
  
      const todoInput = document.createElement('input')
  
      const todoEdit = document.createElement('button')
      todoEdit.innerText = 'Edit'

      todoEdit.addEventListener('click', function(event) {
        todoLabel.innerText = todoInput.value
        todoInput.value = null
      })
  
      const todoDelete = document.createElement('button')
      todoDelete.innerText = 'Delete'
      
      todoDelete.addEventListener('click', function(event) {
        todoLi.remove()
      })


      todoList.appendChild(todoLi)
      todoLi.appendChild(todoCheck)
      todoLi.appendChild(todoLabel)
      todoLi.appendChild(todoInput)
      todoLi.appendChild(todoEdit)
      todoLi.appendChild(todoDelete)

    }

      newTodoButton.addEventListener('click', function(event) {
        if (newTodoInput.value !== '') {
          makeTodoList(newTodoInput.value)
          newTodoInput.value = null
        }
      })





      const completedTasks = document.querySelector('#completedTasks')

      function makeCompletedTask(text) {
      const completedLi = document.createElement('li')
  
      const completedCheck = document.createElement('input')
      completedCheck.setAttribute('type', 'checkbox')

      completedCheck.addEventListener('click', function(event) {
        makeTodoList(completedLabel.innerText)
        completedLi.remove()
      })
  
      const completedLabel = document.createElement('del')
      completedLabel.innerText = text
  
      const completedInput = document.createElement('input')
  
      const completedEdit = document.createElement('button')
      completedEdit.innerText = 'Edit'

      completedEdit.addEventListener('click', function(event) {
        completedLabel.innerText = completedInput.value
        completedInput.value = null
      })
  
      const completedDelete = document.createElement('button')
      completedDelete.innerText = 'Delete'
      
      completedDelete.addEventListener('click', function(event) {
        completedLi.remove()
      })

      completedTasks.appendChild(completedLi)
      completedLi.appendChild(completedCheck)
      completedLi.appendChild(completedLabel)
      completedLi.appendChild(completedInput)
      completedLi.appendChild(completedEdit)
      completedLi.appendChild(completedDelete)


      }
  </script>
</body>
</html>
```

