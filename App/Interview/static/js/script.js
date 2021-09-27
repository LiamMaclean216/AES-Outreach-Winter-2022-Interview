
const csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value;


document.querySelector("#create").addEventListener("submit", function(e) {
    e.preventDefault();
    let data = JSON.stringify({"list_ids" : this.querySelector("#door_id_list").value.replace(" ", "").split(",")})
    let url = `/create/`

    document.querySelector("#b_sent").innerHTML = `Sending POST request to url ${url} with body ${data}`

    let self = this
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: data

    }).then((response) => response.json()
    ) .then(function (response) {
        self.querySelector("#access_key").innerHTML = `Access Token : ${response["access_token"]}`
        document.querySelector("#b_received").innerHTML = `Received : ${JSON.stringify(response)}`
    })

});

document.querySelector("#validate").addEventListener("submit", function(e) {
    e.preventDefault();
    let id = this.querySelector("#door_id_val").value.replace(" ", "")
    let token = this.querySelector("#acess_key").value.replace(" ", "")
    
    let url = `/validate/${id}/${token}`
    document.querySelector("#b_sent").innerHTML = `Sending GET request to url ${url}`

    let self = this
    fetch(url, {
        method: 'GET',

    }).then((response) => response.json()
    ) .then(function (response) {
        self.querySelector("#is_valid").innerHTML = response["is_valid"] ? "valid" : "invalid"

        document.querySelector("#b_received").innerHTML = `Received : ${JSON.stringify(response)}`
    })

});