$("#actualizarEstadoColorDispostivo").click(function() {

    $.ajax({
        url: '{% url "ActualizarColorDispositivos" %}',
        data: {
            'code': 'true',
        },
        dataType: 'json',
        success: function (data) {
            alert("Salio melo");
        }

    });
    return false;
});
