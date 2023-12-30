
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