var a = document.getElementById("summarized")

a.innerText = "Heloo worlds"


$.ajax({
    type: "POST",
    url: "~/pythoncode.py",
    data: { param: text}
  }).done(function( o ) {
     // do something
  });