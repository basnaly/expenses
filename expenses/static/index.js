
function getMonthAndYear() {

    const selectedMonthAndYear = document.getElementById('selectMonth').value; // '2023-12'
    const selectCurrency = document.getElementById('selectCurrency').value;
    const maxMonth = document.getElementById('selectMonth').max;
    const [year, month] = selectedMonthAndYear.split('-'); // ['2023', '12']

    if (selectedMonthAndYear !== maxMonth) {
        let query = `?month=${month}&year=${year}&currency=${selectCurrency}`;
        window.location.search = query;
    }    
}


function getCurrency() {
    
    const selectedMonthAndYear = document.getElementById('selectMonth').value; // '2023-12'
    const selectCurrency = document.getElementById('selectCurrency').value;
    const maxMonth = document.getElementById('selectMonth').max;
    const [year, month] = selectedMonthAndYear.split('-'); // ['2023', '12']

    if (selectedMonthAndYear !== maxMonth) {
        let query =`?month=${month}&year=${year}&currency=${selectCurrency}`;
        window.location.search = query;
    }    
    else {
        let query =`?currency=${selectCurrency}`;
        window.location.search = query;
    }

}

