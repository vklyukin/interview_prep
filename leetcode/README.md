# Solved problems from Leetcode

<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
    google.charts.load('current', {'packages':['corechart']});
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {

    var data = google.visualization.arrayToDataTable([
        ['Level', 'Amount'],
        ['Easy', 25],
        ['Medium', 15],
        ['Hard', 2],
    ]);

    var options = {
        title: 'Solved Problems by Level'
    };

    var chart = new google.visualization.PieChart(document.getElementById('piechart'));

    chart.draw(data, options);
    }
</script>

<div id="piechart" style="width: 900px; height: 500px;"></div>

| **Easy** | **Medium** | **Hard** | **Total** |
| -------- | ---------- | -------- | --------- |
| 25       | 15         | 2        | 42        |
