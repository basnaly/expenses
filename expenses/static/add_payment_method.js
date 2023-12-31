
function displayTypeOfPayment() {
    const selectedElement = document.getElementById("selectPayment").value;

    if (selectedElement == '1') {
        document.getElementById('cash_form').classList.add('d-none');
        document.getElementById('credit_card_form').classList.remove('d-none');
    }
    else if (selectedElement == '2') {
        document.getElementById('credit_card_form').classList.add('d-none');
        document.getElementById('cash_form').classList.remove('d-none');
    }
    else {
        document.getElementById('cash_form').classList.add('d-none');
        document.getElementById('credit_card_form').classList.add('d-none');
    }
}

function deleteCreditCard(credit_card_id) {
    fetch(`delete_credit_card/${credit_card_id}`, {
        method: "DELETE"
    })
    .then(response => response.json())
    .then(data => {
        const messageElement = document.createElement('div');
        messageElement.className = '';
        messageElement.id = 'message';
        document.querySelector('#display-items').prepend(messageElement);
        document.querySelector('#message').innerHTML = data.message;

        setTimeout(() => {
            document.querySelector('#message').innerHTML = '';
            window.location.replace(window.location.href);
        }, 10000)
    })
}