function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');


function addCart(id,action){
const todo = { idno: id,Action:action};

fetch('addCart/', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json;',
            'X-CSRFTocken': csrftoken,
        },
        body: JSON.stringify(todo),

    })

.then(
    function added(){
        btn = document.getElementById(id);
        btn.innerHTML = "Added !";
        
    }
);
}
