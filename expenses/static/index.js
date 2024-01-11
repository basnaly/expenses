
function getMonthAndYear() {

    const selectedMonthAndYear = document.getElementById('selectMonth').value; // '2023-12'
    const maxMonth = document.getElementById('selectMonth').max;
    const [year, month] = selectedMonthAndYear.split('-'); // ['2023', '12']

    if (selectedMonthAndYear !== maxMonth) {
        let query = `?month=${month}&year=${year}`;
        window.location.search = query;
    }    
}