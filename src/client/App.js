import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [tasks, setTasks] = useState([]);
  const [token, setToken] = useState('');
  const [title, setTitle] = useState('');
  const [assignee, setAssignee] = useState('');

  const login = async () => {
    try {
      const res = await axios.post('/api/login', { username: 'admin', password: 'securepass' });
      setToken(res.data.access_token);
    } catch (err) {
      alert('Login failed');
    }
  };

  const fetchTasks = async () => {
    if (token) {
      const res = await axios.get('/api/tasks', {
        headers: { Authorization: `Bearer ${token}` },
      });
      setTasks(res.data);
    }
  };

  const addTask = async (e) => {
    e.preventDefault();
    if (token) {
      await axios.post('/api/tasks', { title, assignee }, {
        headers: { Authorization: `Bearer ${token}` },
      });
      setTitle('');
      setAssignee('');
      fetchTasks();
    }
  };

  useEffect(() => {
    fetchTasks();
  }, [token]);

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1>Secure Task Manager</h1>
      {!token ? (
        <button onClick={login}>Login</button>
      ) : (
        <>
          <form onSubmit={addTask}>
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="Task Title"
              required
            />
            <input
              type="text"
              value={assignee}
              onChange={(e) => setAssignee(e.target.value)}
              placeholder="Assignee"
              required
            />
            <button type="submit">Add Task</button>
          </form>
          <ul>
            {tasks.map((task) => (
              <li key={task.id}>
                {task.title} - {task.assignee}
              </li>
            ))}
          </ul>
        </>
      )}
    </div>
  );
}

export default App;