
const csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value;


document.querySelector("#create").addEventListener("submit", function(e) {
    e.preventDefault();
    let data = {"list_ids" : this.querySelector("#door_id_list").value.replace(" ", "").split(",")}
    
    let self = this
    fetch(`/create/`, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(data)

    }).then((response) => response.json()
    ) .then(function (response) {
        self.querySelector("#access_key").innerHTML = `Access Token : ${response["access_token"]}`
        
    })

});