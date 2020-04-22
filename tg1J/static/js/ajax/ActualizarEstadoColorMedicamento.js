$("#actualizarEstadoColor").click(function() {

    $.ajax({
        url: '{% url "class ActualizarColorMedicamentos" %}',
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

