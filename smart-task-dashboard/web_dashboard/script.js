fetch('../data/tasks.json')
  .then(response => response.json())
  .then(tasks => {
    const list = document.getElementById('taskList');
    tasks.forEach(task => {
      const li = document.createElement('li');
      li.textContent = `${task.task} — ${task.date}`;
      list.appendChild(li);
    });
  })
  .catch(err => console.error('Error loading tasks:', err));
