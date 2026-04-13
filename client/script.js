const API = "http://127.0.0.1:8001";

// ── NOTES ──────────────────────────────────────────

async function loadNotes() {
  const res = await fetch(`${API}/notes`);
  const notes = await res.json();
  const list = document.getElementById("notes-list");
  list.innerHTML = "";
  notes.forEach(n => {
    const li = document.createElement("li");
    li.className = "card";
    li.innerHTML = `<strong>${n.title}</strong><p>${n.content}</p>`;
    list.appendChild(li);
  });
}

document.getElementById("note-form").addEventListener("submit", async e => {
  e.preventDefault();
  const title = document.getElementById("note-title").value.trim();
  const content = document.getElementById("note-content").value.trim();
  await fetch(`${API}/notes`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title, content })
  });
  e.target.reset();
  loadNotes();
});

// ── TODOS ──────────────────────────────────────────

async function loadTodos() {
  const res = await fetch(`${API}/todos`);
  const todos = await res.json();
  const list = document.getElementById("todos-list");
  list.innerHTML = "";
  todos.forEach(t => {
    const li = document.createElement("li");
    li.className = "card";
    const taskItems = t.tasks.map(task =>
      `<li>${task.text}${task.completed ? " ✓" : ""}</li>`
    ).join("");
    li.innerHTML = `<strong>${t.title}</strong><ul>${taskItems}</ul>`;
    list.appendChild(li);
  });
}

document.getElementById("add-task-btn").addEventListener("click", () => {
  const container = document.getElementById("tasks-container");
  const input = document.createElement("input");
  input.className = "task-input";
  input.type = "text";
  input.placeholder = `Task ${container.children.length + 1}`;
  container.appendChild(input);
});

document.getElementById("todo-form").addEventListener("submit", async e => {
  e.preventDefault();
  const title = document.getElementById("todo-title").value.trim();
  const taskInputs = document.querySelectorAll(".task-input");
  const tasks = Array.from(taskInputs)
    .map(i => i.value.trim())
    .filter(v => v !== "")
    .map(text => ({ text, completed: false }));
  await fetch(`${API}/todos`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title, tasks })
  });
  e.target.reset();
  document.getElementById("tasks-container").innerHTML =
    '<input class="task-input" type="text" placeholder="Task 1"/>';
  loadTodos();
});

// ── INIT ───────────────────────────────────────────
loadNotes();
loadTodos();