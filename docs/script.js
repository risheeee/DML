function addNote() {
  const input = document.getElementById("noteInput");
  const list = document.getElementById("notesList");

  if (input.value.trim() === "") return;

  const li = document.createElement("li");
  li.textContent = input.value;
  list.appendChild(li);

  input.value = "";
}
