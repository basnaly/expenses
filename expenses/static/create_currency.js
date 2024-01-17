
function displayEditCurrencyForm (currency_id, currency_name ) {

    const existingForm = document.getElementById('edit-currency');
    if (existingForm) {
        existingForm.remove();
    }

    const parentElement = document.createElement('div');
    parentElement.className = 'd-flex flex-column border rounded-3 p-3';
    parentElement.id = 'edit-currency';
    document.querySelector('#currency-table').append(parentElement);

    const editElements = document.createElement('div');
    editElements.className = 'd-flex flex-column';
    parentElement.append(editElements);

    const inputCardNameGroup = document.createElement('div');
    inputCardNameGroup.className = 'input-group my-3';
    editElements.append(inputCardNameGroup);

    const spanCardNameElement = document.createElement('span');
    spanCardNameElement.className = 'input-group-text';
    spanCardNameElement.innerHTML = 'Currency Name';
    inputCardNameGroup.append(spanCardNameElement);

    const inputCardNameElement = document.createElement('input');
    inputCardNameElement.type = 'text';    
    inputCardNameElement.className = 'form-control';
    inputCardNameElement.id = 'edit-currency-name';
    inputCardNameGroup.append(inputCardNameElement);
    inputCardNameElement.focus();
    inputCardNameElement.value = currency_name;

    const buttonsElement = document.createElement('div');
    buttonsElement.className = 'd-flex justify-content-evenly mb-2';
    parentElement.appendChild(buttonsElement)

    const cancelButton = document.createElement('button');
    cancelButton.className = 'btn cancel-button m-2';
    cancelButton.type = 'button';
    cancelButton.innerHTML = 'Cancel'
    buttonsElement.append(cancelButton);
    cancelButton.addEventListener('click', () => cancelEditCurrency());

    const saveButton = document.createElement('button');
    saveButton.className = 'btn save-button m-2';
    saveButton.type = 'button';
    saveButton.innerHTML = 'Save'
    buttonsElement.append(saveButton);
    saveButton.addEventListener('click', () => editCurrency(currency_id));  
}

function cancelEditCurrency() {
    document.getElementById('edit-currency').remove();
}

function editCurrency(currency_id) {

    const changed_currency_name = document.getElementById('edit-currency-name').value;

    fetch(`edit_currency/${currency_id}`, {
        method: "POST",
        body: JSON.stringify({
            changed_currency_name: changed_currency_name
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            const messageElement = document.createElement('div');
            messageElement.className = 'alert shadow alert-success';
            messageElement.role = 'alert';
            document.getElementById('display-items').append(messageElement);
            messageElement.innerHTML = data.message;

            setTimeout(() => {
                messageElement.innerHTML = '';
                window.location.replace(window.location.href);
            }, 5000)
        }
    })
    .catch(error => {
        console.log("Error:", error)
    })
}


function deleteCurrency(currency_id) {

    fetch(`delete_currency/${currency_id}`, {
        method: "DELETE"
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            const messageElement = document.createElement('div');
            messageElement.className = 'alert shadow alert-success';
            messageElement.role = 'alert';
            document.getElementById('display-items').append(messageElement);
            messageElement.innerHTML = data.message;

            setTimeout(() => {
                messageElement.innerHTML = '';
                window.location.replace(window.location.href);
            }, 5000)
        }
    })
}