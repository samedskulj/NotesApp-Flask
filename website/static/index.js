function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((res) => {
    window.location.href = "/";
  });
}

function test() {
  console.log("test");
}
