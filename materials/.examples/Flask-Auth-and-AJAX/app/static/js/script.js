const form = document.querySelector('#ajax-form');
const titleInput = document.querySelector('#title-input-ajax');
const todosList = document.querySelector('#todos');

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    try {
        const response = await fetch('/api/todos', {
            method: 'POST',
            credentials: 'same-origin',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                title: titleInput.value,
            }),
        });
        if (!response.ok) {
            alert(await response.text());
            return;
        }
        const newTodo = await response.json();
        const newListItem = document.createElement('li');
        newListItem.classList.add('list-group-item');
        newListItem.textContent = newTodo.title;
        newListItem.setAttribute('data-todo-id', newTodo.id);
        const deleteButton = document.createElement('button');
        deleteButton.type = 'button';
        deleteButton.classList.add('btn', 'btn-outline-danger', 'btn-sm');
        deleteButton.textContent = '❌';
        deleteButton.addEventListener('click', () => deleteTodo(newTodo.id));
        newListItem.appendChild(deleteButton);
        todosList.appendChild(newListItem);
    } catch (e) {
        alert(e.message);
    }
});

async function deleteTodo(todoId) {
    try {
        const response = await fetch(`/api/todos/${todoId}`, {
            method: 'DELETE',
            credentials: 'same-origin',
        });
        if (!response.ok) {
            alert(await response.text());
            if (response.status === 401) {
                window.location = '/login';
            }
            return;
        }
        document.querySelector(`li[data-todo-id='${todoId}']`).remove();
    } catch (e) {
        alert(e.message);
    }
}
