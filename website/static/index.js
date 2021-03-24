function deleteNode(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((res) => {
    window.location.href = "/";
  });
}
