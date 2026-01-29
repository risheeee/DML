function addNote() {
  const input = document.getElementById("noteInput");
  const list = document.getElementById("notesList");

  if (input.value.trim() === "") return;

  const li = document.createElement("li");

  // note text
  const span = document.createElement("span");
  span.textContent = input.value;

  // strike button
  const btn = document.createElement("button");
  btn.textContent = "Done";
  btn.onclick = function () {
    span.classList.toggle("done");
  };

  li.appendChild(span);
  li.appendChild(btn);
  list.appendChild(li);

  input.value = "";
}
