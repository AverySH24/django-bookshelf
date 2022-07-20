console.log("HELLO")

function saveBook(){
  // Remember to add '.value'
  title = document.getElementById("newTitle").value
  author = document.getElementById("newAuthor").value
  description = document.getElementById("newDescription").value

  // "" is re-running this url but now in a POST request
  axios.post("", {title : title, author : author, description: description}).then((response) => {
    // Redirecting from JS based on your current url
    // Example: if current url = "genres/books/2/"
    // ../../ will cut off two of the last snippets of your url and run "genres/"
    window.location.href = "../../"
	})

}

function editBook(){
  title = document.getElementById("newTitle").value
  author = document.getElementById("newAuthor").value
  description = document.getElementById("newDescription").value

  axios.post("", {title : title, author : author, description: description}).then((response) => {
    window.location.href = "../../../"
	})

}