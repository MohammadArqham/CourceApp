
function add_comment(){
const data = document.getElementById("question").value;
console.log(data)
const todo = {Data:data};

fetch('addComment/', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json;',
            'X-CSRFTocken': csrftoken,
        },
        body: JSON.stringify(todo),

    })

.then(
    function added(){
        console.log('sucess')
        window.open('.',target="_self")
        // btn = document.getElementById(id);
        // btn.innerHTML = "Added !";
        
    }
);
}
