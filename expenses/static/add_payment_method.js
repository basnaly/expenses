
function displayTypeOfPayment() {
    const selectedElement = document.getElementById("selectPayment").value;

    if (selectedElement == '1') {
        document.getElementById('credit_card_form').classList.remove('d-none');
        document.getElementById('cash_form').classList.add('d-none');
        document.getElementById('debit_card_form').classList.add('d-none');
    }
    else if (selectedElement == '2') {
        document.getElementById('debit_card_form').classList.remove('d-none');
        document.getElementById('credit_card_form').classList.add('d-none');
        document.getElementById('cash_form').classList.add('d-none');
    }
    else if (selectedElement == '3') {
        document.getElementById('cash_form').classList.remove('d-none');
        document.getElementById('credit_card_form').classList.add('d-none');
        document.getElementById('debit_card_form').classList.add('d-none');
    }
    else {
        document.getElementById('cash_form').classList.add('d-none');
        document.getElementById('credit_card_form').classList.add('d-none');
        document.getElementById('debit_card_form').classList.add('d-none');
    }
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


function cancelEditCreditCard() {

    document.getElementById('edit-credit-card').remove();
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


function displayEditDebitCardForm(debit_card_id, debit_card_name, debit_card_currency, debit_card_reminder, debit_card_note) {

    const existingForm = document.querySelector('#edit-debit-card');
    if (existingForm) {
        document.querySelector('#edit-debit-card').remove();
    }

    const parentElement = document.createElement('div');
    parentElement.className = 'd-flex flex-column border rounded-3 p-3';
    parentElement.id = 'edit-debit-card';
    document.querySelector('#debit-card-table').append(parentElement);

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
    inputCardNameElement.id = 'edit-debit-card-name';
    inputCardNameGroup.append(inputCardNameElement);
    inputCardNameElement.focus();
    inputCardNameElement.value = debit_card_name;

    const inputCurrencyGroup = document.createElement('div');
    inputCurrencyGroup.className = 'input-group my-3';
    editElements.append(inputCurrencyGroup);

    const spanCurrencyElement = document.createElement('span');
    spanCurrencyElement.className = 'input-group-text';
    spanCurrencyElement.innerHTML = 'Currency';
    inputCurrencyGroup.append(spanCurrencyElement);

    const inputCurrencyElement = document.createElement('input');
    inputCurrencyElement.type = 'text';    
    inputCurrencyElement.className = 'form-control';
    inputCurrencyElement.id = 'edit-currency';
    inputCurrencyGroup.append(inputCurrencyElement);
    inputCurrencyElement.value = debit_card_currency;

    const inputReminderGroup = document.createElement('div');
    inputReminderGroup.className = 'input-group my-3';
    editElements.append(inputReminderGroup);

    const spanReminderElement = document.createElement('span');
    spanReminderElement.className = 'input-group-text';
    spanReminderElement.innerHTML = 'Currency';
    inputReminderGroup.append(spanReminderElement);

    const inputReminderElement = document.createElement('input');
    inputReminderElement.type = 'text';    
    inputReminderElement.className = 'form-control';
    inputReminderElement.id = 'edit-reminder';
    inputReminderGroup.append(inputReminderElement);
    inputReminderElement.value = debit_card_reminder;

    const inputNoteGroup = document.createElement('div');
    inputNoteGroup.className = 'input-group my-3';
    editElements.append(inputNoteGroup);

    const spanNoteElement = document.createElement('span');
    spanNoteElement.className = 'input-group-text';
    spanNoteElement.innerHTML = 'Note';
    inputNoteGroup.append(spanNoteElement);

    const inputNoteElement = document.createElement('input');
    inputNoteElement.type = 'text';    
    inputNoteElement.className = 'form-control';
    inputNoteElement.id = 'edit-note';
    inputNoteGroup.append(inputNoteElement);
    inputNoteElement.value = debit_card_note;

    const buttonsElement = document.createElement('div');
    buttonsElement.className = 'd-flex justify-content-evenly mb-2';
    parentElement.appendChild(buttonsElement)

    const cancelButton = document.createElement('button');
    cancelButton.className = 'btn cancel-button m-2';
    cancelButton.type = 'button';
    cancelButton.innerHTML = 'Cancel'
    buttonsElement.append(cancelButton);
    cancelButton.addEventListener('click', () => cancelEditDebitCard());

    const saveButton = document.createElement('button');
    saveButton.className = 'btn save-button m-2';
    saveButton.type = 'button';
    saveButton.innerHTML = 'Save'
    buttonsElement.append(saveButton);
    saveButton.addEventListener('click', () => editDebitCard(debit_card_id));

}


function displayAddDebitCardAmountForm(debit_card_id, debit_card_currency, debit_card_card_name) {

    const existingForm = document.getElementById('show-add-amount-debit');
    if (existingForm) {
        existingForm.remove();
    }

    const parentElement = document.createElement('div');
    parentElement.className = 'd-flex flex-column border rounded-3 p-3 shadow';
    parentElement.id = 'show-add-amount-debit';
    document.getElementById('debit-card-table').append(parentElement);

    const inputAmountDebitCardGroup = document.createElement('div');
    inputAmountDebitCardGroup.className = 'input-group my-3';
    parentElement.append(inputAmountDebitCardGroup);

    const spanAmountDebitCard = document.createElement('span');
    spanAmountDebitCard.className = 'input-group-text';
    spanAmountDebitCard.innerHTML = `Add ${ debit_card_currency } on ${debit_card_card_name} card`;
    inputAmountDebitCardGroup.append(spanAmountDebitCard);

    const inputAmountDebitCard = document.createElement('input');
    inputAmountDebitCard.className = 'form-control';
    inputAmountDebitCard.id = 'add-amount-debit-card';
    inputAmountDebitCardGroup.append(inputAmountDebitCard);
    inputAmountDebitCard.focus();

    const buttonsElement = document.createElement('div');
    buttonsElement.className = 'd-flex justify-content-evenly mb-2';
    parentElement.append(buttonsElement);

    const cancelButton = document.createElement('button');
    cancelButton.className = 'btn cancel-button m-2';
    cancelButton.type = 'button';
    cancelButton.innerHTML = 'Cancel';
    buttonsElement.append(cancelButton);
    cancelButton.addEventListener('click', () => cancelAddAmountDebitCard());


    const saveButton = document.createElement('button');
    saveButton.className = 'btn save-button m-2';
    saveButton.type = 'button';
    saveButton.innerHTML = 'Save';
    buttonsElement.append(saveButton);
    saveButton.addEventListener('click', () => saveAddAmountDebitCard(debit_card_id))
}


function cancelAddAmountDebitCard() {
    document.getElementById('show-add-amount-debit').remove
}


function saveAddAmountDebitCard(debit_card_id) {

    const add_money = document.getElementById('add-amount-debit-card').value;

    fetch(`add_money_debit_card/${debit_card_id}`, {
        method: "POST",
        body: JSON.stringify({
            add_money: add_money
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        const messageElement = document.createElement('div');
        messageElement.className = 'alert shadow alert-success';
        messageElement.role = 'alert';
        document.getElementById('message').append(messageElement);
        messageElement.innerHTML = data.message;

        setTimeout(() => {
            messageElement.innerHTML = '';
            window.location.replace(window.location.href);
        }, 5000)

    })
    .catch(error => {
        "Error:", error
    })
}


function editDebitCard(debit_card_id) {

    const changed_card_name = document.getElementById('edit-debit-card-name').value;
    const changed_currency = document.getElementById('edit-currency').value;
    const changed_reminder = document.getElementById('edit-reminder').value;
    const changed_note = document.getElementById('edit-note').value;

    fetch(`edit_debit_card/${debit_card_id}`, {
        method: "POST",
        body: JSON.stringify({
            changed_card_name: changed_card_name,
            changed_currency: changed_currency,
            changed_reminder: changed_reminder,
            changed_note: changed_note
        })
    })
    .then(response => response.json())
    .then(data => {

        const messageElement = document.createElement('div');
        messageElement.className = 'alert shadow alert-success';
        messageElement.role = 'alert';
        document.getElementById('message').append(messageElement);
        messageElement.innerHTML = data.message;

        setTimeout(() => {
            messageElement.innerHTML = '';
            window.location.replace(window.location.href);
        }, 5000)
    })
    .catch(error => {
        "Error:", error
    })
}


function cancelEditDebitCard() {

    document.getElementById('edit-debit-card').remove();
}


function deleteDebitCard(debit_card_id) {

    fetch(`delete_debit_card/${debit_card_id}`, {
        method: "DELETE"
    })
    .then(response => response.json())
    .then(data => {
        const messageElement = document.createElement('div');
        messageElement.className = 'alert shadow alert-success';
        messageElement.role = 'alert';
        document.getElementById('message').append(messageElement);
        messageElement.innerHTML = data.message;

        setTimeout(() => {
            messageElement.innerHTML = '';
            window.location.replace(window.location.href);
        }, 5000)
    })
    .catch(error => {
        "Error:", error
    })
}


function displayCashForm(cash_id, cash_currency) {

    const exsistingForm = document.getElementById('show-add-cash');
    if (exsistingForm) {
        exsistingForm.remove();
    }

    const parentElement = document.createElement('div');
    parentElement.className = 'd-flex flex-column border rounded-3 p-3 shadow';
    parentElement.id = 'show-add-cash';
    document.querySelector('#cash-table').append(parentElement);

    const inputGroup = document.createElement('div');
    inputGroup.className = 'input-group my-3';
    parentElement.append(inputGroup);

    const spanElement = document.createElement('span');
    spanElement.className = 'input-group-text';
    spanElement.innerHTML = `Add ${ cash_currency } cash`;
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


function cancelAddCash() {
    document.getElementById('show-add-cash').remove();
}


function displayEditCashForm(cash_id, cash_currency, cash_reminder) {

    const exsistingForm = document.getElementById('edit-cash');
    if (exsistingForm) {
        exsistingForm.remove();
    }

    const parentElement = document.createElement('div');
    parentElement.className = 'd-flex flex-column border rounded-3 p-3';
    parentElement.id = 'edit-cash';
    document.querySelector('#cash-table').append(parentElement);

    const editElements = document.createElement('div');
    editElements.className = 'd-flex flex-column';
    parentElement.append(editElements);

    const inputCashCurrencyGroup = document.createElement('div');
    inputCashCurrencyGroup.className = 'input-group my-3';
    editElements.append(inputCashCurrencyGroup);

    const spanCashCurrencyElement = document.createElement('span');
    spanCashCurrencyElement.className = 'input-group-text';
    spanCashCurrencyElement.innerHTML = 'Currency';
    inputCashCurrencyGroup.append(spanCashCurrencyElement);

    const inputCashCurrencyElement = document.createElement('input');
    inputCashCurrencyElement.type = 'text';    
    inputCashCurrencyElement.className = 'form-control';
    inputCashCurrencyElement.id = 'cash-currency';
    inputCashCurrencyGroup.append(inputCashCurrencyElement);
    inputCashCurrencyElement.focus();
    inputCashCurrencyElement.value = cash_currency;

    const inputReminderCashGroup = document.createElement('div');
    inputReminderCashGroup.className = 'input-group my-3';
    editElements.append(inputReminderCashGroup);

    const spanReminderCashElement = document.createElement('span');
    spanReminderCashElement.className = 'input-group-text';
    spanReminderCashElement.innerHTML = 'Reminder';
    inputReminderCashGroup.append(spanReminderCashElement);

    const inputReminderCashElement = document.createElement('input');
    inputReminderCashElement.type = 'number';    
    inputReminderCashElement.className = 'form-control';
    inputReminderCashElement.id = 'cash-reminder';
    inputReminderCashGroup.append(inputReminderCashElement);
    inputReminderCashElement.value = cash_reminder;

    const buttonsElement = document.createElement('div');
    buttonsElement.className = 'd-flex justify-content-evenly mb-2';
    parentElement.appendChild(buttonsElement)

    const cancelButton = document.createElement('button');
    cancelButton.className = 'btn cancel-button m-2';
    cancelButton.type = 'button';
    cancelButton.innerHTML = 'Cancel'
    buttonsElement.append(cancelButton);
    cancelButton.addEventListener('click', () => cancelEditCash());

    const saveButton = document.createElement('button');
    saveButton.className = 'btn save-button m-2';
    saveButton.type = 'button';
    saveButton.innerHTML = 'Save'
    buttonsElement.append(saveButton);
    saveButton.addEventListener('click', () => editCash(cash_id));
}


function editCash(cash_id) {

    const changed_cash_currency = document.getElementById('cash-currency').value;
    const changed_cash_reminder = document.getElementById('cash-reminder').value;

    fetch(`edit_cash/${cash_id}`, {
        method: "POST",
        body: JSON.stringify({
            changed_cash_currency: changed_cash_currency,
            changed_cash_reminder: changed_cash_reminder
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)

        const messageElement = document.createElement('div');
        messageElement.className = 'alert shadow alert-success';
        messageElement.role = 'alert';
        document.getElementById('message').append(messageElement);
        messageElement.innerHTML = data.message;

        setTimeout(() => {
            document.getElementById('message').innerHTML = '';
            window.location.reload(window.location.href)
        }, 5000)
    })
    .catch(error => {
        console.log("Error:", error)
    })
}


function cancelEditCash() {
    document.getElementById('edit-cash').remove();
}


function deleteCash(cash_id) {

    fetch(`delete_cash/${cash_id}`, {
        method: "DELETE"
    })
    .then(response => response.json())
    .then(data => {
        const messageElement = document.createElement('div');
        messageElement.className = 'alert alert-success shadow';
        messageElement.role = 'alert';
        document.getElementById('message').append(messageElement);
        messageElement.innerHTML = data.message;

        setTimeout(() => {
            document.getElementById('message').innerHTML = '';
            window.location.replace(window.location.href);
        }, 5000)

    })
    .catch(error => {
        console.log("Error:", error)
    })
}

