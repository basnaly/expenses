
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
        messageElement.className = 'alert shadow alert-success';
        messageElement.role = 'alert';
        document.querySelector('#message').append(messageElement);
        messageElement.innerHTML = data.message;

        setTimeout(() => {
            document.querySelector('#message').innerHTML = '';
            window.location.replace(window.location.href);
        }, 5000)
    })
    .catch(error => {
        console.log('Error:', error)
    })
}


function displayCashForm(cash_id) {

    const exsistingForm = document.getElementById('show-add-cash');
    if (exsistingForm) {
        exsistingForm.remove();
    }

    const parentElement = document.createElement('div');
    parentElement.className = 'd-flex flex-column border rounded-3 p-3';
    parentElement.id = 'show-add-cash';
    document.querySelector('#cash-table').append(parentElement);

    const inputGroup = document.createElement('div');
    inputGroup.className = 'input-group my-3';
    parentElement.append(inputGroup);

    const spanElement = document.createElement('span');
    spanElement.className = 'input-group-text';
    spanElement.innerHTML = 'Add cash';
    inputGroup.append(spanElement);

    const inputElement = document.createElement('input');
    inputElement.type = 'text';    
    inputElement.className = 'form-control';
    inputElement.id = 'add-amount-cash';
    inputGroup.append(inputElement);
    inputElement.focus();

    const buttonsElement = document.createElement('div');
    buttonsElement.className = 'd-flex justify-content-evenly mb-2';
    parentElement.appendChild(buttonsElement)

    const cancelButton = document.createElement('button');
    cancelButton.className = 'btn cancel-button m-2';
    cancelButton.type = 'button';
    cancelButton.innerHTML = 'Cancel'
    buttonsElement.append(cancelButton);
    cancelButton.addEventListener('click', () => cancelAddCash());

    const saveButton = document.createElement('button');
    saveButton.className = 'btn save-button m-2';
    saveButton.type = 'button';
    saveButton.innerHTML = 'Save'
    buttonsElement.append(saveButton);
    saveButton.addEventListener('click', () => addAmountCash(cash_id));
}


function cancelAddCash() {
    document.getElementById('show-add-cash').remove();
}


function addAmountCash(cash_id) {

    const add_cash = document.getElementById('add-amount-cash').value;

    fetch(`add_cash/${cash_id}`, {
        method: 'POST',
        body: JSON.stringify({
            add_cash: add_cash
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        if (data.message) {

            const messageElement = document.createElement('div');
            messageElement.className = 'alert shadow alert-success';
            messageElement.role = 'alert';
            document.getElementById('message').append(messageElement);
            messageElement.innerHTML = data.message;

            setTimeout(() => {
                document.getElementById('message').innerHTML = '';
                window.location.replace(window.location.href);
            }, 5000)
        }
    })
    .catch(error => {
        console.log('Error:', error);
    })
}


function displayEditCreditCardForm(credit_card_id, credit_card_name, expired_date) {

    const exsistingForm = document.getElementById('edit-credit-card');
    if (exsistingForm) {
        exsistingForm.remove();
    }

    const parentElement = document.createElement('div');
    parentElement.className = 'd-flex flex-column border rounded-3 p-3';
    parentElement.id = 'edit-credit-card';
    document.querySelector('#credit-card-table').append(parentElement);

    const editElements = document.createElement('div');
    editElements.className = 'd-flex flex-column';
    parentElement.append(editElements);

    const inputCardNameGroup = document.createElement('div');
    inputCardNameGroup.className = 'input-group my-3';
    editElements.append(inputCardNameGroup);

    const spanCardNameElement = document.createElement('span');
    spanCardNameElement.className = 'input-group-text';
    spanCardNameElement.innerHTML = 'Name of card';
    inputCardNameGroup.append(spanCardNameElement);

    const inputCardNameElement = document.createElement('input');
    inputCardNameElement.type = 'text';    
    inputCardNameElement.className = 'form-control';
    inputCardNameElement.id = 'edit-card-name';
    inputCardNameGroup.append(inputCardNameElement);
    inputCardNameElement.focus();
    inputCardNameElement.value = credit_card_name;

    const inputExpiredDateGroup = document.createElement('div');
    inputExpiredDateGroup.className = 'input-group my-3';
    editElements.append(inputExpiredDateGroup);

    const spanExpiredDateElement = document.createElement('span');
    spanExpiredDateElement.className = 'input-group-text';
    spanExpiredDateElement.innerHTML = 'Expired date';
    inputExpiredDateGroup.append(spanExpiredDateElement);

    const inputExpiredDateElement = document.createElement('input');
    inputExpiredDateElement.type = 'date';    
    inputExpiredDateElement.className = 'form-control';
    inputExpiredDateElement.id = 'edit-expired-date';
    inputExpiredDateGroup.append(inputExpiredDateElement);
    inputExpiredDateElement.value = expired_date;
    console.log(expired_date);

    const buttonsElement = document.createElement('div');
    buttonsElement.className = 'd-flex justify-content-evenly mb-2';
    parentElement.appendChild(buttonsElement)

    const cancelButton = document.createElement('button');
    cancelButton.className = 'btn cancel-button m-2';
    cancelButton.type = 'button';
    cancelButton.innerHTML = 'Cancel'
    buttonsElement.append(cancelButton);
    cancelButton.addEventListener('click', () => cancelEditCreditCard());

    const saveButton = document.createElement('button');
    saveButton.className = 'btn save-button m-2';
    saveButton.type = 'button';
    saveButton.innerHTML = 'Save'
    buttonsElement.append(saveButton);
    saveButton.addEventListener('click', () => editCreditCard(credit_card_id));
    
}


function cancelEditCreditCard() {

    document.getElementById('edit-credit-card').remove();
}


function editCreditCard(credit_card_id) {

    const changed_card_name = document.getElementById('edit-card-name').value;
    const changed_expiried_date = document.getElementById('edit-expired-date').value;

    fetch(`edit_credit_card/${credit_card_id}`, {
        method: 'POST',
        body: JSON.stringify({
            changed_card_name: changed_card_name,
            changed_expiried_date: changed_expiried_date
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        if (data.message) {

            const messageElement = document.createElement('div');
            messageElement.className = 'alert shadow alert-success';
            messageElement.role = 'alert';
            document.getElementById('message').append(messageElement);
            messageElement.innerHTML = data.message;

            setTimeout(() => {
                document.getElementById('message').innerHTML = '';
                window.location.replace(window.location.href);
            }, 5000)
        }
    })
    .catch(error => {
        console.log('Error:', error);
    })
}