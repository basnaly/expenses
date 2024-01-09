
function getMonthAndYear() {

    const selectedMonthAndYear = document.getElementById('selectMonth').value; // '2023-12'
    const [year, month] = selectedMonthAndYear.split('-'); // ['2023', '12']

    let query = `?month=${month}&year=${year}`;
    window.location.search = query;
}